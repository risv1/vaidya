from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, collect_list, lit, when
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer
from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml import Pipeline
from pyspark.ml.pipeline import PipelineModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import pandas as pd
import json
import os
from dotenv import load_dotenv

class SparkCropRecommender:
    def __init__(self, spark):
        self.spark = spark
        self.feature_names = ['LATITUDE', 'LONGITUDE', 'TEMPERATURE', 'HUMIDITY', 'RAINFALL']
        self.target_features = ['N_SOIL', 'P_SOIL', 'K_SOIL', 'ph', 'CROP_PRICE']
        self.model = None
        self.pipeline = None
        self.label_indexer = None
        self.crop_stats = {}
        self.label_indexer_model = None
        
        with open ('crop_stats_test_spark.txt', 'r') as f:
            self.crop_stats = json.load(f)
            
        self.state_coordinates = {
            'Andaman and Nicobar': (10.7449, 92.5000),
            'Andhra Pradesh': (15.9129, 79.7400),
            'Assam': (26.2006, 92.9376),
            'Chattisgarh': (21.2787, 81.8661),
            'Goa': (15.2993, 74.1240),
            'Gujarat': (22.6708, 71.5724),
            'Haryana': (29.0588, 76.0856),
            'Himachal Pradesh': (32.1024, 77.5619),
            'Jammu and Kashmir': (33.2778, 75.3412),
            'Karnataka': (15.3173, 75.7139),
            'Kerala': (10.1632, 76.6413),
            'Madhya Pradesh': (22.9734, 78.6569),
            'Maharashtra': (19.7515, 75.7139),
            'Manipur': (24.6637, 93.9063),
            'Meghalaya': (25.4670, 91.3662),
            'Nagaland': (26.1584, 94.5624),
            'Odisha': (20.2376, 84.2700),
            'Pondicherry': (11.9416, 79.8083),
            'Punjab': (31.1471, 75.3412),
            'Rajasthan': (27.0238, 74.2179),
            'Tamil Nadu': (11.1271, 78.6569),
            'Telangana': (18.1124, 79.0193),
            'Tripura': (23.5639, 91.6761),
            'Uttar Pradesh': (27.5706, 80.0982),
            'Uttrakhand': (29.2163, 79.0108),
            'West Bengal': (22.9868, 87.8550)
        }
        
    def prepare_data(self, input_path):
        pdf = pd.read_csv(input_path)
        df = self.spark.createDataFrame(pdf)
        
        df = df.withColumn('LATITUDE', lit(0.0))
        df = df.withColumn('LONGITUDE', lit(0.0))
        
        for state, (lat, long) in self.state_coordinates.items():
            df = df.withColumn(
                'LATITUDE',
                when(col('STATE') == state, lit(float(lat))).otherwise(col('LATITUDE'))
            )
            df = df.withColumn(
                'LONGITUDE',
                when(col('STATE') == state, lit(float(long))).otherwise(col('LONGITUDE'))
            )
        
        self.spark.sparkContext.setLogLevel("ERROR")
        
        crop_stats_df = df.groupBy('CROP').agg(
            mean('N_SOIL').alias('avg_N'),
            mean('P_SOIL').alias('avg_P'),
            mean('K_SOIL').alias('avg_K'),
            mean('ph').alias('avg_ph'),
            mean('CROP_PRICE').alias('avg_price')
        )
        
        self.crop_stats = {row['CROP']: {
            'avg_params': [row['avg_N'], row['avg_P'], row['avg_K'], row['avg_ph']],
            'avg_price': row['avg_price']
        } for row in crop_stats_df.collect()}
        
        assembler = VectorAssembler(
            inputCols=self.feature_names,
            outputCol="features"
        )
        
        scaler = StandardScaler(
            inputCol="features",
            outputCol="scaledFeatures",
            withStd=True,
            withMean=True
        )
        
        self.label_indexer = StringIndexer(
            inputCol="CROP",
            outputCol="label"
        )

        layers = [len(self.feature_names), 128, 128, len(self.crop_stats)]
        classifier = MultilayerPerceptronClassifier(
            maxIter=100,
            layers=layers,
            featuresCol="scaledFeatures",
            labelCol="label",
            predictionCol="prediction",
            seed=42
        )

        self.pipeline = Pipeline(stages=[
            assembler,
            scaler,
            self.label_indexer,
            classifier
        ])
        
        return df
    
    def train(self, df):
        train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

        self.model = self.pipeline.fit(train_data)
        
        self.label_indexer_model = self.model.stages[2]
        
        predictions = self.model.transform(test_data)
        evaluator = MulticlassClassificationEvaluator(
            labelCol="label",
            predictionCol="prediction",
            metricName="accuracy"
        )
        accuracy = evaluator.evaluate(predictions)
        print(f"Test Accuracy = {accuracy}")
        
        return self.model
    
    def predict(self, latitude, longitude, temperature, humidity, rainfall):
        pred_data = self.spark.createDataFrame(
            [(latitude, longitude, temperature, humidity, rainfall)],
            self.feature_names
        )
    
        predictions = self.model.transform(pred_data)

        prob_scores = predictions.select("probability").collect()[0][0]

        label_map = {float(idx): label for idx, label in enumerate(self.label_indexer_model.labels)}

        recommendations = []
        top_3_indices = (-prob_scores).argsort()[:3]

        for idx in top_3_indices:
            crop_name = label_map[float(idx)]
            confidence = float(prob_scores[int(idx)]) * 100

            avg_params = self.crop_stats[crop_name]['avg_params']
            avg_price = self.crop_stats[crop_name]['avg_price']

            recommendations.append({
                'crop': crop_name,
                'confidence': confidence,
                'soil_requirements': {
                    'N': round(float(avg_params[0]), 2),
                    'P': round(float(avg_params[1]), 2),
                    'K': round(float(avg_params[2]), 2),
                    'pH': round(float(avg_params[3]), 2)
                },
                'estimated_price': round(float(avg_price), 2)
            })

        return recommendations

    def load_model(self, model_path):
        self.model = PipelineModel.load(model_path)
        self.label_indexer_model = self.model.stages[2] 
        print("Model loaded successfully from", model_path)

def save_crop_stats(recommender, output_path):
    with open(output_path, 'w') as f:
        json.dump(recommender.crop_stats, f, indent=4)
    print("Crop stats saved successfully!")

def main():
    load_dotenv()
    spark = SparkSession.builder \
        .appName("CropRecommendation") \
        .config("spark.driver.host", os.getenv('SPARK_BINDADDR')) \
        .config("spark.driver.bindAddress", os.getenv('SPARK_BINDADDR')) \
        .config("spark.executor.memory", "1g") \
        .config("spark.driver.memory", "1g") \
        .master("local[*]") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")
        
    recommender = SparkCropRecommender(spark)
    
    df = recommender.prepare_data('src/data/indiancrop_dataset.csv')
    model = recommender.train(df)
    
    save_crop_stats(recommender, 'crop_stats_test_spark.txt')
    
    latitude = 10.7449
    longitude = 92.5000
    temperature = 21.0
    humidity = 82.0
    rainfall = 202.0
    
    recommendations = recommender.predict(
        latitude=latitude,
        longitude=longitude,
        temperature=temperature,
        humidity=humidity,
        rainfall=rainfall
    )
    
    print("\nCrop Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['crop']} (Confidence: {rec['confidence']:.2f}%)")
        print("Soil Requirements:")
        print(f"  - Nitrogen (N): {rec['soil_requirements']['N']}")
        print(f"  - Phosphorous (P): {rec['soil_requirements']['P']}")
        print(f"  - Potassium (K): {rec['soil_requirements']['K']}")
        print(f"  - pH: {rec['soil_requirements']['pH']}")
        print(f"Estimated Price: ₹{rec['estimated_price']}")
    
    model.save("spark_crop_recommender")
    
    spark.stop()

if __name__ == "__main__":
    main()
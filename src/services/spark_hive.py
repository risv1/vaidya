from pyspark.sql import SparkSession
from schema import CropSchema, WindSchema, AQISchema, SolarSchema

spark = SparkSession.builder \
    .appName("Python Spark SQL basic example") \
    .config("hive.metastore.uris", "thrift://localhost:9083") \
    .enableHiveSupport() \
    .getOrCreate()

def create_db_and_tables():    
    databases = spark.sql("show databases")
    databases.show()

    spark.sql("CREATE DATABASE IF NOT EXISTS test_db")

    spark.sql("""
    CREATE TABLE IF NOT EXISTS test_db.crops_table (
        id INT,
        lat DOUBLE,
        lon DOUBLE,
        crop STRING,
        N DOUBLE,
        P DOUBLE,
        K DOUBLE,
        pH DOUBLE,
        rainfall DOUBLE,
        temperature DOUBLE,
        humidity DOUBLE,
        price DOUBLE,
        pests ARRAY<STRUCT<name:STRING, description:STRING>>,
        diseases ARRAY<STRUCT<name:STRING, description:STRING>>        
        ) 
        STORED AS PARQUET
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS test_db.aqi_table (
        id INT,
        lat DOUBLE,
        lon DOUBLE,
        humidity DOUBLE,
        wind_speed DOUBLE,
        wind_direction DOUBLE,
        dew_point DOUBLE,
        temperature DOUBLE,
        clouds_all DOUBLE,
        visibility_in_miles DOUBLE,
        rain_p_h DOUBLE,
        snow_p_h DOUBLE,
        traffic_volume DOUBLE,
        aqi DOUBLE,
        ) 
        STORED AS PARQUET
    """)

    spark.sql("""
    CREATE TABLE IF NOT EXISTS test_db.solar_table (           
        id INT,
        lat DOUBLE,
        lon DOUBLE,
        power DOUBLE,
        temperature_2_m_above_gnd DOUBLE,
        relative_humidity_2_m_above_gnd DOUBLE,
        dewpoint_2m DOUBLE,
        mean_sea_level_pressure_MSL DOUBLE,
        total_precipitation_sfc DOUBLE,
        snowfall_amount_sfc DOUBLE,
        total_cloud_cover_sfc DOUBLE,
        high_cloud_cover_high_cld_lay DOUBLE,
        medium_cloud_cover_mid_cld_lay DOUBLE,
        low_cloud_cover_low_cld_lay DOUBLE,
        shortwave_radiation_backwards_sfc DOUBLE,
        wind_speed_10_m_above_gnd DOUBLE,
        wind_direction_10_m_above_gnd DOUBLE,
        wind_speed_80_m_above_gnd DOUBLE,
        wind_direction_80_m_above_gnd DOUBLE,
        wind_speed_900_mb DOUBLE,
        wind_direction_900_mb DOUBLE,
        wind_gust_10_m_above_gnd DOUBLE,
        angle_of_incidence DOUBLE,
        zenith DOUBLE,
        azimuth DOUBLE
        ) 
        STORED AS PARQUET
    """)
    
    spark.sql("""
    CREATE TABLE IF NOT EXISTS test_db.wind_table (
        id INT,
        lat DOUBLE,
        lon DOUBLE,
        power DOUBLE,
        temperature_2_m_above_gnd DOUBLE,
        relative_humidity_2_m_above_gnd DOUBLE,
        dewpoint_2m DOUBLE,
        wind_speed_10_m_above_gnd DOUBLE,
        windspeed_100m DOUBLE,
        wind_direction_10_m_above_gnd DOUBLE,
        winddirection_100m DOUBLE,
        wind_gust_10_m_above_gnd DOUBLE,
        timestamp STRING
        ) 
        STORED AS PARQUET          
    """)

    spark.sql("SHOW TABLES IN test_db").show()
    
def insert_into_crops(data: CropSchema):
    df = spark.createDataFrame([data.dict()])
    insert = df.write.mode("append").saveAsTable("test_db.crops_table")
    if insert:
        return True
    return False

def insert_into_aqi(data: AQISchema):
    df = spark.createDataFrame([data.dict()])
    insert = df.write.mode("append").saveAsTable("test_db.aqi_table")
    if insert:
        return True
    return False

def insert_into_solar(data: SolarSchema):
    df = spark.createDataFrame([data.dict()])
    insert = df.write.mode("append").saveAsTable("test_db.solar_table")
    if insert:
        return True
    return False

def insert_into_wind(data: WindSchema):
    df = spark.createDataFrame([data.dict()])
    insert = df.write.mode("append").saveAsTable("test_db.wind_table")
    if insert:
        return True
    return False

def read_from_crops():
    df = spark.sql("SELECT * FROM test_db.crops_table")
    return df

def read_from_aqi():
    df = spark.sql("SELECT * FROM test_db.aqi_table")
    return df

def read_from_solar():
    df = spark.sql("SELECT * FROM test_db.solar_table")
    return df

def read_from_wind():
    df = spark.sql("SELECT * FROM test_db.wind_table")
    return df

def close_spark():
    spark.stop()
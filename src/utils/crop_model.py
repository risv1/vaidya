import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import json

df = pd.read_csv('src/data/indiancrop_dataset.csv')

class CropRecommendationModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_crops):
        super(CropRecommendationModel, self).__init__()
        
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, num_crops)
        )
        
    def forward(self, x):
        return self.network(x)

class CropRecommender:
    def __init__(self, hidden_size=128):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.feature_names = ['LATITUDE', 'LONGITUDE', 'TEMPERATURE', 'HUMIDITY', 'RAINFALL']
        self.target_features = ['N_SOIL', 'P_SOIL', 'K_SOIL', 'ph', 'CROP_PRICE']
        self.crop_stats = {}

        input_size = len(self.feature_names)
        num_crops = 22
        self.model = CropRecommendationModel(input_size, hidden_size, num_crops).to(self.device)

    def load_crop_stats(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.crop_stats = json.load(f)
                print(f"Loaded crop stats: {self.crop_stats}") 
        except FileNotFoundError:
            print(f"Error: {filepath} not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from {filepath}.")


    def get_crop_parameters(self, crop_name):
        print(f"Looking for crop: {crop_name} in crop_stats.")
        print(f"Available crops in stats: {self.crop_stats.keys()}")

        if crop_name in self.crop_stats:
            return (self.crop_stats[crop_name]['avg_params'], 
                    self.crop_stats[crop_name]['avg_price'])
    
        print(f"Crop '{crop_name}' not found in crop_stats.")
        return None, None

    def predict(self, latitude, longitude, temperature, humidity, rainfall):
        if self.model is None:
            raise Exception("Model needs to be trained first!")
            
        input_data = np.array([[latitude, longitude, temperature, humidity, rainfall]])
        input_scaled = self.scaler.transform(input_data)
        input_tensor = torch.FloatTensor(input_scaled).to(self.device)
        print("Input Tensor:", input_tensor)
        
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.softmax(outputs, dim=1)
            print("Probabilities:", probabilities)
            
        top_probs, top_indices = torch.topk(probabilities, k=3)
        recommendations = []
        print("Top Indices:", top_indices)
        
        for idx, prob in zip(top_indices[0], top_probs[0]):
            crop_name = self.label_encoder.inverse_transform([idx.item()])[0]
            print(f"Predicted Crop: {crop_name}")
                
            avg_params, avg_price = self.get_crop_parameters(crop_name)
            print(f"Avg. Parameters: {avg_params}, Avg. Price: {avg_price}")
            
            if avg_params is not None:
                recommendations.append({
                    'crop': crop_name,
                    'confidence': prob.item() * 100,
                    'soil_requirements': {
                        'N': round(float(avg_params[0]), 2),
                        'P': round(float(avg_params[1]), 2),
                        'K': round(float(avg_params[2]), 2),
                        'pH': round(float(avg_params[3]), 2)
                    },
                    'estimated_price': round(float(avg_price), 2)
                })
            
        return recommendations

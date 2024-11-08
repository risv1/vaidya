import json
import torch 
from utils.crop_model import CropRecommendationModel, CropRecommender
from utils.gem import gen_pests_and_diseases
import joblib

def load_model():
    recommender = CropRecommender()
    
    recommender.model.load_state_dict(torch.load('crop_recommender.pt'))
    recommender.model.eval()

    recommender.scaler = joblib.load('scaler.pkl')
    recommender.label_encoder = joblib.load('label_encoder.pkl')
    
    return recommender

def predict_crop_yield(lat: str, lon: str, temp: float, humidity: float, rainfall: float):
    recommender = load_model()
    
    if recommender.model and recommender.scaler and recommender.label_encoder:
        print("Model, scaler, and label encoder loaded successfully.")

    recommender.load_crop_stats('crop_stats.txt')

    recommendations = recommender.predict(
        latitude=lat,
        longitude=lon,
        temperature=temp,
        humidity=humidity,
        rainfall=rainfall
    )
    
    if not recommendations:
        print("No recommendations returned. Check model and input data.")
        return
    
    print("\nCrop Recommendations:")
    crops_rec = []
    for i, rec in enumerate(recommendations, 1):
        new_crop = {
            'crop': rec['crop'],
            'confidence': rec['confidence'],
            'soil_requirements': rec['soil_requirements'],
            'estimated_price': rec['estimated_price'] / 50,
        }
        crops_rec.append(new_crop)

    print("\nCrop Recommendations Predicted:", crops_rec)
    
    enhanced_data = gen_pests_and_diseases(json.dumps(crops_rec))
    
    try:
        if isinstance(enhanced_data, str):
            parsed_data = json.loads(enhanced_data)
        else:
            parsed_data = enhanced_data
        return parsed_data 
            
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in enhanced data"}
    except Exception as e:
        return {"error": f"Processing error: {str(e)}"}

def predict_crop_yield_spark(lat: str, lon: str, temp: float, humidity: float, rainfall: float, recommender):
    
    recommendations = recommender.predict(
        latitude=float(lat),
        longitude=float(lon),
        temperature=temp,
        humidity=humidity,
        rainfall=rainfall
    )
    
    if not recommendations:
        print("No recommendations returned. Check model and input data.")
        return
    
    print("\nCrop Recommendations:")
    crops_rec = []
    for i, rec in enumerate(recommendations, 1):
        new_crop = {
            'crop': rec['crop'],
            'confidence': rec['confidence'],
            'soil_requirements': rec['soil_requirements'],
            'estimated_price': float(rec['estimated_price']) / 50,
        }
        crops_rec.append(new_crop)

    print("\nCrop Recommendations Predicted:", crops_rec)
    
    enhanced_data = gen_pests_and_diseases(json.dumps(crops_rec))
    
    try:
        if isinstance(enhanced_data, str):
            parsed_data = json.loads(enhanced_data)
        else:
            parsed_data = enhanced_data
        return parsed_data 
            
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in enhanced data"}
    except Exception as e:
        return {"error": f"Processing error: {str(e)}"}
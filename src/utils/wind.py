import datetime
import pickle
from typing import Optional
from fastapi import HTTPException
import pandas as pd
from pydantic import BaseModel

model_data = None

def load_model():
    global model_data
    if model_data is None:
        try:
            with open('random_forest_model_1.pkl', 'rb') as file:
                model_data = pickle.load(file)
            return model_data
        except FileNotFoundError:
            raise Exception("Model file 'random_forest_model_1.pkl' not found!")
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    return model_data

class WeatherData(BaseModel):
    temperature_2_m_above_gnd: float
    relative_humidity_2_m_above_gnd: float
    dewpoint_2m: float
    wind_speed_10_m_above_gnd: float
    windspeed_100m: float
    wind_direction_10_m_above_gnd: float
    winddirection_100m: float
    wind_gust_10_m_above_gnd: float
    timestamp: Optional[str] = None

async def predict_power_wind(data: WeatherData):
    try:
        model_dict = load_model()
        model = model_dict['model']
        scaler = model_dict['scaler']

        if data.timestamp:
            dt = pd.to_datetime(data.timestamp)
        else:
            dt = datetime.datetime.now()
            
        hour = dt.hour
        day = dt.day
        month = dt.month
        year = dt.year

        features = pd.DataFrame([[
            data.dewpoint_2m,                      
            data.winddirection_100m,               
            data.windspeed_100m,                   
            hour,                                  
            day,                                   
            month,                                 
            year,                                  
            data.temperature_2_m_above_gnd,        
            data.relative_humidity_2_m_above_gnd,  
            data.wind_speed_10_m_above_gnd,      
            data.wind_direction_10_m_above_gnd,  
            data.wind_gust_10_m_above_gnd        
        ]], columns=[
            'dewpoint_2m',
            'winddirection_100m',
            'windspeed_100m',
            'hour',
            'day', 
            'month',
            'year',
            'temperature_2_m_above_gnd',
            'relative_humidity_2_m_above_gnd',
            'wind_speed_10_m_above_gnd',
            'wind_direction_10_m_above_gnd',
            'wind_gust_10_m_above_gnd'
        ])

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]

        return {
            "predicted_power": float(prediction),
            "timestamp": data.timestamp or dt.isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import asyncio
    
    data = WeatherData(
        temperature_2m=10.0,
        relativehumidity_2m=50.0,
        dewpoint_2m=5.0,
        windspeed_10m=10.0,
        windspeed_100m=20.0,
        winddirection_10m=180.0,
        winddirection_100m=180.0,
        windgusts_10m=15.0
    )
    
    async def main():
        try:
            result = await predict_power_wind(data)
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())
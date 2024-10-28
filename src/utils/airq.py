import pickle
from pydantic import BaseModel

model = None

def load_model():
    global model
    if model is None:
        try:
            with open('air_pollution.pkl', 'rb') as file:
                model = pickle.load(file)
            return model
        except FileNotFoundError:
            raise Exception("Model file 'air_pollution.pkl' not found!")
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    return model

class IncomingData(BaseModel):
    humidity: float
    wind_speed: float
    wind_direction: float
    dew_point: float
    temperature: float
    clouds_all: float
    

class AQI(BaseModel):
    humidity: float
    wind_speed: float
    wind_direction: float
    visibility_in_miles: float
    dew_point: float
    temperature: float
    rain_p_h: float
    snow_p_h: float
    clouds_all: float
    traffic_volume: float
    
def generate_required_fields(data: IncomingData) -> AQI:
    humidity_factor = 1 - (data.humidity / 100) 
    temp_dew_diff = abs(data.temperature - data.dew_point)
    base_visibility = 10 
    calculated_visibility = base_visibility * humidity_factor * (1 - (temp_dew_diff / 100))
    visibility = max(min(calculated_visibility, 10), 0.1)
    
    return AQI(
        humidity=data.humidity,
        wind_speed=data.wind_speed,
        wind_direction=data.wind_direction,
        dew_point=data.dew_point,
        temperature=data.temperature,
        clouds_all=data.clouds_all,
        visibility_in_miles=visibility,
        rain_p_h=0.0,  
        snow_p_h=0.0,  
        traffic_volume=1000.0
    )
    
    
def predict_aqi(data: IncomingData):
    try:
        ml_model = load_model()
        required_fields = generate_required_fields(data)
        
        data_dict = required_fields.dict()
        features = [
            data_dict['humidity'],
            data_dict['wind_speed'],
            data_dict['wind_direction'],
            data_dict['visibility_in_miles'],
            data_dict['dew_point'],
            data_dict['temperature'],
            data_dict['rain_p_h'],
            data_dict['snow_p_h'],
            data_dict['clouds_all'],
            data_dict['traffic_volume']
        ]
        
        return ml_model.predict([features])[0]
    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")
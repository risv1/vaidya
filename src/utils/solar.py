from fastapi import HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

class SolarPowerInput(BaseModel):
    temperature_2_m_above_gnd: float
    relative_humidity_2_m_above_gnd: float
    mean_sea_level_pressure_MSL: float
    total_precipitation_sfc: float
    snowfall_amount_sfc: float
    total_cloud_cover_sfc: float
    high_cloud_cover_high_cld_lay: float
    medium_cloud_cover_mid_cld_lay: float
    low_cloud_cover_low_cld_lay: float
    shortwave_radiation_backwards_sfc: float
    wind_speed_10_m_above_gnd: float
    wind_direction_10_m_above_gnd: float
    wind_speed_80_m_above_gnd: float
    wind_direction_80_m_above_gnd: float
    wind_speed_900_mb: float
    wind_direction_900_mb: float
    wind_gust_10_m_above_gnd: float
    angle_of_incidence: float
    zenith: float
    azimuth: float


async def predict_power_solar(data: SolarPowerInput):
    try:
        with open('solar_power_model.pkl', 'rb') as f:
            model_data = pickle.load(f)
            model = model_data['model']
            scaler = model_data['scaler']
            feature_names = model_data['feature_names']
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")
    
    try:
        input_data = pd.DataFrame([[
            data.temperature_2_m_above_gnd,
            data.relative_humidity_2_m_above_gnd,
            data.mean_sea_level_pressure_MSL,
            data.total_precipitation_sfc,
            data.snowfall_amount_sfc,
            data.total_cloud_cover_sfc,
            data.high_cloud_cover_high_cld_lay,
            data.medium_cloud_cover_mid_cld_lay,
            data.low_cloud_cover_low_cld_lay,
            data.shortwave_radiation_backwards_sfc,
            data.wind_speed_10_m_above_gnd,
            data.wind_direction_10_m_above_gnd,
            data.wind_speed_80_m_above_gnd,
            data.wind_direction_80_m_above_gnd,
            data.wind_speed_900_mb,
            data.wind_direction_900_mb,
            data.wind_gust_10_m_above_gnd,
            data.angle_of_incidence,
            data.zenith,
            data.azimuth
        ]], columns=feature_names)

        input_scaled = scaler.transform(input_data)
        
        prediction = model.predict(input_scaled)[0]

        return {
            "predicted_power_kw": float(prediction),
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import asyncio
    data = SolarPowerInput(
        temperature_2_m_above_gnd=10.0,
        relative_humidity_2_m_above_gnd=0.5,
        mean_sea_level_pressure_MSL=1013.25,
        total_precipitation_sfc=0.0,
        snowfall_amount_sfc=0.0,
        total_cloud_cover_sfc=0.0,
        high_cloud_cover_high_cld_lay=0.0,
        medium_cloud_cover_mid_cld_lay=0.0,
        low_cloud_cover_low_cld_lay=0.0,
        shortwave_radiation_backwards_sfc=0.0,
        wind_speed_10_m_above_gnd=5.0,
        wind_direction_10_m_above_gnd=180.0,
        wind_speed_80_m_above_gnd=10.0,
        wind_direction_80_m_above_gnd=180.0,
        wind_speed_900_mb=15.0,
        wind_direction_900_mb=180.0,
        wind_gust_10_m_above_gnd=10.0,
        angle_of_incidence=30.0,
        zenith=30.0,
        azimuth=180.0
    )
    
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(predict_power_solar(data))
    print(result)
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel
from starlette.requests import Request
from utils.crops import predict_crop_yield
from utils.owa import convert_kelvin_to_celsius, get_complete_weather
from utils.wind import WeatherData, predict_power_wind
from utils.solar import SolarPowerInput, predict_power_solar
from utils.airq import predict_aqi, IncomingData
import datetime

router = APIRouter()

@router.get("/health")
async def health():
    return { "status": "ok" }

@router.post("/crops_info")
async def crops(request: Request):
    try:
        body = await request.json()
        data = get_complete_weather(body['lat'], body['lon'])
        
        result = predict_crop_yield(
            body['lat'], 
            body['lon'], 
            convert_kelvin_to_celsius(data['temperature_2_m_above_gnd']), 
            data['relative_humidity_2_m_above_gnd'], 
            data['total_precipitation_sfc']
        )
        
        if isinstance(result, dict) and "error" in result:
            return result 

        return {
            "data": result
        }
        
    except Exception as e:
        return {"error": f"API error: {str(e)}"}
    
@router.post("/power")
async def power(request: Request):
    body = await request.json()
    data = get_complete_weather(body['lat'], body['lon'])
    
    try:
        solar_data = SolarPowerInput(
            temperature_2_m_above_gnd=data['temperature_2_m_above_gnd'],
            relative_humidity_2_m_above_gnd=data['relative_humidity_2_m_above_gnd'],
            mean_sea_level_pressure_MSL=data['mean_sea_level_pressure_MSL'],
            total_precipitation_sfc=data['total_precipitation_sfc'],
            snowfall_amount_sfc=data['snowfall_amount_sfc'],
            total_cloud_cover_sfc=data['total_cloud_cover_sfc'],
            high_cloud_cover_high_cld_lay=data['high_cloud_cover_high_cld_lay'],
            medium_cloud_cover_mid_cld_lay=data['medium_cloud_cover_mid_cld_lay'],
            low_cloud_cover_low_cld_lay=data['low_cloud_cover_low_cld_lay'],
            shortwave_radiation_backwards_sfc=data['shortwave_radiation_backwards_sfc'],
            wind_speed_10_m_above_gnd=data['wind_speed_10_m_above_gnd'],
            wind_direction_10_m_above_gnd=data['wind_direction_10_m_above_gnd'],
            wind_speed_80_m_above_gnd=data['wind_speed_80_m_above_gnd'],
            wind_direction_80_m_above_gnd=data['wind_direction_80_m_above_gnd'],
            wind_speed_900_mb=data['wind_speed_900_mb'],
            wind_direction_900_mb=data['wind_direction_900_mb'],
            wind_gust_10_m_above_gnd=data['wind_gust_10_m_above_gnd'],
            angle_of_incidence=data['angle_of_incidence'],
            zenith=data['zenith'],
            azimuth=data['azimuth']         
        )
        
        wind_data = WeatherData(
            temperature_2_m_above_gnd=data['temperature_2_m_above_gnd'],
            relative_humidity_2_m_above_gnd=data['relative_humidity_2_m_above_gnd'],
            dewpoint_2m=data['dewpoint_2m'],
            wind_speed_10_m_above_gnd=data['wind_speed_10_m_above_gnd'],
            windspeed_100m=data['wind_speed_80_m_above_gnd'],
            wind_direction_10_m_above_gnd=data['wind_direction_10_m_above_gnd'],
            winddirection_100m=data['wind_direction_80_m_above_gnd'],
            wind_gust_10_m_above_gnd=data['wind_gust_10_m_above_gnd'],
        )
        pred_solar = await predict_power_solar(solar_data)
        pred_wind = await predict_power_wind(wind_data)
        
        return {
            "solar": pred_solar,
            "wind": pred_wind
        }
    except Exception as e:
        return {"error": f"API error: {str(e)}"}
        

@router.post("/air_quality")
async def aqi(request: Request):
    body = await request.json()
    data = get_complete_weather(body['lat'], body['lon'])
    
    try:
        airq_data = IncomingData(
            humidity=data['relative_humidity_2_m_above_gnd'],
            wind_speed=data['wind_speed_10_m_above_gnd'],
            wind_direction=data['wind_direction_10_m_above_gnd'],
            dew_point=data['dewpoint_2m'],
            temperature=data['temperature_2_m_above_gnd'],
            clouds_all=data['total_cloud_cover_sfc']
        )
        
        pred_aqi = predict_aqi(airq_data)
    
        return {
            "aqi": pred_aqi,
            "status": "ok"
        }
        
    except Exception as e:
        return {"error": f"API error: {str(e)}"}
        
    
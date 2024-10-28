import math
import requests
import os
from datetime import datetime
from typing import Dict, Any

api_key = os.getenv('OWA_API_KEY')

def convert_kelvin_to_celsius(temp: float) -> float:
    return temp - 273.15

def calculate_dewpoint(temp_k: float, relative_humidity: float) -> float:
    temp_c = temp_k - 273.15
    b = 17.62
    c = 243.12
    
    gamma = math.log(relative_humidity / 100) + (b * temp_c) / (c + temp_c)
    dewpoint = (c * gamma) / (b - gamma)
    return dewpoint

def calculate_solar_position(lat: float, lon: float, timestamp: int) -> tuple[float, float, float]:
    dt = datetime.fromtimestamp(timestamp)
    hour = dt.hour + dt.minute/60
    day_of_year = dt.timetuple().tm_yday

    declination = 23.45 * math.sin(math.radians(360/365 * (day_of_year - 81)))
    hour_angle = 15 * (hour - 12)
    
    lat_rad = math.radians(lat)
    decl_rad = math.radians(declination)
    hour_rad = math.radians(hour_angle)
    
    zenith = math.degrees(math.acos(
        math.sin(lat_rad) * math.sin(decl_rad) + 
        math.cos(lat_rad) * math.cos(decl_rad) * math.cos(hour_rad)
    ))
    
    azimuth = math.degrees(math.atan2(
        -math.cos(decl_rad) * math.sin(hour_rad),
        math.cos(lat_rad) * math.sin(decl_rad) - 
        math.sin(lat_rad) * math.cos(decl_rad) * math.cos(hour_rad)
    ))
    azimuth = (azimuth + 360) % 360
    
    angle_of_incidence = zenith
    return zenith, azimuth, angle_of_incidence

def transform_weather_data(raw_data: Dict[str, Any]) -> Dict[str, float]:
    main = raw_data.get('main', {})
    wind = raw_data.get('wind', {})
    clouds = raw_data.get('clouds', {})
    
    lat = raw_data['coord']['lat']
    lon = raw_data['coord']['lon']
    timestamp = raw_data['dt']
    zenith, azimuth, angle_of_incidence = calculate_solar_position(lat, lon, timestamp)

    transformed_data = {
        'temperature_2_m_above_gnd': main.get('temp', 0),
        'relative_humidity_2_m_above_gnd': main.get('humidity', 0),
        'dewpoint_2m': calculate_dewpoint(main.get('temp', 0), main.get('humidity', 0)),
        'mean_sea_level_pressure_MSL': main.get('sea_level', main.get('pressure', 0)),
        'total_precipitation_sfc': raw_data.get('rain', {}).get('1h', 0) + raw_data.get('snow', {}).get('1h', 0),
        'snowfall_amount_sfc': raw_data.get('snow', {}).get('1h', 0),
        'total_cloud_cover_sfc': clouds.get('all', 0),
        'high_cloud_cover_high_cld_lay': clouds.get('all', 0) * 0.33,
        'medium_cloud_cover_mid_cld_lay': clouds.get('all', 0) * 0.33,
        'low_cloud_cover_low_cld_lay': clouds.get('all', 0) * 0.34,
        'shortwave_radiation_backwards_sfc': max(0, 1000 * (1 - clouds.get('all', 0)/100) * math.cos(math.radians(zenith))),
        'wind_speed_10_m_above_gnd': wind.get('speed', 0),
        'wind_direction_10_m_above_gnd': wind.get('deg', 0),
        'wind_speed_80_m_above_gnd': wind.get('speed', 0) * (80/10)**0.143,
        'wind_direction_80_m_above_gnd': wind.get('deg', 0) + 10,
        'wind_speed_900_mb': wind.get('speed', 0) * 1.5,
        'wind_direction_900_mb': wind.get('deg', 0) + 20,
        'wind_gust_10_m_above_gnd': wind.get('gust', wind.get('speed', 0) * 1.5),
        'angle_of_incidence': angle_of_incidence,
        'zenith': zenith,
        'azimuth': azimuth,
    }
    
    return transformed_data

def get_complete_weather(lat: str, lon: str, api_key=api_key) -> Dict[str, float]:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    raw_data = response.json()
    
    return transform_weather_data(raw_data)

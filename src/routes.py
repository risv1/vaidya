from fastapi import APIRouter
from starlette.requests import Request
from utils.crops import convert_kelvin_to_celsius, get_weather, predict_crop_yield

router = APIRouter()

@router.get("/health")
async def health():
    return { "status": "ok" }

@router.post("/crops_info")
async def crops(request: Request):
    try:
        body = await request.json()
        data = get_weather(body['lat'], body['lon'])
        
        result = predict_crop_yield(
            body['lat'], 
            body['lon'], 
            convert_kelvin_to_celsius(data['temp']), 
            data['humidity'], 
            data['rainfall']
        )
        
        if isinstance(result, dict) and "error" in result:
            return result 

        return {
            "data": result
        }
        
    except Exception as e:
        return {"error": f"API error: {str(e)}"}
    
@router.get("/power")
async def power():
    return { "status": "ok" }

@router.get("/air_quality")
async def health():
    return { "status": "ok" }
import os
import google.generativeai as genai
from typing import List

api_key = os.getenv('API_KEY')
modelv = os.getenv('MODEL')

genai.configure(api_key=api_key)

model = genai.GenerativeModel(modelv)

def gen_pests_and_diseases(temp: str, humidity: str, rainfall: str, crops: List[str]):
    prompt = os.getenv('')
    res = model.generate_content(f"""
            {prompt} 
            temperature: {temp}
            humidity: {humidity}
            rainfall: {rainfall}
            crops: {crops}
        """)
    return res



import os
import google.generativeai as genai
from typing import List

gem_api_key = os.getenv('GEMINI_API_KEY')
modelv = os.getenv('MODEL')

genai.configure(api_key=gem_api_key)

model = genai.GenerativeModel(modelv)

prompt = os.getenv('CROP_PROMPT')
def gen_pests_and_diseases(crops_rec):
    res = model.generate_content(f"{prompt} {crops_rec}")

    return res.text

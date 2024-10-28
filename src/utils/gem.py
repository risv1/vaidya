import os
import google.generativeai as genai
from typing import List

gem_api_key = os.getenv('GEMINI_API_KEY')
modelv = os.getenv('MODEL')

genai.configure(api_key=gem_api_key)

model = genai.GenerativeModel(modelv)

prompt = """
STRICT INSTRUCTIONS:
1. Return ONLY valid JSON - no explanations, no markdown, no text
2. The response must start with "[" and end with "]"
3. Keep all existing fields from the input exactly as they are
4. Add only these new fields to each crop object:
   - "pests": array of {name, description} objects
   - "diseases": array of {name, description} objects
5. Format: Exact match to this structure:
{
    "crop": <existing>,
    "confidence": <existing>,
    "soil_requirements": <existing>,
    "estimated_price": <existing>,
    "pests": [
        {
            "name": "Example Pest",
            "description": "Description here"
        }
    ],
    "diseases": [
        {
            "name": "Example Disease",
            "description": "Description here"
        }
    ]
}
Give in Array of JSON format as mentioned above, dont give any text describing whats happening
"""
def gen_pests_and_diseases(crops_rec):
    res = model.generate_content(f"{prompt} {crops_rec}")

    return res.text

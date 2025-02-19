# src/my_project/tools/custom_tool.py

import os
import requests

# It's a good practice to store your API key in your .env file.
# You can then load it using os.getenv. For now, we'll use the provided key.
API_KEY = os.getenv("STARRYAI_API_KEY", "2ebGIvkSFD1Kp2KtjpyM1eMHStfETA")
API_URL = "https://api.starryai.com/creations/"

def generate_images(
    model="lyra",
    aspect_ratio="square",
    high_resolution=False,
    images=4,
    steps=20,
    initial_image_mode="color"
):
    headers = {
        "X-API-Key": API_KEY,
        "accept": "application/json",
        "content-type": "application/json"
    }
    payload = {
        "model": model,
        "aspectRatio": aspect_ratio,
        "highResolution": high_resolution,
        "images": images,
        "steps": steps,
        "initialImageMode": initial_image_mode
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")

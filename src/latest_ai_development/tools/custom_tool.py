import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

API_KEY = "2ebGIvkSFD1Kp2KtjpyM1eMHStfETA"
API_URL = "https://api.starryai.com/creations/"

class GenerateImageInput(BaseModel):
    """Input schema for image generation."""
    prompt: str = Field(description="The text prompt to generate the image from")

class GenerateImageTool(BaseTool):
    name: str = "generate_image"
    description: str = "Generate images using the StarryAI API based on text prompts"
    args_schema: Type[BaseModel] = GenerateImageInput

    def _run(self, prompt: str) -> str:
        """Execute the image generation"""
        headers = {
            "accept": "application/json",
            "X-API-Key": API_KEY,
            "content-type": "application/json"
        }
        
        payload = {
            "model": "lyra",
            "aspectRatio": "square",
            "highResolution": False,
            "images": 1,
            "steps": 20,
            "initialImageMode": "color",
            "prompt": prompt
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return f"Image generation successful: {result}"
        except requests.RequestException as e:
            return f"Error generating image: {str(e)}"

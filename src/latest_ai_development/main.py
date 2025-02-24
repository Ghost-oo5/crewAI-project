#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_ai_model_choice():
    """Get user's AI model selection."""
    while True:
        print("\nPlease select an AI model:")
        print("1. Midjourney")
        print("2. Stable Diffusion")
        print("3. Leonardo AI")
        print("4. DALL-E")
        print("5. Adobe Firefly")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                models = {
                    1: "Midjourney",
                    2: "Stable Diffusion",
                    3: "Leonardo AI",
                    4: "DALL-E",
                    5: "Adobe Firefly"
                }
                return models[choice]
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

def get_dimensions_choice():
    """Get user's desired image dimensions."""
    while True:
        print("\nPlease select image dimensions:")
        print("1. Square (1:1) - Best for: Instagram posts, profile pictures")
        print("2. Landscape (16:9) - Best for: YouTube thumbnails, blog headers")
        print("3. Portrait (4:5) - Best for: Instagram, Pinterest")
        print("4. Wide Banner (2:1) - Best for: LinkedIn, Twitter headers")
        print("5. Custom dimensions")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                dimensions = {
                    1: {"ratio": "1:1", "pixels": "1080x1080"},
                    2: {"ratio": "16:9", "pixels": "1920x1080"},
                    3: {"ratio": "4:5", "pixels": "1080x1350"},
                    4: {"ratio": "2:1", "pixels": "1500x750"},
                    5: "custom"
                }
                
                if choice == 5:
                    width = int(input("Enter width in pixels: "))
                    height = int(input("Enter height in pixels: "))
                    return f"{width}x{height}"
                return dimensions[choice]
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter valid numbers.")

def get_image_type_choice(dimensions):
    """Get user's image type selection based on dimensions."""
    # Suggest appropriate image types based on dimensions
    ratio = dimensions["ratio"] if isinstance(dimensions, dict) else "custom"
    
    suggested_types = {
        "1:1": ["Instagram Posts", "Profile Pictures", "Social Media Cards"],
        "16:9": ["YouTube Thumbnails", "Blog Headers", "Presentation Slides"],
        "4:5": ["Instagram Stories", "Pinterest Pins", "Mobile Posters"],
        "2:1": ["LinkedIn Banners", "Twitter Headers", "Email Headers"]
    }
    
    if ratio in suggested_types:
        print(f"\nRecommended uses for {ratio} ratio:")
        for use in suggested_types[ratio]:
            print(f"- {use}")
    
    while True:
        print("\nPlease select an image type:")
        print("\n1. Digital Marketing & Social Media")
        print("   - YouTube Thumbnails")
        print("   - Social Media Posts (Instagram, Facebook, Twitter)")
        print("   - Story/Reel Covers")
        print("   - Blog Headers")
        print("   - Social Media Ads")
        
        print("\n2. Realism-Based Images")
        print("   - Photorealistic")
        print("   - Hyperrealistic")
        print("   - AI-Enhanced Realism")
        
        print("\n3. Artistic & Stylized Images")
        print("   - Illustrations")
        print("   - Concept Art")
        print("   - Cartoon & Anime")
        print("   - Pixel Art")
        print("   - Oil Painting/Watercolor/Sketch")
        
        print("\n4. Abstract & Surreal Images")
        print("   - Dreamlike / Fantasy")
        print("   - Glitch / Cyberpunk")
        print("   - Geometric / Minimalist")
        
        print("\n5. Business & Professional")
        print("   - Logos & Branding")
        print("   - UI/UX Mockups")
        print("   - Infographics")
        print("   - Product Presentations")
        print("   - Corporate Banners")
        
        try:
            main_choice = int(input("\nEnter main category (1-5): "))
            if not 1 <= main_choice <= 5:
                print("Please enter a number between 1 and 5.")
                continue
                
            subcategories = {
                1: ["YouTube Thumbnails", "Social Media Posts", "Story/Reel Covers", "Blog Headers", "Social Media Ads"],
                2: ["Photorealistic", "Hyperrealistic", "AI-Enhanced Realism"],
                3: ["Illustrations", "Concept Art", "Cartoon & Anime", "Pixel Art", "Oil Painting/Watercolor/Sketch"],
                4: ["Dreamlike / Fantasy", "Glitch / Cyberpunk", "Geometric / Minimalist"],
                5: ["Logos & Branding", "UI/UX Mockups", "Infographics", "Product Presentations", "Corporate Banners"]
            }
            
            print("\nSelect specific style:")
            for idx, style in enumerate(subcategories[main_choice], 1):
                print(f"{idx}. {style}")
                
            sub_choice = int(input(f"\nEnter style (1-{len(subcategories[main_choice])}): "))
            if 1 <= sub_choice <= len(subcategories[main_choice]):
                return subcategories[main_choice][sub_choice - 1]
            else:
                print("Invalid subcategory choice.")
        except ValueError:
            print("Please enter valid numbers.")

def format_result(result):
    """Format the result for better readability"""
    if not isinstance(result, dict):
        return str(result)
    
    formatted = "\nEnhanced Prompt Details:\n" + "="*50 + "\n\n"
    
    # Format enhanced prompt
    formatted += "📝 ENHANCED PROMPT:\n"
    formatted += "-"*30 + "\n"
    formatted += f"{result.get('enhanced_prompt', '').strip()}\n\n"
    
    # Format negative prompt if it exists
    if result.get('negative_prompt'):
        formatted += "🚫 NEGATIVE PROMPT:\n"
        formatted += "-"*30 + "\n"
        formatted += f"{result.get('negative_prompt', '').strip()}\n\n"
    
    # Format model parameters
    if result.get('model_specific_parameters'):
        formatted += "⚙️ MODEL PARAMETERS:\n"
        formatted += "-"*30 + "\n"
        formatted += f"{result.get('model_specific_parameters', '').strip()}\n\n"
    
    # Format image type and dimensions
    formatted += "📊 SPECIFICATIONS:\n"
    formatted += "-"*30 + "\n"
    formatted += f"Image Type: {result.get('image_type', '').strip()}\n"
    formatted += f"Dimensions: {result.get('dimensions', '').strip()}\n"
    
    return formatted

def run():
    """
    Run the crew.
    """
    # Display AI model information
    crew_instance = LatestAiDevelopment()
    prompt_engineer = crew_instance.prompt_engineer()
    print("\n=== AI Model Information ===")
    print(f"Using LLM: {prompt_engineer.llm}\n")

    # Get user inputs in this order:
    prompt = input("Enter your prompt: ")
    negative_prompt = input("Enter negative prompt (what you don't want in the image, optional): ")
    dimensions = get_dimensions_choice()
    selected_model = get_ai_model_choice()
    image_type = get_image_type_choice(dimensions)
    
    print(f"\nSelected Dimensions: {dimensions['pixels'] if isinstance(dimensions, dict) else dimensions}")
    print(f"Selected Model: {selected_model}")
    print(f"Selected Image Type: {image_type}")
    print("\nProcessing...\n")

    inputs = {
        "dimensions": dimensions['pixels'] if isinstance(dimensions, dict) else dimensions,
        "prompt": prompt,
        "negative_prompt": negative_prompt if negative_prompt else "None",
        "selected_model": selected_model,
        "image_type": image_type
    }

    try:
        crew = crew_instance.crew()
        crew.verbose = True
        result = crew.kickoff(inputs=inputs)
        
        # Format and display the result
        formatted_result = format_result(result)
        print(formatted_result)
        
        # Save result to report.md with better formatting
        with open('report.md', 'w') as f:
            f.write(f"# AI Prompt Generation Report\n\n")
            f.write(f"## Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## Input Parameters\n")
            f.write(f"- **Original Prompt:** {prompt}\n")
            f.write(f"- **Negative Prompt:** {negative_prompt}\n")
            f.write(f"- **Selected Model:** {selected_model}\n")
            f.write(f"- **Image Type:** {image_type}\n")
            f.write(f"- **Dimensions:** {dimensions['pixels'] if isinstance(dimensions, dict) else dimensions}\n\n")
            
            f.write("## Generated Output\n")
            f.write("```\n")
            f.write(formatted_result)
            f.write("```\n")
            
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        raise

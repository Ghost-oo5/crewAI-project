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

def get_image_type_choice():
    """Get user's image type selection."""
    while True:
        print("\nPlease select an image type:")
        print("\n1. Realism-Based Images")
        print("   - Photorealistic")
        print("   - Hyperrealistic")
        print("   - AI-Enhanced Realism")
        print("\n2. Artistic & Stylized Images")
        print("   - Illustrations")
        print("   - Concept Art")
        print("   - Cartoon & Anime")
        print("   - Pixel Art")
        print("   - Oil Painting/Watercolor/Sketch")
        print("\n3. Abstract & Surreal Images")
        print("   - Dreamlike / Fantasy")
        print("   - Glitch / Cyberpunk")
        print("   - Geometric / Minimalist")
        print("\n4. Informational & Infographics")
        print("   - Diagrams & Charts")
        print("   - Infographics")
        print("\n5. Specific-Use Cases")
        print("   - Logos & Branding")
        print("   - UI/UX Mockups")
        print("   - 3D Renders")
        print("   - AI-Generated Faces")
        
        try:
            main_choice = int(input("\nEnter main category (1-5): "))
            if not 1 <= main_choice <= 5:
                print("Please enter a number between 1 and 5.")
                continue
                
            subcategories = {
                1: ["Photorealistic", "Hyperrealistic", "AI-Enhanced Realism"],
                2: ["Illustrations", "Concept Art", "Cartoon & Anime", "Pixel Art", "Oil Painting/Watercolor/Sketch"],
                3: ["Dreamlike / Fantasy", "Glitch / Cyberpunk", "Geometric / Minimalist"],
                4: ["Diagrams & Charts", "Infographics"],
                5: ["Logos & Branding", "UI/UX Mockups", "3D Renders", "AI-Generated Faces"]
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

def run():
    """
    Run the crew.
    """
    # Display AI model information
    crew_instance = LatestAiDevelopment()
    prompt_engineer = crew_instance.prompt_engineer()
    print("\n=== AI Model Information ===")
    print(f"Using LLM: {prompt_engineer.llm}\n")

    # Get user inputs
    prompt = input("Enter your prompt: ")
    # instructions = input("Enter instructions for the prompt engineer (optional): ")
    selected_model = get_ai_model_choice()
    image_type = get_image_type_choice()
    
    print(f"\nSelected Model: {selected_model}")
    print(f"Selected Image Type: {image_type}")
    print("\nProcessing...\n")

    inputs = {
        "prompt": prompt,
        # "instructions": instructions,
        "selected_model": selected_model,
        "image_type": image_type
    }

    try:
        # Create crew with verbose output enabled
        crew = crew_instance.crew()
        crew.verbose = True  # Enable detailed output including reasoning
        result = crew.kickoff(inputs=inputs)
        print(f"\nFinal result: {result}")
        
        # Save result to report.md
        with open('report.md', 'w') as f:
            f.write(f"# Generated Result\n\n")
            f.write(f"## Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Selected Model\n{selected_model}\n\n")
            f.write(f"## Selected Image Type\n{image_type}\n\n")
            f.write(f"## Original Prompt\n{prompt}\n\n")
            # f.write(f"## Instructions\n{instructions}\n\n")
            f.write(f"## Enhanced Result\n{result}\n")
            
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        raise

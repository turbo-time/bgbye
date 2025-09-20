#!/usr/bin/env python3
"""
Example usage of the batch background remover.
This script creates some sample images and demonstrates the background removal process.
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw
import random

def create_sample_images(output_dir="sample_images", count=3):
    """Create sample images for testing the background remover."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    
    for i in range(count):
        # Create a simple image with colored shapes
        img = Image.new('RGB', (400, 400), 'white')
        draw = ImageDraw.Draw(img)
        
        # Draw some shapes
        color = random.choice(colors)
        draw.ellipse([50, 50, 350, 350], fill=color, outline='black', width=3)
        draw.rectangle([150, 150, 250, 250], fill='yellow', outline='black', width=2)
        
        filename = f"sample_{i+1}.jpg"
        img.save(output_path / filename, "JPEG")
        print(f"Created: {filename}")
    
    return output_path

def main():
    print("Batch Background Remover - Example Usage")
    print("=" * 50)
    
    # Create sample images
    print("\n1. Creating sample images...")
    sample_dir = create_sample_images()
    print(f"Sample images created in: {sample_dir}")
    
    # Show usage example
    print(f"\n2. To remove backgrounds from these images (uses CPU by default):")
    print(f"   python batch_background_remover.py {sample_dir} {sample_dir}_no_bg")
    
    print(f"\n3. With GPU acceleration (if available):")
    print(f"   python batch_background_remover.py {sample_dir} {sample_dir}_no_bg --device cuda")
    
    print(f"\n4. The processed images will be saved in: {sample_dir}_no_bg/")
    print("   - Original: sample_1.jpg → Processed: sample_1_no_bg.png")
    print("   - Original: sample_2.jpg → Processed: sample_2_no_bg.png")
    print("   - Original: sample_3.jpg → Processed: sample_3_no_bg.png")

if __name__ == "__main__":
    main()
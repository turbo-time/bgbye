#!/usr/bin/env python3
"""
Batch Background Remover using BRIA RMBG-1.4 model

This script processes all images in a given input directory and removes their backgrounds,
saving the results as PNG files in the specified output directory.

Usage:
    python batch_background_remover.py input_dir output_dir [--device cpu|cuda]

Requirements:
    - transformers
    - torch
    - PIL (Pillow)
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image
import torch
from transformers import pipeline


class BatchBackgroundRemover:
    def __init__(self, device="cpu"):
        """Initialize the background remover with BRIA model."""
        print(f"Initializing BRIA model on {device}...")
        self.device = device
        self.model = pipeline(
            "image-segmentation", 
            model="briaai/RMBG-1.4", 
            trust_remote_code=True, 
            device=device
        )
        print("Model loaded successfully!")

    def process_image(self, image_path):
        """
        Process a single image to remove background.
        
        Args:
            image_path: Path to input image
            
        Returns:
            PIL.Image: Processed image with transparent background
        """
        # Load and convert image to RGB
        image = Image.open(image_path).convert('RGB')
        
        # Process with BRIA model
        result = self.model(image, return_mask=True)
        mask = result
        
        # Ensure mask is a PIL Image
        if not isinstance(mask, Image.Image):
            mask = Image.fromarray((mask * 255).astype('uint8'))
        
        # Create transparent background image
        no_bg_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
        no_bg_image.paste(image, mask=mask)
        
        return no_bg_image

    def process_directory(self, input_dir, output_dir):
        """
        Process all images in the input directory.
        
        Args:
            input_dir: Path to directory containing input images
            output_dir: Path to directory where processed images will be saved
        """
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        
        # Validate input directory
        if not input_path.exists():
            raise ValueError(f"Input directory does not exist: {input_dir}")
        
        if not input_path.is_dir():
            raise ValueError(f"Input path is not a directory: {input_dir}")
        
        # Create output directory if it doesn't exist
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Supported image formats
        supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        
        # Find all image files
        image_files = []
        for ext in supported_formats:
            image_files.extend(list(input_path.glob(f'*{ext}')))
            image_files.extend(list(input_path.glob(f'*{ext.upper()}')))
        
        if not image_files:
            print(f"No supported image files found in {input_dir}")
            print(f"Supported formats: {', '.join(supported_formats)}")
            return
        
        print(f"Found {len(image_files)} image(s) to process")
        
        # Process each image
        for i, image_file in enumerate(image_files, 1):
            print(f"Processing {i}/{len(image_files)}: {image_file.name}")
            
            try:
                # Process the image
                processed_image = self.process_image(image_file)
                
                # Create output filename (change extension to .png to preserve transparency)
                output_filename = image_file.stem + "_no_bg.png"
                output_file = output_path / output_filename
                
                # Save the processed image
                processed_image.save(output_file, "PNG")
                print(f"  → Saved: {output_file}")
                
            except Exception as e:
                print(f"  ✗ Error processing {image_file.name}: {str(e)}")
                continue
        
        print(f"\nProcessing complete! Results saved in: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Remove backgrounds from all images in a directory using BRIA RMBG-1.4 model"
    )
    parser.add_argument(
        "input_dir", 
        help="Directory containing input images"
    )
    parser.add_argument(
        "output_dir", 
        help="Directory where processed images will be saved"
    )
    parser.add_argument(
        "--device", 
        choices=["cpu", "cuda"], 
        default="cpu",
        help="Device to run the model on. Defaults to CPU for broader compatibility (default: cpu)"
    )
    
    args = parser.parse_args()
    
    # Check if CUDA is available when requested
    if args.device == "cuda" and not torch.cuda.is_available():
        print("Warning: CUDA requested but not available. Falling back to CPU.")
        args.device = "cpu"
    
    try:
        # Initialize the background remover
        remover = BatchBackgroundRemover(device=args.device)
        
        # Process the directory
        remover.process_directory(args.input_dir, args.output_dir)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
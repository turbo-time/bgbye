# Batch Background Remover

A simple Python script to remove backgrounds from all images in a directory using the BRIA RMBG-1.4 model.

## Features

- **Batch Processing**: Process all images in a directory at once
- **High Quality**: Uses the BRIA RMBG-1.4 model for excellent background removal
- **Multiple Formats**: Supports JPG, JPEG, PNG, BMP, TIFF, and WebP formats
- **Transparent Output**: Saves results as PNG files with transparent backgrounds
- **GPU Support**: Can utilize CUDA for faster processing
- **Simple CLI**: Easy-to-use command-line interface

## Quick Setup

1. **Run the setup script:**
   ```bash
   ./setup_batch.sh
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv_batch/bin/activate
   ```

3. **Process your images (defaults to CPU):**
   ```bash
   python batch_background_remover.py input_folder output_folder
   ```

## Usage Examples

### Basic Usage (CPU - Default)
```bash
python batch_background_remover.py ./photos ./photos_no_bg
```

### With GPU Acceleration
```bash
python batch_background_remover.py ./photos ./photos_no_bg --device cuda
```

### Process specific directory
```bash
python batch_background_remover.py /path/to/images /path/to/output --device cuda
```

## Command Line Options

- `input_dir`: Directory containing images to process
- `output_dir`: Directory where processed images will be saved
- `--device`: Device to use (`cpu` or `cuda`, default: `cpu`)

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Output

- All processed images are saved as PNG files with transparent backgrounds
- Original filenames are preserved with "_no_bg" suffix
- Example: `photo.jpg` → `photo_no_bg.png`

## Manual Installation

If you prefer to install dependencies manually:

```bash
# Create virtual environment
python3 -m venv venv_batch
source venv_batch/bin/activate

# Install dependencies
pip install torch torchvision transformers Pillow
```

## System Requirements

- Python 3.7+
- 4GB+ RAM (8GB+ recommended for large images)
- CUDA-compatible GPU (optional, for acceleration)

## Troubleshooting

### CUDA Issues
If you encounter CUDA-related errors, use CPU mode:
```bash
python batch_background_remover.py input_dir output_dir --device cpu
```

### Memory Issues
For large images or limited RAM:
- Process smaller batches of images
- Use CPU mode to reduce memory usage
- Close other applications to free up memory

### Model Download
The BRIA model (~1.7GB) will be downloaded automatically on first run. Ensure you have a stable internet connection.

## Performance Notes

- **CPU Mode**: ~2-5 seconds per image (depending on image size and CPU)
- **GPU Mode**: ~0.5-2 seconds per image (depending on GPU)
- First run takes longer due to model download

## Differences from Original Web App

This batch script is a simplified version that:
- Only uses the BRIA model (most reliable for general use)
- Processes images locally without a web interface
- Is optimized for batch processing rather than interactive use
- Has minimal dependencies compared to the full web app
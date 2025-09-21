# Batch Background Remover - Standalone Package

This folder contains everything you need to run batch background removal as a standalone Python project, extracted from the BGBye repository.

## 📁 What's Included

- **`batch_background_remover.py`** - Main script for batch processing
- **`example_usage.py`** - Demo script that creates sample images
- **`setup_batch.sh`** - Setup script for dependencies
- **`requirements_batch.txt`** - Python package requirements
- **`README_batch.md`** - Detailed documentation and usage guide
- **`BATCH_SUMMARY.md`** - Complete overview and comparison with original
- **`.gitignore`** - Git ignore file (excludes venv, cache, model files)

## 🚀 Quick Start

1. **Extract this folder** to your desired location
2. **Make setup script executable:**
   ```bash
   chmod +x setup_batch.sh
   ```
3. **Run setup:**
   ```bash
   ./setup_batch.sh
   ```
4. **Activate environment:**
   ```bash
   source venv_batch/bin/activate
   ```
5. **Process images (CPU - default):**
   ```bash
   python batch_background_remover.py input_folder output_folder
   ```

6. **Optional - Install globally:**
   ```bash
   ./install.sh
   # Then use: bgremove input_folder output_folder
   ```

## 📖 Documentation

- See `README_batch.md` for comprehensive documentation
- See `BATCH_SUMMARY.md` for technical details and comparisons
- Run `python example_usage.py` to create sample images for testing

## 🎯 Key Features

✅ **Standalone** - No dependencies on original BGBye repository  
✅ **Minimal Setup** - Only 4 Python packages required  
✅ **Batch Processing** - Process entire directories  
✅ **High Quality** - Uses BRIA RMBG-1.4 model  
✅ **CPU Optimized** - Defaults to CPU, optional CUDA acceleration  
✅ **Multiple Formats** - JPG, PNG, BMP, TIFF, WebP  

## 🔧 Requirements

- Python 3.7+
- 4GB+ RAM (8GB+ recommended)
- Optional: CUDA-compatible GPU for acceleration

This package is completely self-contained and ready to use in any project!
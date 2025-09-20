#!/bin/bash

# Setup script for batch background removal
# This installs only the minimal dependencies needed for batch processing

echo "Setting up batch background remover..."

# Create a virtual environment if it doesn't exist
if [ ! -d "venv_batch" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv_batch
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv_batch/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements_batch.txt

echo "Setup complete!"
echo ""
echo "To use the batch background remover:"
echo "1. Activate the virtual environment: source venv_batch/bin/activate"
echo "2. Run the script: python batch_background_remover.py input_dir output_dir"
echo ""
echo "Example: python batch_background_remover.py ./photos ./photos_no_bg"
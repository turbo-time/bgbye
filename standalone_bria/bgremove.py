#!/usr/bin/env python3
"""
Entry point script for Batch Background Remover
This creates a proper Python package entry point
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Paths to virtual environment and main script
    venv_path = script_dir / "venv_batch"
    python_script = script_dir / "batch_background_remover.py"
    
    # Check if virtual environment exists
    if not venv_path.exists():
        print(f"Error: Virtual environment not found at {venv_path}")
        print("Please run setup_batch.sh first from the script directory.")
        sys.exit(1)
    
    # Check if Python script exists
    if not python_script.exists():
        print(f"Error: Python script not found at {python_script}")
        sys.exit(1)
    
    # Path to Python executable in virtual environment
    python_exe = venv_path / "bin" / "python"
    
    # Run the script with all arguments passed through
    try:
        result = subprocess.run([str(python_exe), str(python_script)] + sys.argv[1:])
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error running background remover: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
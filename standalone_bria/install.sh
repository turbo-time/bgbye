#!/bin/bash

# Installation script for Batch Background Remover

echo "Installing Batch Background Remover..."

# Get current directory (where the script files are)
INSTALL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
WRAPPER_SCRIPT="$INSTALL_DIR/bgremove"

# Check if wrapper script exists
if [ ! -f "$WRAPPER_SCRIPT" ]; then
    echo "Error: Wrapper script 'bgremove' not found in current directory"
    exit 1
fi

# Method 1: Install to /usr/local/bin (system-wide, requires sudo)
echo "Choose installation method:"
echo "1) System-wide installation (/usr/local/bin) - requires sudo"
echo "2) User installation (~/.local/bin) - no sudo required"
echo "3) Add to PATH via .bashrc - no copying required"
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "Installing to /usr/local/bin (requires sudo)..."
        sudo cp "$WRAPPER_SCRIPT" /usr/local/bin/bgremove
        if [ $? -eq 0 ]; then
            echo "✅ Successfully installed! You can now use 'bgremove' from anywhere."
            echo "Usage: bgremove input_folder output_folder"
        else
            echo "❌ Installation failed"
            exit 1
        fi
        ;;
    2)
        echo "Installing to ~/.local/bin..."
        mkdir -p ~/.local/bin
        cp "$WRAPPER_SCRIPT" ~/.local/bin/bgremove
        
        # Check if ~/.local/bin is in PATH
        if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
            echo "Adding ~/.local/bin to PATH..."
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
            echo "⚠️  Please restart your terminal or run: source ~/.bashrc"
        fi
        
        echo "✅ Successfully installed! You can now use 'bgremove' from anywhere."
        echo "Usage: bgremove input_folder output_folder"
        ;;
    3)
        echo "Adding current directory to PATH via .bashrc..."
        echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.bashrc
        echo "✅ Successfully added to PATH!"
        echo "⚠️  Please restart your terminal or run: source ~/.bashrc"
        echo "Usage: bgremove input_folder output_folder"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "Test the installation with:"
echo "bgremove --help"
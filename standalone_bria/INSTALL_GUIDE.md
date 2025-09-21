# Installing Batch Background Remover System-Wide

This guide shows you how to install the batch background remover so you can use it from anywhere in your Linux system.

## Quick Install

1. **Run the automatic installer:**
   ```bash
   cd /path/to/standalone_bria
   ./install.sh
   ```

2. **Choose your preferred installation method:**
   - **Option 1**: System-wide (requires sudo) - installs to `/usr/local/bin`
   - **Option 2**: User-only (no sudo) - installs to `~/.local/bin`
   - **Option 3**: Add to PATH - no copying, just adds current directory to PATH

3. **Test the installation:**
   ```bash
   bgremove --help
   ```

## Manual Installation Methods

### Method 1: System-Wide Installation (Recommended)

```bash
# Copy the wrapper script to system bin directory
sudo cp bgremove /usr/local/bin/bgremove

# Make it executable (should already be)
sudo chmod +x /usr/local/bin/bgremove

# Test it
bgremove --help
```

**Pros:** Available to all users, standard location
**Cons:** Requires sudo access

### Method 2: User Installation

```bash
# Create user bin directory if it doesn't exist
mkdir -p ~/.local/bin

# Copy the wrapper script
cp bgremove ~/.local/bin/bgremove

# Add to PATH if not already there
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Reload bashrc
source ~/.bashrc

# Test it
bgremove --help
```

**Pros:** No sudo required, user-specific
**Cons:** Only available to current user

### Method 3: Add to PATH

```bash
# Add current directory to PATH
echo 'export PATH="/full/path/to/standalone_bria:$PATH"' >> ~/.bashrc

# Reload bashrc
source ~/.bashrc

# Test it
bgremove --help
```

**Pros:** No copying required, easy to update
**Cons:** Requires full path, directory must not be moved

### Method 4: Create an Alias

```bash
# Add alias to your bashrc
echo 'alias bgremove="/full/path/to/standalone_bria/bgremove"' >> ~/.bashrc

# Reload bashrc
source ~/.bashrc

# Test it
bgremove --help
```

## Usage After Installation

Once installed, you can use the background remover from anywhere:

```bash
# Basic usage
bgremove /path/to/input/images /path/to/output/images

# With GPU (if available)
bgremove /path/to/input/images /path/to/output/images --device cuda

# Example
bgremove ~/Pictures/photos ~/Pictures/photos_no_bg
```

## What the Wrapper Script Does

The `bgremove` wrapper script:

1. ✅ **Finds the installation directory** automatically
2. ✅ **Activates the virtual environment** (`venv_batch`)
3. ✅ **Runs the Python script** with all your arguments
4. ✅ **Handles errors** gracefully
5. ✅ **Works from any directory** you call it from

## Troubleshooting

### "Command not found"
- Make sure the installation directory is in your `$PATH`
- Run `echo $PATH` to check
- Restart your terminal or run `source ~/.bashrc`

### "Virtual environment not found"
- The wrapper script needs to be in the same directory as `venv_batch/`
- Don't move files individually; move the entire `standalone_bria` folder

### "Permission denied"
- Make sure the script is executable: `chmod +x bgremove`
- For system-wide install, you might need `sudo`

## Alternative: Python Entry Point

You can also use the Python entry point directly:

```bash
# Copy the Python entry point
sudo cp bgremove.py /usr/local/bin/bgremove-py
sudo chmod +x /usr/local/bin/bgremove-py

# Use it
bgremove-py --help
```

## Uninstallation

To remove the background remover:

```bash
# If installed system-wide
sudo rm /usr/local/bin/bgremove

# If installed to user directory
rm ~/.local/bin/bgremove

# If added to PATH, edit ~/.bashrc and remove the export line
```

That's it! You now have a globally accessible `bgremove` command! 🎉


https://github.com/user-attachments/assets/6e5b6eec-9a0e-4c8c-be69-53cf709d8a99

## Configure

- pip install pillow
- set paths to images
```Python
image_paths = [
    "/full/path/to/layer0.png",
    "/full/path/to/layer1.png",
    "/full/path/to/layer2.png"
]
```
- map to keyboard shorcut

## Creating a Keyboard Shortcut in XFCE On Kali
1. Open XFCE Keyboard Settings
Go to Settings → Keyboard → Application Shortcuts.
2. Add a New Shortcut
- Click the Add button.
- Enter the command to run the script. Use the absolute path, for example:
```bash
/full/path/to/keymap.py
```
- Press OK
3. Assign a Key Combination
- After clicking OK, you'll be prompted to press the desired key combination (e.g., Super+K).
- Press the keys you want to use as the shortcut.
4. Test

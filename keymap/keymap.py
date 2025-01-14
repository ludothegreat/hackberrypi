#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk

# Change these to your actual image paths
image_paths = [
    "layer0.png",
    "layer1.png",
    "layer2.png"
]

# Custom names for each layer (displayed in the text label)
layer_names = ["Layer 0", "Layer 1", "Layer 2"]

images_cache = []
current_index = 0
MAX_SIZE = 720  # Hackberry -Pi_Zero window is 720x720

def resize_to_fit(img, max_size=MAX_SIZE):
    """
    Resize 'img' so the largest dimension is 'max_size', preserving aspect ratio.
    """
    w, h = img.size
    scale = min(max_size / w, max_size / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    return img.resize((new_w, new_h), Image.LANCZOS)

def show_image(index):
    """
    Switch the image label to show the cached image at position 'index'
    and update the text label to indicate which layer we're on.
    """
    global current_index
    current_index = index % len(images_cache)
    image_label.config(image=images_cache[current_index])
    image_label.image = images_cache[current_index]  # keep reference
    layer_label.config(text=layer_names[current_index])

def next_image(event=None):
    show_image(current_index + 1)

def prev_image(event=None):
    show_image(current_index - 1)

def select_layer0(event=None):
    show_image(0)

def select_layer1(event=None):
    show_image(1)

def select_layer2(event=None):
    show_image(2)

def main():
    global image_label, layer_label

    root = tk.Tk()
    root.title("Hackberry Layouts")
    root.geometry("720x720")
    
    # Create a container frame to hold the image (covers full window)
    container = tk.Frame(root, width=720, height=720)
    container.place(x=0, y=0)

    # Pre-load each image, resizing while preserving the aspect ratio
    for path in image_paths:
        img = Image.open(path)
        resized = resize_to_fit(img, MAX_SIZE)
        images_cache.append(ImageTk.PhotoImage(resized))

    # Create the image label and center it in the container
    image_label = tk.Label(container, bg="black")
    image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create the layer label and place it at the desired position
    layer_label = tk.Label(root, text="", font=("Arial", 16))
    layer_label.place(x=10, y=140)

    # Create a close button at the top right corner
    close_button = tk.Button(root, text="X", font=("Arial", 12),
                             width=2, command=root.destroy)
    close_button.place(x=680, y=1)

    # Create a layer to show controls
    controls_label = tk.Label(root, text="<- User Arrow Keys ->", font=("Arial", 12),)
    controls_label.place(x=270, y=145)

    # Creat layer for close shortcut "Esc"
    close_shortcut_label = tk.Label(root, text="'Esc' = Close", font=("Arial", 12),)
    close_shortcut_label.place(x=615, y=145)

    # Show the first layer by default
    show_image(0)

    # Key bindings:
    root.bind("<Left>",  prev_image)
    root.bind("<Right>", next_image)
    root.bind("1", select_layer0)
    root.bind("2", select_layer1)
    root.bind("3", select_layer2)
    root.bind("<Escape>", lambda event: root.destroy())  # Esc key binding

    root.mainloop()

if __name__ == "__main__":
    main()

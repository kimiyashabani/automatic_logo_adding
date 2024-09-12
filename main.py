from PIL import Image
import os
from tkinter import filedialog, Tk, Button
def add_logo(img_path, logo_path, output_path):
    try:
        base_img = Image.open(img_path)
        logo = Image.open(logo_path)

        base_width, base_height = base_img.size
        logo_width, logo_height = logo.size

        base_img.paste(logo, (base_width - logo_width - 200, base_height - logo_height - 100))

        base_img.save(output_path)
    except Exception as e:
        print(f"Error processing the image: {e}")
def apply_logo():
    image_paths = filedialog.askopenfilenames(title="Select Photos", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not image_paths:
        print("No images selected.")
        return

        # Select the logo file
    logo_path = filedialog.askopenfilename(title="Select Logo", filetypes=[("Image Files", "*.png;*.jpg")])

    if not logo_path:
        print("No logo selected.")
        return
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        print("No output directory selected.")
        return

    for image_path in image_paths:
        output_filename = os.path.join(output_dir, os.path.basename(image_path))
        add_logo(image_path, logo_path, output_filename)


root = Tk()
root.title('Add Logo')
root.geometry('400x400')
btn = Button(root, text='Select your photo', command=apply_logo)
btn.pack(padx=50, pady=50)

root.mainloop()
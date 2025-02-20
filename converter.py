from PIL import Image

def convert_images_to_pdf(image_paths, output_path):
    images = [Image.open(img).convert("RGB") for img in image_paths]
    images[0].save(output_path, save_all=True, append_images=images[1:])
    print(f"تم حفظ الملف: {output_path}")

import sys
from PIL import Image

def fix_size(image_path, desired_height=512, desired_width=512):
    image = Image.open(image_path)
    image_width, image_height = image.size

    aspect_ratio = image_width / image_height
    desired_ratio = desired_width / desired_height

    width = max(desired_width, image_width)
    height = width // desired_ratio
    
    if height < image_height:
        height = image_height
        width = int(height * desired_ratio)

    background_image = Image.new("RGB", (width, height), "black")
    background_image.paste(image, ((width - image_width) // 2, (height - image_height) // 2))
    return background_image.resize((desired_width, desired_height))

if __name__ == '__main__':
    final_image = fix_size(sys.argv[1])
    final_image.save('temp.jpeg')
    final_image.show()
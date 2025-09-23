import sys
from PIL import Image
import requests
from io import BytesIO
import os

TARGET_WIDTH = 950
TARGET_HEIGHT = 300

def resize_and_crop(url, output="async-agentic-header.jpg"):
    # Download
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Target size for blog headers
    target_size = (TARGET_WIDTH, TARGET_HEIGHT)
    target_ratio = target_size[0] / target_size[1]
    img_ratio = img.width / img.height

    # Center crop to match aspect ratio
    if img_ratio > target_ratio:
        # Image too wide -> crop sides
        new_width = int(img.height * target_ratio)
        left = (img.width - new_width) // 2
        img = img.crop((left, 0, left + new_width, img.height))
    else:
        # Image too tall -> crop top/bottom
        new_height = int(img.width / target_ratio)
        top = (img.height - new_height) // 2
        img = img.crop((0, top, img.width, top + new_height))

    # Resize to target
    img = img.resize(target_size, Image.LANCZOS)

    # Save
    img.save(output, "JPEG")
    print(f"✅ Saved {output}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python resize.py <image_url> <output_filename>")
        sys.exit(1)

    url = sys.argv[1]
    output = sys.argv[2]

    resize_and_crop(url, output)

# written by chatgpt
# 🖌️ Pencil Sketch Converter

This Python script converts an image into a pencil sketch using OpenCV. It supports downloading images from a URL and processing them into sketch format.

## ✨ Features
- 🖼️ Converts images into pencil sketches.
- 🌐 Supports loading images from URLs.
- 💾 Saves and displays the final output.

## 📦 Requirements
Make sure you have the required dependencies installed:
```bash
pip install opencv-python numpy requests
```

## 🚀 Usage
1. 🔗 Update the `image_url` variable with the image link you want to convert.
2. ▶️ Run the script using:
```bash
python pencil_sketch.py
```
3. 🖍️ The output sketch will be saved as `pencil_sketch.jpg` and displayed on the screen.

## 📝 Code
```python
import cv2
import numpy as np
import requests
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = cv2.imdecode(np.frombuffer(image_data.read(), np.uint8), cv2.IMREAD_COLOR)
        return image
    else:
        raise Exception("Failed to download image")

def pencil_sketch(image, output_path):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray = 255 - gray
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    cv2.imwrite(output_path, sketch)
    print(f"Pencil sketch saved at {output_path}")
    cv2.imshow("Pencil Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_url = "https://media.collegedekho.com/media/img/institute/logo/Screenshot_from_2024-06-21_11-56-54.png" #replace with your image url
output_image = "pencil_sketch.jpg"

try:
    image = download_image(image_url)
    pencil_sketch(image, output_image)
except Exception as e:
    print(f"Error: {e}")
```

## 🎨 Example Output
The generated pencil sketch will be saved as `pencil_sketch.jpg`.

## 📜 License
This project is open-source and free to use.

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
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_gray = 255 - gray
    
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blur = 255 - blurred
    
    # Create the pencil sketch
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    
    # Save the output
    cv2.imwrite(output_path, sketch)
    print(f"Pencil sketch saved at {output_path}")
    
    # Display the image
    cv2.imshow("Pencil Sketch", sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_url = "https://media.collegedekho.com/media/img/institute/logo/Screenshot_from_2024-06-21_11-56-54.png"
output_image = "pencil_sketch.jpg"

try:
    image = download_image(image_url)
    pencil_sketch(image, output_image)
except Exception as e:
    print(f"Error: {e}")

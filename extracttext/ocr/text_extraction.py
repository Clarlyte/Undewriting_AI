import pytesseract
from preprocessing import preprocess_image

# Set tesseract exe location
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_text(image_path):
    # Preprocess the image 
    preprocessed_img = preprocess_image(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(preprocessed_img)
    return text

import cv2

def adaptive_rescale_image(image, target_size=(800, 600)):
    # Get the current size of the image
    current_height, current_width = image.shape[:2]

    # Calculate the aspect ratio of the image
    aspect_ratio = current_width / current_height

    # Calculate the target width and height based on the aspect ratio
    target_width, target_height = target_size
    if aspect_ratio > 1:  # Landscape orientation
        new_width = target_width
        new_height = int(new_width / aspect_ratio)
    else:  # Portrait or square orientation
        new_height = target_height
        new_width = int(new_height * aspect_ratio)

    # Resize the image using bilinear interpolation
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    return resized_image

def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Adaptive rescaling
    img = adaptive_rescale_image(img)

    # Convert the image to grayscale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(threshold, (1, 1), 0)
   
    return blurred

'''
# Test Processed Image Quality
image_path = "C:\\Users\\biboy\\Desktop\\Underwrting Ai\\Underwriting_project\\images\\test2.png"
cv2.imshow("Preprocessed Image", preprocess_image(image_path))
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
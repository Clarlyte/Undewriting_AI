import os
from text_extraction import extract_text

# Directory containing the images
image_dir = "C:\\Users\\biboy\\Desktop\\Underwrting Ai\\Underwriting_project\\images"

# Specify the directory to save the README files
output_directory = "C:\\Users\\biboy\\Desktop\\Underwrting Ai\\Underwriting_project\\extracted_text\\"

# Iterate over all files in the image directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Construct the full path to the image file
        image_path = os.path.join(image_dir, filename)

        # Extract text from the image
        text = extract_text(image_path)

        # Construct the README file path
        readme_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".txt")

        # Save the extracted text to the README file
        with open(readme_file, "w") as readme:
            readme.write(text)

print("Extraction complete. Check individual README files for the extracted text.")

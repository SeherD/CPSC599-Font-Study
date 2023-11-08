from PIL import Image
import os

input_directory = r"C:\Users\seher\Desktop\Fall 2023\CPSC599\AdobeVFR\unsupervised_data_round6"
output_directory = r"C:\Users\seher\Desktop\Fall 2023\CPSC599\AdobeVFR\unsupervised_data_thumb"


if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def resize_with_padding(image_path, output_path, size=(256, 256)):
    try:
        img = Image.open(image_path)

        # Create a new white background image of the target size
        new_img = Image.new("RGB", size, "white")

        # Calculate the size of the thumbnail without cutting or cropping
        img.thumbnail(size)

        # Calculate the position to paste the thumbnail (center it)
        position = ((size[0] - img.size[0]) // 2, (size[1] - img.size[1]) // 2)

        # Paste the thumbnail onto the new background
        new_img.paste(img, position)

        # Save the new image
        new_img.save(output_path)
    except Exception as e:
        print(f"An error occurred with image: {image_path}")
        print(f"Error message: {e}")
        # Handle the error as needed

# Iterate through each image in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # You can add more extensions as needed
        file_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        resize_with_padding(file_path, output_path)

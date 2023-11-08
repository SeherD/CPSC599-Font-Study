import os
import random
import shutil

# Function to randomly select and copy 6000 images from a directory
def select_random_images(source_dir, output_dir, num_images):
    all_images = [f for f in os.listdir(source_dir) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]
    
    # Choose 6000 random images
    selected_images = random.sample(all_images, num_images)

    # Copy the randomly selected images to the output directory
    for image in selected_images:
        source_path = os.path.join(source_dir, image)
        destination_path = os.path.join(output_dir, image)
        shutil.copyfile(source_path, destination_path)
        print(f"Copied {image} to {output_dir}")

# Replace these paths with your source directory and output directory
source_directory = r'C:\Users\seher\Desktop\Fall 2023\CPSC599\AdobeVFR\scrape-wtf-new'
output_directory = r'C:\Users\seher\Desktop\Fall 2023\CPSC599\AdobeVFR\unsupervised_data_round6'

# Number of images you want to select
num_images_to_select = 2000
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
# Call the function to select and copy 6000 random images
select_random_images(source_directory, output_directory, num_images_to_select)

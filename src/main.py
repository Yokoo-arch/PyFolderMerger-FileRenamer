"""
Wrote by Yokoo-arch 2023 (https://github.com/Yokoo-arch).
Github repository: https://github.com/Yokoo-arch/***.
If you have any issues, please feel free to open an issue on the Github repository.
"""

# Imports
import os
import shutil
from utility.log_config import logger
import zipfile

# Source folders containing image files
source_folders = ['resources/image3', 'resources/images', 'resources/images (1)']

# Destination folder where you want to merge and rename the images
destination_folder = 'resources/merged_images'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    logger.info(f'Created "{destination_folder}" folder')

# Initialize a counter for renaming
counter = 1

# Iterate through each source folder
for source_folder in source_folders:
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)
    # Filter only image files (customizable if needed)
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
    logger.info(f'Found {len(image_files)} files in "{source_folder}" folder')

    # Iterate through the image files and copy them to the destination folder
    for image_file in image_files:
        # Generate the new filename as "image_<counter>.<file_extension>"
        file_extension = os.path.splitext(image_file)[1]
        new_filename = f'image_{counter}{file_extension}'
        logger.info(f'Renaming "{image_file}" to "{new_filename}"')
        # Copy the file to the destination folder with the new name
        source_path = os.path.join(source_folder, image_file)
        destination_path = os.path.join(destination_folder, new_filename)
        shutil.copy(source_path, destination_path)
        logger.info(f'Copied "{source_path}" to "{destination_path}"')
        
        # Increment the counter for the next image
        counter += 1

logger.info(f'{counter - 1} images merged and renamed in "{destination_folder}"')

# Create a zip file with the merged images
zip_filename = 'resources/merged_images.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(destination_folder):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, destination_folder))

logger.info(f'Created {zip_filename}')
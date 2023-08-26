# Folder Merger and File Renamer

This Python script allows you to merge image files from multiple source folders into a single destination folder while renaming them sequentially. Additionally, it creates a zip archive of the merged images.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Yokoo-arch/Image-Merger-and-Renamer.git
   cd Image-Merger-and-Renamer
2. Install the required libraries (loguru) if not already installed:
   ```bash
    pip install loguru

3. Modify the main.py file to specify your source folders and destination folder as needed.

4. Run the script:

   ```bash
    python main.py
4. The script will merge the images and create a zip file containing the merged images in the destination folder.

## Project Structure
- **main.py:** The main Python script that performs the image merging and renaming.
- **log_config.py:** Configuration for logging using the Loguru library.
- **resources/: Directory containing source folders and the destination folder.
- **resources/image3, resources/images, resources/images (1):** Sample source folders containing image files.
- **resources/merged_images:** Destination folder where merged and renamed images are stored.
- **resources/merged_images.zip:** Zip archive containing the merged images.
## Author
**@Yokoo-arch**
## Issues
If you encounter any issues or have suggestions, please feel free to open an issue on the GitHub repository.

*Note:* This project was created as a part of the Image Merger and Renamer project by Yokoo-arch.
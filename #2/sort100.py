import os
import shutil
import re

def divide_png_files_into_sequential_folders(source_directory, file_limit=100):
    # Helper function to extract numbers from .png file names
    def extract_number(file_name):
        match = re.search(r'(\d+)\.png$', file_name)
        return int(match.group(1)) if match else None

    # Check if source directory exists
    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return

    # Get a list of all .png files in the source directory
    files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f)) and f.lower().endswith('.png')]

    # Check if there are any PNG files
    if not files:
        print("No PNG files found in the specified directory.")
        return

    # Sort the files by the number in their names
    files = sorted(files, key=lambda f: extract_number(f))

    total_files = len(files)
    total_folders = (total_files // file_limit) + (1 if total_files % file_limit != 0 else 0)

    for folder_num in range(total_folders):
        # Create sequential folder names like #1, #2, #3, etc.
        folder_name = os.path.join(source_directory, f'#{folder_num + 1}')
        os.makedirs(folder_name, exist_ok=True)

        # Get the next batch of files (up to file_limit)
        start_idx = folder_num * file_limit
        end_idx = start_idx + file_limit
        files_to_move = files[start_idx:end_idx]

        # Move the files into the current folder
        for file in files_to_move:
            src_file_path = os.path.join(source_directory, file)
            dest_file_path = os.path.join(folder_name, file)
            shutil.move(src_file_path, dest_file_path)

        print(f"Moved {len(files_to_move)} files to folder {folder_name}")

# Specify the source directory (where your .png files are located)
source_directory = 'C:/Users/femit/OneDrive/Desktop/Bytegen-labs/workedd/#2'

# Call the function to move .png files in batches of 100 based on file numbers in the names
divide_png_files_into_sequential_folders(source_directory, 100)

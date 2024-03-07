from PIL import Image
from PIL.ExifTags import TAGS
import hachoir.parser
from hachoir.metadata import extractMetadata
from os.path import splitext

def extract_image_metadata(filename):
    image = Image.open(filename)
    image_metadata = image._getexif()
    return {TAGS.get(tag): value for tag, value in image_metadata.items() if tag in TAGS}

def extract_video_metadata(filename):
    parser = hachoir.parser.createParser(filename)
    metadata = extractMetadata(parser)
    return metadata.exportDictionary()['Metadata']

def save_metadata_to_txt(metadata, output_filename):
    with open(output_filename, 'w') as file:
        for key, value in metadata.items():
            file.write(f"{key}: {value}\n")

def user_choice():
    choice = input("Enter 'image' for pictures or 'video' for movies: ").lower()
    if choice == 'image':
        filename = input("Enter the image file name: ")
        metadata = extract_image_metadata(filename)
        save_metadata_to_txt(metadata, f"{splitext(filename)[0]}_metadata.txt")
        print(f"Metadata extracted and saved to {splitext(filename)[0]}_metadata.txt")
    elif choice == 'video':
        filename = input("Enter the video file name: ")
        metadata = extract_video_metadata(filename)
        save_metadata_to_txt(metadata, f"{splitext(filename)[0]}_metadata.txt")
        print(f"Metadata extracted and saved to {splitext(filename)[0]}_metadata.txt")
    else:
        print("Invalid choice. Please enter 'image' or 'video'.")

# Example usage:
user_choice()

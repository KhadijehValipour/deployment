from PIL import Image
import os

def resize_images(input_folder, output_folder, width, height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image file
            img = Image.open(os.path.join(input_folder, filename))

            # Resize the image
            resized_img = img.resize((width, height))

            # Save the resized image to the output folder
            resized_img.save(os.path.join(output_folder, filename))

    print("Images resized and saved successfully!")

# Set the input folder containing the photos
input_folder = "weather_app\icon_app"

# Set the output folder for resized photos
output_folder = "weather_app\icon_app_resize"

# Set the desired width and height for resizing
desired_width = 135
desired_height = 50

# Resize images in the input folder and save them to the output folder
resize_images(input_folder, output_folder, desired_width, desired_height)

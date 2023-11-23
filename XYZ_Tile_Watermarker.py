"""
Name: XYZ_Tile_Watermarker
Author: burakustuner
Date: 23.11.2023
Description: 
    This script adds a watermark to image tiles in specified layers.
    It processes every 'frequency'-th file in the given directory and
    applies the specified watermark text with certain stylistic 
    attributes like font size, color, and margins.

Usage:
    ! pip install Pillow
    ! Check if python added to path like "C:\Users\burak.ustuner\AppData\Roaming\Python\Python312\Scripts"
    
    Modify the parameters in the add_watermark function call as per your requirements.
    The function can be called with different directories, watermark texts, 
    layer levels, fonts, sizes, colors, and frequencies.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(directory, watermark_text, layer_levels, font_path="arial.ttf", font_size=10, 
                  text_color=(255, 255, 255, 128), margin_right=10, margin_bottom=10, frequency=10):
    for layer in layer_levels:
        path = os.path.join(directory, str(layer))
        for root, _, files in os.walk(path):
            for index, file in enumerate(files):
                if index % frequency == 0: # Process every 'frequency'-th file
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        try:
                            full_path = os.path.join(root, file)
                            image = Image.open(full_path)
                            draw = ImageDraw.Draw(image)
                            # Specify font and size
                            try:
                                font = ImageFont.truetype(font_path, font_size)
                            except IOError:
                                font = ImageFont.load_default()
                                print("Default font is being used as the specified font was not found.")

                            # Calculate watermark text size
                            text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:]
                            x = image.width - text_width - margin_right
                            y = image.height - text_height - margin_bottom

                            # Draw watermark in the bottom right corner
                            draw.text((x, y), watermark_text, text_color, font=font)

                            image.save(full_path)
                        except Exception as e:
                            print(f"Error processing {file}: {e}")


# Example usage
add_watermark(directory="E:\\XYZ_Tile\\milas_xyz",  # Specify Directory
              watermark_text="01.01.2001", # Specify watermark text
              layer_levels=[17], # Specify layer levels
              font_path="arial.ttf",  # Specify font path
              font_size=10, # Specify font size
              text_color=(255, 255, 255, 10),  # Specify text color
              margin_right=10, # Specify margin right
              margin_bottom=10, # Specify margin bottom
              frequency=5)  # Specify frequency

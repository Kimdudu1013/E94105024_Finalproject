import os
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

def load_image(file_path):
    """Load an image from a file path."""
    return Image.open(file_path)

def save_image(image, file_path):
    """Save an image to a file path."""
    image.save(file_path)

def flip_image_horizontal(image):
    """Flip an image horizontally."""
    return ImageOps.mirror(image)

def flip_image_vertical(image):
    """Flip an image vertically."""
    return ImageOps.flip(image)

def resize_image(image, size):
    """Resize an image to the given size."""
    return image.resize(size)

def adjust_brightness(image, factor):
    """Adjust the brightness of an image."""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    """Adjust the contrast of an image."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def adjust_color(image, factor):
    """Adjust the color balance of an image."""
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)

def crop_image(image, box):
    """Crop an image to the given box."""
    return image.crop(box)

def rotate_image(image, angle):
    """Rotate an image by a given angle."""
    return image.rotate(angle, expand=True)

def image_to_matrix(image):
    """Convert an image to a NumPy matrix."""
    return np.array(image)

def matrix_to_image(matrix):
    """Convert a NumPy matrix to an image."""
    return Image.fromarray(matrix)


if __name__ == "__main__":
    # Define the input and output directories
    input_dir = '/Users/user/Desktop/photo/kimdudu'
    output_dir = '/Users/user/Desktop/Photo/Photo.edited'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the input file path
    input_file = os.path.join(input_dir, '咬嘴唇.jpg')
    
    # Load image
    image = load_image(input_file)
    
    # Flip image horizontally
    flipped_horizontal_image = flip_image_horizontal(image)
    save_image(flipped_horizontal_image, os.path.join(output_dir, 'flipped_horizontal(水平翻轉).jpg'))
    
    # Flip image vertically
    flipped_vertical_image = flip_image_vertical(image)
    save_image(flipped_vertical_image, os.path.join(output_dir, 'flipped_vertical(垂直翻轉).jpg'))

    # Resize image
    resized_image = resize_image(image, (200, 200))
    save_image(resized_image, os.path.join(output_dir, 'resized(縮放).jpg'))
    
    # Adjust brightness
    brighter_image = adjust_brightness(image, 1.5)
    save_image(brighter_image, os.path.join(output_dir, 'brighter(曝光).jpg'))
    
    # Adjust contrast
    contrasted_image = adjust_contrast(image, 1.5)
    save_image(contrasted_image, os.path.join(output_dir, 'contrasted(對比度).jpg'))
    
    # Adjust color balance
    color_adjusted_image = adjust_color(image, 1.5)
    save_image(color_adjusted_image, os.path.join(output_dir, 'color_adjusted(色彩平衡).jpg'))
    
    # Crop image
    cropped_image = crop_image(image, (100, 100, 400, 400))
    save_image(cropped_image, os.path.join(output_dir, 'cropped(裁剪).jpg'))
    
    # Rotate image
    rotated_image = rotate_image(image, 45)
    save_image(rotated_image, os.path.join(output_dir, 'rotated(旋轉).jpg'))
    
    # Convert image to matrix and back
    image_matrix = image_to_matrix(image)
    new_image = matrix_to_image(image_matrix)
    save_image(new_image, os.path.join(output_dir, 'new_photo(圖像與矩陣之間的轉換).jpg'))


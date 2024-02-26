import os
from PIL import Image
import numpy as np

def floyd_steinberg_dithering(input_image):
    # convert to grayscale
    img = input_image.convert('L')
    pixels = np.array(img, dtype=np.float32)

    # Get dimensions
    height, width = pixels.shape

    for y in range(height):
        for x in range(width):
            old_pixel = pixels[y, x]
            new_pixel = 0 if old_pixel < 128 else 255
            pixels[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            if x < width - 1:
                pixels[y, x+1] += quant_error * 7 / 16
            if x > 0 and y < height - 1:
                pixels[y+1, x-1] += quant_error * 3 / 16
            if y < height - 1:
                pixels[y+1, x] += quant_error * 5 / 16
            if x < width - 1 and y < height - 1:
                pixels[y+1, x+1] += quant_error * 1 / 16

    # Convert back to uint8 and create an image
    result_img = Image.fromarray(np.clip(pixels, 0, 255).astype('uint8'))
    return result_img

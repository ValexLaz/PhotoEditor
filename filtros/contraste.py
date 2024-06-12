# filtros/contraste.py
import cv2
import numpy as np

def adjust_contrast(image, contrast_factor):
    contrast_factor = max(0, contrast_factor)
    image_float = image.astype(np.float32)
    mean = np.mean(image_float)
    adjusted = contrast_factor * (image_float - mean) + mean

    adjusted = np.clip(adjusted, 0, 255).astype(np.uint8)

    return adjusted

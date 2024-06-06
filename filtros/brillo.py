import numpy as np
import cv2

def adjust_brightness(img, brightness_factor):
    img = img.astype(np.float32)
    img = img * (brightness_factor / 100.0)
    img = np.clip(img, 0, 255)
    img = img.astype(np.uint8)
    return img

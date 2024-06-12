import cv2
import numpy as np

def apply_negative(img):
    if img is None:
        return None

    negative_img = 255 - img  
    return negative_img

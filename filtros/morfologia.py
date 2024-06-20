import cv2
import numpy as np

def apply_dilation(image, kernel_size=(5, 5), iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=iterations)
    return dilated_image

def apply_erosion(image, kernel_size=(5, 5), iterations=1):
    kernel = np.ones(kernel_size, np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=iterations)
    return eroded_image

import cv2
from PIL import Image
def apply_gray_filter(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_image_rgb = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
    return gray_image_rgb

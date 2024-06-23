import numpy as np
import cv2

def apply_kernel1(image):
    kernel = np.ones((5,5),np.float32)/30
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

def apply_kernel2(image):
    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

def apply_kernel3(image):
    kernel = np.array([[0,0,0],[0,2,0],[0,0,0]])
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

def apply_random_kernel(image):
    kernel_size = (3, 3)
    kernel = np.random.rand(*kernel_size) * 10 - 1
    return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

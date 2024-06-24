import cv2
import numpy as np

class Convolution:
    def __init__(self, image, kernel):
        self.image = image
        self.kernel = kernel

    def apply_convolution(self):
        convolved_image = cv2.filter2D(self.image, -1, self.kernel)
        return convolved_image

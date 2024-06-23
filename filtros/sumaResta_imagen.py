import cv2
import numpy as np

class SumaRestaImagen:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2

    def resize_images(self):
        self.img2 = cv2.resize(self.img2, (self.img1.shape[1], self.img1.shape[0]), interpolation=cv2.INTER_LINEAR)

    def sumar_imagenes(self, alpha1, alpha2):
        self.resize_images()
        gray_img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY)
        sum_img = cv2.addWeighted(gray_img1, alpha1, gray_img2, alpha2, 0)
        return sum_img

    def restar_imagenes(self, alpha1, alpha2):
        self.resize_images()
        gray_img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY)
        rest_img = cv2.addWeighted(gray_img1, alpha1, gray_img2, -alpha2, 0)
        return rest_img

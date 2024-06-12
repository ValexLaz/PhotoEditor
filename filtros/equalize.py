import cv2
import numpy as np
from matplotlib import pyplot as plt

class EqualizeHistogram:
    def __init__(self, image):
        self.image = image
    def equalize_histogram(self):
        if self.image is None:
            print("No se ha cargado ninguna imagen.")
            return None
        if len(self.image.shape) == 3:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        else:
            gray_image = self.image
        equalized_image = cv2.equalizeHist(gray_image)
        return equalized_image

    def plot_equalized_histogram(self):
        equalized_image = self.equalize_histogram()
        if equalized_image is None:
            return None
        hist, bins = np.histogram(equalized_image.flatten(), 256, [0, 256])
        plt.figure()
        plt.title("Histograma Ecualizado")
        plt.xlabel("Intensidad de píxel")
        plt.ylabel("Cantidad de píxeles")
        plt.plot(hist, color='black')
        plt.xlim([0, 256])
        plt.show()
        return equalized_image

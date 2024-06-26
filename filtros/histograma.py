import cv2
import matplotlib.pyplot as plt
import numpy as np

class Histogram:
    def __init__(self, image):
        self.image = image

    def compute_histogram(self):
        if self.image is None:
            print("No se ha cargado ninguna imagen.")
            return None, None
        if len(self.image.shape) == 3:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        else:
            gray_image = self.image
        hist, bins = np.histogram(gray_image.flatten(), 256, [0, 256])
        return hist, bins, gray_image

    def plot_histogram(self):
        hist, bins, gray_image = self.compute_histogram()

        if hist is None or bins is None:
            return None

        plt.figure()
        plt.title("Histograma de la imagen")
        plt.xlabel("Intensidad de píxel")
        plt.ylabel("Cantidad de píxeles")
        plt.plot(hist, color='black')
        plt.xlim([0, 256])
        plt.show()

        return gray_image

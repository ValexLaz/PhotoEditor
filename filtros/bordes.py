import cv2
import numpy as np

def edge_detection_and_display(img):
    if img is not None:
        # Convertimos la imagen a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Aplicamos umbralización
        ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

        # Detectamos contornos
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dibujamos los contornos encontrados en la imagen original
        img_with_contours = img.copy()
        cv2.drawContours(img_with_contours, contours, -1, (255, 0, 0), 2)

        return img_with_contours

    return None

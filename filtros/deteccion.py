import cv2
import numpy as np

def detect_objects(img, min_area_threshold=100):
    if img is None:
        print("No se ha cargado ninguna imagen.")
        return None

    # Convertir la imagen a escala de grises
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Aplicar umbralización
    ret, thresh = cv2.threshold(imgray, 230, 255, cv2.THRESH_BINARY)

    # Dilatación para eliminar el ruido y cerrar pequeños huecos en los objetos
    kernel = np.ones((10, 10), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # Encontrar contornos en la imagen dilatada
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar rectángulos alrededor de los objetos y numerarlos
    objeto_numero = -1
    img_with_rectangles = img.copy()
    for c in contours:
        area = cv2.contourArea(c)
        if area > min_area_threshold:
            objeto_numero += 1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img_with_rectangles, (x, y), (x + w, y + h), (0, 0, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_with_rectangles, f'Objeto {objeto_numero}', (x, y - 10), font, 0.5, (0, 0, 0), 2,
                        cv2.LINE_AA)

    return img_with_rectangles

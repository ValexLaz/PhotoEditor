import cv2
import numpy as np

def apply_quantization(img, clusters=5):
    if img is None or clusters == 0:
        return img
    data = img.reshape((-1, 3))
    data = np.float32(data)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(data, clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized_img = centers[labels.flatten()]
    quantized_img = quantized_img.reshape((img.shape))

    return quantized_img


def apply_pixelation(img, pixel_size=3):
    if img is None or pixel_size == 0:
        return img
    height, width = img.shape[:2]
    small_img = cv2.resize(img, (pixel_size, pixel_size), interpolation=cv2.INTER_LINEAR)
    pixelated_img = cv2.resize(small_img, (width, height), interpolation=cv2.INTER_NEAREST)

    return pixelated_img

import cv2
import numpy as np

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def perspective_transform(image, points_in, points_out):
    M = cv2.getPerspectiveTransform(np.float32(points_in), np.float32(points_out))
    transformed = cv2.warpPerspective(image, M, (image.shape[1], image.shape[0]))
    return transformed

def custom_transform_1(image):
    h, w = image.shape[:2]
    points_in = [[0, 0], [0, h], [w, h], [w, 0]]
    points_out = [[0, 0], [0, h], [w // 3, h // 2], [w // 3, 0]]
    return perspective_transform(image, points_in, points_out)

def custom_transform_2(image):
    h, w = image.shape[:2]
    points_in = [[0, 0], [0, h], [w, h], [w, 0]]
    points_out = [[w // 3, h // 2], [0, h], [w, h], [w - w // 3, h // 2]]
    return perspective_transform(image, points_in, points_out)

def custom_transform_3(image):
    h, w = image.shape[:2]
    points_in = [[0, 0], [0, h], [w, h], [w, 0]]
    points_out = [[w // 3, h // 2], [w // 3, 0], [2 * (w // 3), 0], [2 * (w // 3), h // 2]]
    return perspective_transform(image, points_in, points_out)

def custom_transform_4(image):
    h, w = image.shape[:2]
    points_in = [[0, 0], [0, h], [w, h], [w, 0]]
    points_out = [[w, 0], [w, h], [2 * w // 3, h // 2], [2 * w // 3, 0]]
    return perspective_transform(image, points_in, points_out)

import cv2
from PIL import Image, ImageTk

def resize_image(img, max_size):
    h, w = img.shape[:2]
    scale = min(max_size / h, max_size / w)
    new_size = (int(w * scale), int(h * scale))
    return cv2.resize(img, new_size)

def segment_color(img_rgb, panel, layer):
    if img_rgb is not None:
        if layer == 'R':
            segmented_img = img_rgb[:, :, 0]
            cmap = 'Reds'
        elif layer == 'G':
            segmented_img = img_rgb[:, :, 1]
            cmap = 'Greens'
        elif layer == 'B':
            segmented_img = img_rgb[:, :, 2]
            cmap = 'Blues'

        segmented_img_resized = resize_image(segmented_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(segmented_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

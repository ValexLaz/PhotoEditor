import cv2
from PIL import Image, ImageTk

def apply_gaussian_blur(img, kernel_size):
    """Aplica el filtro Gaussiano a la imagen."""
    return cv2.GaussianBlur(img, kernel_size, 0)

def apply_gaussian(img_rgb):
    """Aplica el filtro Gaussiano a la imagen y devuelve la imagen filtrada lista para mostrar."""
    if img_rgb is not None:
        kernel_size = (15, 15)
        blurred_img = apply_gaussian_blur(img_rgb, kernel_size)

        # Redimensionar imagen filtrada
        resized_img = cv2.resize(blurred_img, (600, 600))

        # Convertir imagen a formato compatible con Tkinter
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)))
        return img_tk

    return None

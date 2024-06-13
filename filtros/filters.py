import cv2
from PIL import Image, ImageTk

def apply_blur(img, kernel_size):
    """Aplica el filtro de blur a la imagen."""
    return cv2.blur(img, kernel_size)


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

def apply_laplace_filter(img):
    """Aplica el filtro de Laplace a la imagen y devuelve la imagen filtrada lista para mostrar."""
    if img is not None:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blurred_img = cv2.GaussianBlur(gray_img, (3, 3), 0)

        laplace = cv2.Laplacian(blurred_img, cv2.CV_64F)

        af = gray_img - laplace
        af_uint8 = cv2.convertScaleAbs(af)

        result = cv2.addWeighted(img, 1, cv2.cvtColor(af_uint8, cv2.COLOR_GRAY2BGR), 0.5, 0)

        resized_result = cv2.resize(result, (600, 600))

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(resized_result, cv2.COLOR_BGR2RGB)))
        return img_tk

    return None

def apply_sobel_filter(img, dx, dy, ksize=3):
    """Aplica el filtro Sobel a la imagen."""
    if img is not None:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobel = cv2.Sobel(gray_img, cv2.CV_64F, dx, dy, ksize=ksize)
        abs_sobel = cv2.convertScaleAbs(sobel)
        sobel_img = cv2.cvtColor(abs_sobel, cv2.COLOR_GRAY2BGR)
        return sobel_img
    return None

def apply_canny_filter(img, threshold1, threshold2):
    """Aplica el filtro Canny a la imagen."""
    if img is not None:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_img, threshold1, threshold2)
        canny_img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return canny_img
    return None

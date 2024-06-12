import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
from filtros.segmentacion import segment_color, resize_image
from filtros.byn import apply_gray_filter
from filtros.brillo import adjust_brightness
from filtros.filters import apply_gaussian_blur, apply_laplace_filter
from filtros.histograma import Histogram
from filtros.equalize import EqualizeHistogram
from filtros.contraste import adjust_contrast

img = None
img_rgb = None
current_img = None

def load_image():
    global img, img_rgb, current_img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    current_img = img_rgb

    img_resized = resize_image(img_rgb, 600)

    img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
    panel.config(image=img_tk)
    panel.image = img_tk

    on_frame_configure(None)

def show_info():
    if img is not None:
        img_shape = img.shape
        info_label.config(text=f"Tamaño de la imagen: {img_shape}")
    else:
        info_label.config(text="No se ha cargado ninguna imagen")

def apply_gray_filter_and_display():
    global current_img
    if img is not None:
        gray_img = apply_gray_filter(img)
        current_img = gray_img
        gray_img_resized = resize_image(gray_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(gray_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def adjust_brightness_and_display(brightness):
    global current_img
    if current_img is not None:
        bright_img = adjust_brightness(current_img, brightness)
        bright_img_resized = resize_image(bright_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(bright_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def apply_gaussian_and_display():
    global current_img
    if img is not None:
        blurred_img = apply_gaussian_blur(current_img, (15, 15))
        current_img = blurred_img
        blurred_img_resized = resize_image(blurred_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(blurred_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def show_histogram():
    global current_img
    if img is not None:
        histogram = Histogram(current_img)
        gray_image = histogram.plot_histogram()

        if gray_image is not None:
            current_img = gray_image
            gray_img_resized = resize_image(gray_image, 600)
            img_tk = ImageTk.PhotoImage(image=Image.fromarray(gray_img_resized))
            panel.config(image=img_tk)
            panel.image = img_tk

            on_frame_configure(None)
        else:
            info_label.config(text="Error al generar el histograma.")
    else:
        info_label.config(text="No se ha cargado ninguna imagen")

def equalize_histogram_and_display():
    global current_img
    if img is not None:
        equalizer = EqualizeHistogram(current_img)
        equalized_image = equalizer.plot_equalized_histogram()

        if equalized_image is not None:
            current_img = equalized_image
            equalized_img_resized = resize_image(equalized_image, 600)
            img_tk = ImageTk.PhotoImage(image=Image.fromarray(equalized_img_resized))
            panel.config(image=img_tk)
            panel.image = img_tk

            on_frame_configure(None)
        else:
            info_label.config(text="Error al ecualizar el histograma.")
    else:
        info_label.config(text="No se ha cargado ninguna imagen")

def apply_laplace_and_display():
    global current_img
    if img is not None:
        laplace_img = apply_laplace_filter(img)
        if laplace_img is not None:
            panel.config(image=laplace_img)
            panel.image = laplace_img
            current_img = img

            on_frame_configure(None)

def adjust_contrast_and_display(contrast):
    global current_img
    if current_img is not None:
        contrast_img = adjust_contrast(current_img, float(contrast))
        contrast_img_resized = resize_image(contrast_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(contrast_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def reset_image():
    global current_img
    if img_rgb is not None:
        current_img = img_rgb
        img_resized = resize_image(img_rgb, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

win = tk.Tk()
win.title("Procesamiento de Imágenes")
win.geometry("1000x600")

left_frame = tk.Frame(win, width=600, height=600)
left_frame.pack(side="left", fill="both", expand=True)

right_frame_canvas = tk.Canvas(win, width=200, height=600)
right_frame_canvas.pack(side="right", fill="y")

scrollbar = tk.Scrollbar(win, orient="vertical", command=right_frame_canvas.yview)
scrollbar.pack(side="right", fill="y")
right_frame_canvas.configure(yscrollcommand=scrollbar.set)
right_frame = tk.Frame(right_frame_canvas)
right_frame_canvas.create_window((0,0), window=right_frame, anchor="nw")

def on_frame_configure(event):
    right_frame_canvas.configure(scrollregion=right_frame_canvas.bbox("all"))

right_frame.bind("<Configure>", on_frame_configure)

panel = tk.Label(left_frame)
panel.pack(padx=10, pady=10)

load_btn = tk.Button(right_frame, text="Cargar Imagen", command=load_image)
load_btn.pack(pady=10)

info_label = tk.Label(right_frame, text="Tamaño de la imagen: ", font=('Helvetica', 12))
info_label.pack(pady=10)

histogram_btn = tk.Button(right_frame, text="Mostrar Histograma", command=show_histogram)
histogram_btn.pack(pady=10)

equalize_hist_btn = tk.Button(right_frame, text="Ecualizar Histograma", command=equalize_histogram_and_display)
equalize_hist_btn.pack(pady=10)

info_btn = tk.Button(right_frame, text="Mostrar Información", command=show_info)
info_btn.pack(pady=10)

btn_red = tk.Button(right_frame, text="Segmentar Rojo", command=lambda: segment_color(img_rgb, panel, 'R'))
btn_red.pack(pady=5)
btn_green = tk.Button(right_frame, text="Segmentar Verde", command=lambda: segment_color(img_rgb, panel, 'G'))
btn_green.pack(pady=5)
btn_blue = tk.Button(right_frame, text="Segmentar Azul", command=lambda: segment_color(img_rgb, panel, 'B'))
btn_blue.pack(pady=5)
btn_gray = tk.Button(right_frame, text="Blanco y Negro", command=apply_gray_filter_and_display)
btn_gray.pack(pady=5)

brightness_scrollbar = tk.Scale(right_frame, from_=0, to_=200, orient=tk.HORIZONTAL, label="Ajustar Brillo", command=lambda value: adjust_brightness_and_display(int(value)))
brightness_scrollbar.set(100)
brightness_scrollbar.pack(pady=5)

contrast_scrollbar = tk.Scale(right_frame, from_=0.5, to_=3.0, resolution=0.1, orient=tk.HORIZONTAL, label="Ajustar Contraste", command=lambda value: adjust_contrast_and_display(value))
contrast_scrollbar.set(1.0)
contrast_scrollbar.pack(pady=5)

gaussian_btn = tk.Button(right_frame, text="Aplicar Filtro Gaussiano", command=apply_gaussian_and_display)
gaussian_btn.pack(pady=10)

laplace_btn = tk.Button(right_frame, text="Aplicar Filtro Laplace", command=apply_laplace_and_display)
laplace_btn.pack(pady=10)

reset_btn = tk.Button(right_frame, text="Restaurar Imagen", command=reset_image)
reset_btn.pack(pady=10)

win.mainloop()

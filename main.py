import tkinter as tk
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from filtros.segmantacion import resize_image, segment_color


def load_image():
    global img, img_rgb
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_resized = resize_image(img_rgb, 600)

    img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
    panel.config(image=img_tk)
    panel.image = img_tk

def show_info():
    if img is not None:
        img_shape = img.shape
        info_label.config(text=f"Tamaño de la imagen: {img_shape}")
    else:
        info_label.config(text="No se ha cargado ninguna imagen")

win = tk.Tk()
win.title("Procesamiento de Imágenes")
win.geometry("800x600")

left_frame = tk.Frame(win, width=600, height=600)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(win, width=200, height=600)
right_frame.pack(side="right", fill="both")

panel = tk.Label(left_frame)
panel.pack(padx=10, pady=10)

load_btn = tk.Button(right_frame, text="Cargar Imagen", command=load_image)
load_btn.pack(pady=10)

info_label = tk.Label(right_frame, text="Tamaño de la imagen: ", font=('Helvetica', 12))
info_label.pack(pady=10)

info_btn = tk.Button(right_frame, text="Mostrar Información", command=show_info)
info_btn.pack(pady=10)

btn_red = tk.Button(right_frame, text="Segmentar Rojo", command=lambda: segment_color(img_rgb, panel, 'R'))
btn_red.pack(pady=5)
btn_green = tk.Button(right_frame, text="Segmentar Verde", command=lambda: segment_color(img_rgb, panel, 'G'))
btn_green.pack(pady=5)
btn_blue = tk.Button(right_frame, text="Segmentar Azul", command=lambda: segment_color(img_rgb, panel, 'B'))
btn_blue.pack(pady=5)

win.mainloop()

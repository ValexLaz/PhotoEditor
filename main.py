import tkinter as tk
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# Función para redimensionar la imagen
def resize_image(img, max_size):
    h, w = img.shape[:2]
    scale = min(max_size / h, max_size / w)
    new_size = (int(w * scale), int(h * scale))
    return cv2.resize(img, new_size)

# Función para cargar la imagen
def load_image():
    global img, img_rgb
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Redimensionar imagen
    img_resized = resize_image(img_rgb, 600)
    
    # Mostrar imagen en la ventana
    img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
    panel.config(image=img_tk)
    panel.image = img_tk

# Función para mostrar la información de la imagen
def show_info():
    if img is not None:
        img_shape = img.shape
        info_label.config(text=f"Tamaño de la imagen: {img_shape}")
    else:
        info_label.config(text="No se ha cargado ninguna imagen")

# Función para mostrar la imagen segmentada por capas de color
def segment_color(layer):
    if img is not None:
        if layer == 'R':
            segmented_img = img_rgb[:,:,0]
            cmap = 'Reds'
        elif layer == 'G':
            segmented_img = img_rgb[:,:,1]
            cmap = 'Greens'
        elif layer == 'B':
            segmented_img = img_rgb[:,:,2]
            cmap = 'Blues'
        
        # Redimensionar imagen segmentada
        segmented_img_resized = resize_image(segmented_img, 600)
        
        # Mostrar imagen segmentada en la ventana
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(segmented_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

# Crear la ventana principal
win = tk.Tk()
win.title("Procesamiento de Imágenes")
win.geometry("800x600")

# Frame izquierdo para mostrar la imagen
left_frame = tk.Frame(win, width=600, height=600)
left_frame.pack(side="left", fill="both", expand=True)

# Frame derecho para los botones
right_frame = tk.Frame(win, width=200, height=600)
right_frame.pack(side="right", fill="both")

# Panel para mostrar la imagen cargada
panel = tk.Label(left_frame)
panel.pack(padx=10, pady=10)

# Botón para cargar la imagen
load_btn = tk.Button(right_frame, text="Cargar Imagen", command=load_image)
load_btn.pack(pady=10)

# Etiqueta para mostrar la información de la imagen
info_label = tk.Label(right_frame, text="Tamaño de la imagen: ", font=('Helvetica', 12))
info_label.pack(pady=10)

# Botón para mostrar la información de la imagen
info_btn = tk.Button(right_frame, text="Mostrar Información", command=show_info)
info_btn.pack(pady=10)

# Botones para segmentar por capas de color
btn_red = tk.Button(right_frame, text="Segmentar Rojo", command=lambda: segment_color('R'))
btn_red.pack(pady=5)
btn_green = tk.Button(right_frame, text="Segmentar Verde", command=lambda: segment_color('G'))
btn_green.pack(pady=5)
btn_blue = tk.Button(right_frame, text="Segmentar Azul", command=lambda: segment_color('B'))
btn_blue.pack(pady=5)

# Iniciar el loop de la aplicación
win.mainloop()

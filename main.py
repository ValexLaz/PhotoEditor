import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from filtros.segmentacion import segment_color, resize_image
from filtros.byn import apply_gray_filter
from filtros.brillo import adjust_brightness
from filtros.filters import apply_gaussian_blur, apply_laplace_filter,apply_blur, apply_sobel_filter, apply_canny_filter
from filtros.histograma import Histogram
from filtros.equalize import EqualizeHistogram
from filtros.contraste import adjust_contrast
from filtros.negativo import apply_negative
from filtros.cuantizacion import apply_quantization, apply_pixelation
from filtros.botones_transformaciones import create_transform_buttons,  set_globals
from filtros.morfologia import apply_dilation, apply_erosion
from filtros.kernels import apply_kernel1, apply_kernel2, apply_kernel3, apply_random_kernel
from filtros.sumaResta_imagen import SumaRestaImagen
from filtros.fourier import Fourier
from filtros.convolucion import Convolution
from filtros.bordes import edge_detection_and_display
from filtros.deteccion import detect_objects 


img = None
img_rgb = None
current_img = None
original_img = None
update_image_display = None
cap = None
def load_image():
    global img, img_rgb, current_img, original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"File path: {file_path}")
        img = cv2.imread(file_path)
        if img is None:
            print("Error: Unable to read the image.")
            return
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        current_img = img_rgb
        original_img = img_rgb

        img_resized = resize_image(img_rgb, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        set_globals(current_img, update_image_display)
        on_frame_configure(None)
    else:
        print("No file selected.")

def load_image1():
    global img1, current_img, original_img
    file_path = filedialog.askopenfilename()
    img1 = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    current_img = img_rgb
    original_img = img_rgb
    info_label.config(text="Imagen 1 cargada")
    img_resized = resize_image(img_rgb, 600)

    img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
    panel.config(image=img_tk)
    panel.image = img_tk
    set_globals(current_img, update_image_display)
    on_frame_configure(None)

def load_image2():
    global img2
    file_path = filedialog.askopenfilename()
    img2 = cv2.imread(file_path)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    info_label.config(text="Imagen 2 cargada")

def detect_objects_callback():
    global img_rgb  # Asegúrate de tener acceso a la variable img_rgb globalmente
    if img_rgb is None:
        print("No se ha cargado ninguna imagen.")
        return
    
    img_with_rectangles = detect_objects(img_rgb)
    update_image_display(img_with_rectangles)


def edge_detection_and_display_main():
    global current_img
    if current_img is not None:
        img_with_edges = edge_detection_and_display(current_img)
        update_image_display(img_with_edges)
    else:
        info_label.config(text="No se ha cargado ninguna imagen")

def sumar_imagenes_and_display(alpha1, alpha2):
    global current_img
    if img1 is not None and img2 is not None:
        suma_resta = SumaRestaImagen(img1, img2)
        sum_img = suma_resta.sumar_imagenes(alpha1, alpha2)
        current_img = sum_img
        sum_img_resized = resize_image(sum_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(sum_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def restar_imagenes_and_display(alpha1, alpha2):
    global current_img
    if img1 is not None and img2 is not None:
        suma_resta = SumaRestaImagen(img1, img2)
        rest_img = suma_resta.restar_imagenes(alpha1, alpha2)
        current_img = rest_img
        rest_img_resized = resize_image(rest_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(rest_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def update_image_display(img):
    img_resized = resize_image(img, 600)
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

def apply_blur_and_display(blur_level):
    global current_img
    if original_img is not None:
        kernel_sizes = [(1, 1), (3, 3), (5, 5), (7, 7), (9, 9), (11, 11)]
        kernel_size = kernel_sizes[int(blur_level)]
        blurred_img = apply_blur(original_img, kernel_size)  # Usamos la imagen original
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

def apply_negative_and_display():
    global current_img
    if current_img is not None:
        negative_img = apply_negative(current_img)
        negative_img_resized = resize_image(negative_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(negative_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def reset_image():
    global current_img, original_img
    if img_rgb is not None:
        current_img = img_rgb
        original_img = img_rgb  # Restablecemos la imagen original
        img_resized = resize_image(img_rgb, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def apply_sobel_and_display(dx, dy):
    global current_img
    if img is not None:
        sobel_img = apply_sobel_filter(current_img, dx, dy)
        current_img = sobel_img
        sobel_img_resized = resize_image(sobel_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(sobel_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def apply_canny_and_display(threshold1, threshold2):
    global current_img
    if img is not None:
        canny_img = apply_canny_filter(current_img, threshold1, threshold2)
        current_img = canny_img
        canny_img_resized = resize_image(canny_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(canny_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def apply_quantization_and_display(clusters):
    global current_img
    if current_img is not None:
        if clusters == 0:
            quantized_img = current_img
        else:
            quantized_img = apply_quantization(current_img, clusters)

        quantized_img_resized = resize_image(quantized_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(quantized_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def apply_pixelation_and_display(pixel_size):
    global current_img
    if current_img is not None:
        if pixel_size == 0:
            pixelated_img = current_img
        else:
            pixelated_img = apply_pixelation(current_img, pixel_size)

        pixelated_img_resized = resize_image(pixelated_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(pixelated_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def resize_image_custom():
    global current_img
    if current_img is not None:
        try:
            new_width = int(width_entry.get())
            new_height = int(height_entry.get())
            if new_width > 0 and new_height > 0:
                resized_img = cv2.resize(current_img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
                current_img = resized_img
                resized_img_resized = resize_image(resized_img, 600)

                img_tk = ImageTk.PhotoImage(image=Image.fromarray(resized_img_resized))
                panel.config(image=img_tk)
                panel.image = img_tk

                on_frame_configure(None)
            else:
                info_label.config(text="Por favor, ingrese valores válidos para el ancho y el alto.")
        except ValueError:
            info_label.config(text="Por favor, ingrese valores válidos para el ancho y el alto.")


def rotate_image(angle):
    global current_img
    if current_img is not None:
        height, width = current_img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_img = cv2.warpAffine(current_img, rotation_matrix, (width, height))
        current_img = rotated_img

        rotated_img_resized = resize_image(rotated_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(rotated_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def rotate_90_right():
    rotate_image(-90)

def rotate_90_left():
    rotate_image(90)


def apply_dilation_and_display(iterations):
    global current_img, original_img  # Asegúrate de incluir original_img
    if original_img is not None:
        dilated_img = apply_dilation(original_img, iterations=int(iterations))  # Usa original_img
        current_img = dilated_img
        dilated_img_resized = resize_image(dilated_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(dilated_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)


def apply_erosion_and_display(iterations):
    global current_img, original_img
    if original_img is not None:
        eroded_img = apply_erosion(original_img, iterations=int(iterations))
        current_img = eroded_img
        eroded_img_resized = resize_image(eroded_img, 600)

        img_tk = ImageTk.PhotoImage(image=Image.fromarray(eroded_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk

        on_frame_configure(None)

def apply_kernel1_and_display():
    global current_img
    if current_img is not None:
        kernel1_img = apply_kernel1(current_img)
        current_img = kernel1_img
        kernel1_img_resized = resize_image(kernel1_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(kernel1_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def apply_kernel2_and_display():
    global current_img
    if current_img is not None:
        kernel2_img = apply_kernel2(current_img)
        current_img = kernel2_img
        kernel2_img_resized = resize_image(kernel2_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(kernel2_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def apply_kernel3_and_display():
    global current_img
    if current_img is not None:
        kernel3_img = apply_kernel3(current_img)
        current_img = kernel3_img
        kernel3_img_resized = resize_image(kernel3_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(kernel3_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def apply_random_kernel_and_display():
    global current_img
    if current_img is not None:
        random_kernel_img = apply_random_kernel(current_img)
        current_img = random_kernel_img
        random_kernel_img_resized = resize_image(random_kernel_img, 600)
        img_tk = ImageTk.PhotoImage(image=Image.fromarray(random_kernel_img_resized))
        panel.config(image=img_tk)
        panel.image = img_tk
        on_frame_configure(None)

def start_camera():
    global cap
    cap = cv2.VideoCapture(1) #cambiar dependiendo de la camara
    display_camera()

def display_camera():
    global cap, img, img_rgb, current_img, original_img
    if cap is not None and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            img = frame
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_resized = resize_image(img_rgb, 600)
            img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
            panel.config(image=img_tk)
            panel.image = img_tk
            panel.after(10, display_camera)

def take_snapshot(event):
    global cap, img, img_rgb, current_img, original_img
    if cap is not None and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            img = frame
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            current_img = img_rgb
            original_img = img_rgb
            info_label.config(text="Imagen capturada de la cámara")
            set_globals(current_img, update_image_display)
            img_resized = resize_image(img_rgb, 600)
            img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
            panel.config(image=img_tk)
            panel.image = img_tk
            cap.release()

def apply_fourier_and_display():
    global current_img
    if current_img is not None:
        fourier = Fourier(current_img)
        magnitude_spectrum = fourier.apply_fourier_transform()
        show_image(magnitude_spectrum)
        plot_fourier_spectrum(fourier.get_fourier_spectrum())

def show_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = resize_image(img_rgb, 600)
    img_tk = ImageTk.PhotoImage(image=Image.fromarray(img_resized))
    panel.config(image=img_tk)
    panel.image = img_tk

def plot_fourier_spectrum(spectrum):
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.imshow(spectrum, cmap='gray')
    ax.set_title('Fourier Spectrum')

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def apply_convolution_and_display():
    global current_img
    if current_img is not None:
        kernel = np.array([[1, 0, -1],
                           [0, 0, 0],
                           [-1, 0, 1]])
        convolution = Convolution(current_img, kernel)
        convolved_image = convolution.apply_convolution()
        show_image(convolved_image)

win = tk.Tk()
win.title("Procesamiento de Imágenes")
win.geometry("1200x800")

left_frame = tk.Frame(win, width=800, height=800)
left_frame.pack(side="left", fill="both", expand=True)

right_frame_canvas = tk.Canvas(win, width=200, height=800)
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
load_btn.pack(pady=5)

camera_btn = tk.Button(right_frame, text="Encender Cámara", command=start_camera)
camera_btn.pack(pady=5)

info_label = tk.Label(right_frame, text="Tamaño de la imagen: ", font=('Helvetica', 12))
info_label.pack(pady=5)

histogram_btn = tk.Button(right_frame, text="Mostrar Histograma", command=show_histogram)
histogram_btn.pack(pady=5)

equalize_hist_btn = tk.Button(right_frame, text="Ecualizar Histograma", command=equalize_histogram_and_display)
equalize_hist_btn.pack(pady=5)

negative_btn = tk.Button(right_frame, text="Aplicar Negativo", command=apply_negative_and_display)
negative_btn.pack(pady=5)

info_btn = tk.Button(right_frame, text="Mostrar Información", command=show_info)
info_btn.pack(pady=5)

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

blur_scrollbar = tk.Scale(right_frame, from_=0, to_=5, orient=tk.HORIZONTAL, label="Ajustar Desenfoque", command=lambda value: apply_blur_and_display(int(value)))
blur_scrollbar.set(0)
blur_scrollbar.pack(pady=5)

gaussian_btn = tk.Button(right_frame, text="Aplicar Filtro Gaussiano", command=apply_gaussian_and_display)
gaussian_btn.pack(pady=5)

laplace_btn = tk.Button(right_frame, text="Aplicar Filtro Laplace", command=apply_laplace_and_display)
laplace_btn.pack(pady=5)

reset_btn = tk.Button(right_frame, text="Restaurar Imagen", command=reset_image)
reset_btn.pack(pady=5)

sobel_x_btn = tk.Button(right_frame, text="Aplicar Sobel X", command=lambda: apply_sobel_and_display(1, 0))
sobel_x_btn.pack(pady=5)

clusters_scrollbar = tk.Scale(right_frame, from_=0, to_=5, orient=tk.HORIZONTAL, label="Número de Clusters", command=lambda value: apply_quantization_and_display(int(value)))
clusters_scrollbar.set(0)
clusters_scrollbar.pack(pady=5)

pixel_size_scrollbar = tk.Scale(right_frame, from_=0, to_=5, orient=tk.HORIZONTAL, label="Tamaño del Pixelado", command=lambda value: apply_pixelation_and_display(int(value)))
pixel_size_scrollbar.set(0)
pixel_size_scrollbar.pack(pady=5)

sobel_y_btn = tk.Button(right_frame, text="Aplicar Sobel Y", command=lambda: apply_sobel_and_display(0, 1))
sobel_y_btn.pack(pady=5)

canny_btn = tk.Button(right_frame, text="Aplicar Canny", command=lambda: apply_canny_and_display(100, 200))
canny_btn.pack(pady=5)

width_label = tk.Label(right_frame, text="Ancho")
width_label.pack(pady=5)
width_entry = tk.Entry(right_frame)
width_entry.pack(pady=5)

height_label = tk.Label(right_frame, text="Alto")
height_label.pack(pady=5)
height_entry = tk.Entry(right_frame)
height_entry.pack(pady=5)

resize_button = tk.Button(right_frame, text="Cambiar Tamaño", command=resize_image_custom)
resize_button.pack(pady=5)

rotate_right_button = tk.Button(right_frame, text="Girar 90° a la Derecha", command=rotate_90_right)
rotate_right_button.pack(pady=5)

rotate_left_button = tk.Button(right_frame, text="Girar 90° a la Izquierda", command=rotate_90_left)
rotate_left_button.pack(pady=5)

create_transform_buttons(right_frame)

dilation_scrollbar = tk.Scale(right_frame, from_=0, to_=10, orient=tk.HORIZONTAL, label="Iteraciones de Dilatación", command=apply_dilation_and_display)
dilation_scrollbar.set(0)
dilation_scrollbar.pack(pady=5)

erosion_scrollbar = tk.Scale(right_frame, from_=0, to_=10, orient=tk.HORIZONTAL, label="Iteraciones de Erosión", command=apply_erosion_and_display)
erosion_scrollbar.set(0)
erosion_scrollbar.pack(pady=5)


kernel1_btn = tk.Button(right_frame, text="Aplicar Kernel 1", command=apply_kernel1_and_display)
kernel1_btn.pack(pady=5)

kernel2_btn = tk.Button(right_frame, text="Aplicar Kernel 2", command=apply_kernel2_and_display)
kernel2_btn.pack(pady=5)

kernel3_btn = tk.Button(right_frame, text="Aplicar Kernel 3", command=apply_kernel3_and_display)
kernel3_btn.pack(pady=5)

random_kernel_btn = tk.Button(right_frame, text="Aplicar Kernel Aleatorio", command=apply_random_kernel_and_display)
random_kernel_btn.pack(pady=5)

panel = tk.Label(left_frame)
panel.pack(padx=10, pady=10)

load_btn1 = tk.Button(right_frame, text="Cargar Imagen 1", command=load_image1)
load_btn1.pack(pady=5)

load_btn2 = tk.Button(right_frame, text="Cargar Imagen 2", command=load_image2)
load_btn2.pack(pady=5)

info_label = tk.Label(right_frame, text="Suma y Resta de imagenes", font=('Helvetica', 12))
info_label.pack(pady=5)

alpha1_label = tk.Label(right_frame, text="Alpha 1")
alpha1_label.pack(pady=5)
alpha1_entry = tk.Entry(right_frame)
alpha1_entry.pack(pady=5)

alpha2_label = tk.Label(right_frame, text="Alpha 2")
alpha2_label.pack(pady=5)
alpha2_entry = tk.Entry(right_frame)
alpha2_entry.pack(pady=5)

sum_btn = tk.Button(right_frame, text="Sumar Imágenes", command=lambda: sumar_imagenes_and_display(float(alpha1_entry.get()), float(alpha2_entry.get())))
sum_btn.pack(pady=5)

rest_btn = tk.Button(right_frame, text="Restar Imágenes", command=lambda: restar_imagenes_and_display(float(alpha1_entry.get()), float(alpha2_entry.get())))
rest_btn.pack(pady=5)

fourier_btn = tk.Button(right_frame, text="Aplicar Fourier", command=apply_fourier_and_display)
fourier_btn.pack(pady=5)

convolution_btn = tk.Button(right_frame, text="Aplicar Convolución", command=apply_convolution_and_display)
convolution_btn.pack(pady=5)

edge_detection_btn = tk.Button(right_frame, text="Detectar Bordes", command=edge_detection_and_display_main)
edge_detection_btn.pack(pady=5)

detect_objects_btn = tk.Button(right_frame, text="Detectar Objetos", command=detect_objects_callback)
detect_objects_btn.pack(pady=5)

win.bind('<s>', take_snapshot)
win.mainloop()

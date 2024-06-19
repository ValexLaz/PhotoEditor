import tkinter as tk
from filtros.transformaciones import rotate_image, custom_transform_1, custom_transform_2, custom_transform_3, custom_transform_4
from ..main import current_img, update_image_display
def apply_transformation(transformation_func, *args):
    global current_img, update_image_display
    if current_img is not None:
        transformed_image = transformation_func(current_img, *args)
        current_img = transformed_image
        update_image_display(current_img)

def create_transform_buttons(frame):
    global current_img, update_image_display

    rotate_btn_90 = tk.Button(frame, text="Rotar 90°", command=lambda: apply_transformation(rotate_image, 90))
    rotate_btn_90.pack(pady=5)

    rotate_btn_180 = tk.Button(frame, text="Rotar 180°", command=lambda: apply_transformation(rotate_image, 180))
    rotate_btn_180.pack(pady=5)

    transform_btn_1 = tk.Button(frame, text="Transformación 1", command=lambda: apply_transformation(custom_transform_1))
    transform_btn_1.pack(pady=5)

    transform_btn_2 = tk.Button(frame, text="Transformación 2", command=lambda: apply_transformation(custom_transform_2))
    transform_btn_2.pack(pady=5)

    transform_btn_3 = tk.Button(frame, text="Transformación 3", command=lambda: apply_transformation(custom_transform_3))
    transform_btn_3.pack(pady=5)

    transform_btn_4 = tk.Button(frame, text="Transformación 4", command=lambda: apply_transformation(custom_transform_4))
    transform_btn_4.pack(pady=5)

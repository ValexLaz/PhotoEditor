import tkinter as tk
from transformaciones import rotate_image, custom_transform_1, custom_transform_2, custom_transform_3, custom_transform_4

def create_transform_buttons(frame, globals_dict):
    global img, img_rgb, current_img, original_img, update_image_display

    update_image_display = globals_dict["update_image_display"]

    rotate_btn_90 = tk.Button(frame, text="Rotar 90°", command=lambda: apply_function(rotate_image, 90))
    rotate_btn_90.pack(pady=5)

    rotate_btn_180 = tk.Button(frame, text="Rotar 180°", command=lambda: apply_function(rotate_image, 180))
    rotate_btn_180.pack(pady=5)

    transform_btn_1 = tk.Button(frame, text="Transformación 1", command=lambda: apply_function(custom_transform_1))
    transform_btn_1.pack(pady=5)

    transform_btn_2 = tk.Button(frame, text="Transformación 2", command=lambda: apply_function(custom_transform_2))
    transform_btn_2.pack(pady=5)

    transform_btn_3 = tk.Button(frame, text="Transformación 3", command=lambda: apply_function(custom_transform_3))
    transform_btn_3.pack(pady=5)

    transform_btn_4 = tk.Button(frame, text="Transformación 4", command=lambda: apply_function(custom_transform_4))
    transform_btn_4.pack(pady=5)

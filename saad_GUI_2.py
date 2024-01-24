import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def arnold_map(img, iterations):
    height, width = img.shape
    shuffled_img = np.zeros_like(img)

    for i in range(iterations):
        for x in range(height):
            for y in range(width):
                x_new = (2 * x + y) % height
                y_new = (x + y) % width
                shuffled_img[x_new, y_new] = img[x, y]
        img = shuffled_img.copy()

    return shuffled_img


def inverse_arnold_map(img, iterations):
    height, width = img.shape
    square_img = np.zeros_like(img)

    for i in range(iterations):
        for x in range(height):
            for y in range(width):
                x_new = (x - y) % height
                y_new = (-x + 2 * y) % width
                square_img[x_new, y_new] = img[x, y]
        img = square_img.copy()

    return square_img


def open_image():
    global original_img
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    original_img = cv2.imread(img_path, 0)
    cv2.imshow("Original", original_img)
    cv2.waitKey(0)
    messagebox.showinfo("Image Loaded", "Image has been loaded successfully.")


def encrypt_image():
    global original_img
    global encrypted_img
    iterations = 5

    if original_img is None:
        messagebox.showwarning("Error", "Please load an image first.")
        return

    encrypted_img = arnold_map(original_img, iterations)
    cv2.imshow("Encrypted", encrypted_img)
    cv2.waitKey(0)
    messagebox.showinfo("Encryption Complete", "Image encryption has been completed.")


def decrypt_image():
    global original_img
    global encrypted_img
    global decrypted_img
    iterations = 5

    if encrypted_img is None:
        messagebox.showwarning("Error", "Please encrypt an image first.")
        return

    decrypted_img = inverse_arnold_map(encrypted_img, iterations)
    cv2.imshow("Decrypted", decrypted_img)
    cv2.waitKey(0)
    messagebox.showinfo("Decryption Complete", "Image decryption has been completed.")


# Create the main window
window = tk.Tk()
window.title("Image Encryption and Decryption")
window.geometry("400x200")

# Set custom fonts
font_title = ("Arial", 16, "bold")
font_button = ("Arial", 12)

# Set colors
bg_color = "#F5F5F5"  # Light gray
btn_color = "#FAA500"  # Orange

# Set window background color
window.configure(bg=bg_color)

# Create title label
lbl_title = tk.Label(window, text="Image Encryption and Decryption", font=font_title, bg=bg_color)
lbl_title.pack(pady=10)

# Create buttons with custom colors and fonts
btn_open = tk.Button(window, text="Open Image", font=font_button, bg=btn_color, command=open_image)
btn_open.pack(pady=5)

btn_encrypt = tk.Button(window, text="Encrypt Image", font=font_button, bg=btn_color, command=encrypt_image)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(window, text="Decrypt Image", font=font_button, bg=btn_color, command=decrypt_image)
btn_decrypt.pack(pady=5)

# Global variables
original_img = None
encrypted_img = None
decrypted_img = None
img_path = ""

# Run the GUI loop
window.mainloop()

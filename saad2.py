import numpy as np
from PIL import Image
import cv2

def arnold_map(img, iterations):
    height, width = img.shape

    max_dim = max(width, height)
    square_img = np.zeros((max_dim, max_dim), dtype=np.uint8)
    
    

    x_offset = (max_dim - width) // 2
    y_offset = (max_dim - height) // 2
    square_img[y_offset:y_offset+height, x_offset:x_offset+width] = img
    
    for i in range(iterations):
        for x in range(max_dim):
            for y in range(max_dim):

                x_new = (2*x + y) % max_dim
                y_new = (x + y) % max_dim
                square_img[x_new, y_new] = square_img[x, y]
        square_img = square_img.copy()
    cropped_img = square_img[y_offset:y_offset+height, x_offset:x_offset+width]
    return square_img


def inverse_arnold_map(img, iterations):
    height, width = img.shape

    max_dim = max(width, height)
    square_img = np.zeros((max_dim, max_dim), dtype=np.uint8)

    x_offset = (max_dim - width) // 2
    y_offset = (max_dim - height) // 2
    square_img[y_offset:y_offset+height, x_offset:x_offset+width] = img

    for i in range(iterations):
        for x in range(max_dim):
            for y in range(max_dim):
                x_new = (x - y) % max_dim
                y_new = (-x + 2*y) % max_dim
                square_img[x_new, y_new] = square_img[x, y]
        square_img = square_img.copy()
    decrypted_img = square_img[y_offset:y_offset+height, x_offset:x_offset+width]
    return square_img




iterations = 5

# Read the image file provided by the user
image_path = "img.jpg"
img = cv2.imread(image_path, 0)  # Load the image in grayscale mode

# Check if the image was successfully loaded
if img is None:
    print("Failed to load the image.")
else:
    print("Original Image:")
    cv2.imshow("Original", img)
    cv2.waitKey(0)

    enc_img = arnold_map(img, iterations)
    print("Encrypted Image:")
    cv2.imshow("Encrypted", enc_img)
    cv2.waitKey(0)

    dec_img = inverse_arnold_map(enc_img, iterations)
    print("Decrypted Image:")
    cv2.imshow("Decrypted", dec_img)
    cv2.waitKey(0)

    # Save the decrypted image
    output_path = input("Enter the output file path for the decrypted image: ")
    cv2.imwrite(output_path, dec_img)

    cv2.destroyAllWindows()
     


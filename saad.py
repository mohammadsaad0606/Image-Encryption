import cv2
import numpy as np

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

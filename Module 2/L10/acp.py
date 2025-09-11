import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 6))
    plt.title(title)
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def apply_edge_detection(image, method="sobel", ksize=3, threshold1=100, threshold2=200):
    """Apply the selected edge detection method."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "sobel":
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
        sobel = cv2.magnitude(sobelx, sobely)
        return cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    elif method == "canny":
        return cv2.Canny(image, threshold1, threshold2)

    elif method == "laplacian":
        return cv2.Laplacian(gray_image, cv2.CV_64F, ksize=ksize).astype(np.uint8)

def apply_median_filter(image, ksize):
    """Apply median filter."""
    return cv2.medianBlur(image, ksize)

def interactive_edge_detection(filepath):
    """Interactive utility for edge detection and filtering."""
    image = cv2.imread(filepath)
    if image is None:
        print("Error: Image not found!")
        return

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            ksize = int(input("Enter kernel size for Sobel (odd number): "))
            result = apply_edge_detection(image, method="sobel", ksize=ksize)
            display_image("Sobel Edge Detection", result)

        elif choice == "2":
            t1 = int(input("Enter lower threshold for Canny: "))
            t2 = int(input("Enter upper threshold for Canny: "))
            result = apply_edge_detection(image, method="canny", threshold1=t1, threshold2=t2)
            display_image("Canny Edge Detection", result)

        elif choice == "3":
            ksize = int(input("Enter kernel size for Laplacian (odd number): "))
            result = apply_edge_detection(image, method="laplacian", ksize=ksize)
            display_image("Laplacian Edge Detection", result)

        elif choice == "4":
            ksize = int(input("Enter kernel size for Gaussian smoothing (odd number): "))
            result = cv2.GaussianBlur(image, (ksize, ksize), 0)
            display_image("Gaussian Smoothed Image", result)

        elif choice == "5":
            ksize = int(input("Enter kernel size for Median filtering (odd number): "))
            result = apply_median_filter(image, ksize)
            display_image("Median Filtered Image", result)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Provide the path to an image file for activity
interactive_edge_detection('example.jpg')

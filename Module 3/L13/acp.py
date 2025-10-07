import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('original_images/example.jpg')

# Step 2: Convert to RGB for displaying with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.show()

# Step 3: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Step 4: Crop the image (assume we want the region from 100:300, 200:400)
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()

# Step 5: Rotate the image by 45 degrees
(h, w) = image.shape[:2]
centre = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(centre, 45.0, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Step 6: Increase brightness by adding 50 to all pixel values
brightness

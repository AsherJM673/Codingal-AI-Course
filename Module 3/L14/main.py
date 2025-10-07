import cv2
import numpy as np

def apply_filter(image, filter_type):
    """Apply the selected color filter as edge detection."""
    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    if filter_type == 'red_id':
        # Red channel to 0
        filtered_image[:, :, 2] = 0  # Red channel is 2
    elif filter_type == 'green_id':
        # Green channel to 0
        filtered_image[:, :, 1] = 0  # Green channel is 1
    elif filter_type == 'blue_id':
        # Blue channel to 0
        filtered_image[:, :, 0] = 0  # Blue channel is 0
    elif filter_type == 'red_inv':
        # Invert Red channel
        filtered_image[:, :, 2] = 255 - filtered_image[:, :, 2]
    elif filter_type == 'green_inv':
        # Invert Green channel
        filtered_image[:, :, 1] = 255 - filtered_image[:, :, 1]
    elif filter_type == 'blue_inv':
        # Invert Blue channel
        filtered_image[:, :, 0] = 255 - filtered_image[:, :, 0]
    elif filter_type == 'canny':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    else:
        print("Invalid filter type! Please use 'r', 'g', 'b', 'ri', 'gi', 'bi', or 'c'.")

    return filtered_image


# Load the image
image_path = 'example.jpg'  # Provide your image path
image = cv2.imread(image_path)

if image is None:
    print('Error: Image not found!')
else:
    filter_type = 'original'  # Default filter type

    print('Press the following keys to apply filters:')
    print("'r' - Red Tint")
    print("'g' - Green Tint")
    print("'b' - Blue Tint")
    print("'ri' - Red Invert")
    print("'gi' - Green Invert")
    print("'bi' - Blue Invert")
    print("'c' - Canny Edge Detection")

    while True:
        filtered_image = apply_filter(image, filter_type)

        # Display the filtered image
        cv2.imshow('Filtered Image', filtered_image)

        # Wait for key press
        key = cv2.waitKey(0) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('r'):
            filter_type = 'red_id'
        elif key == ord('g'):
            filter_type = 'green_id'
        elif key == ord('b'):
            filter_type = 'blue_id'
        elif key == ord('i'):
            filter_type = 'red_inv'
        elif key == ord('j'):
            filter_type = 'green_inv'
        elif key == ord('k'):
            filter_type = 'blue_inv'
        elif key == ord('c'):
            filter_type = 'canny'
        else:
            print('Invalid key! Please try again.')

cv2.destroyAllWindows()

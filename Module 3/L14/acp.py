import cv2
import numpy as np

def apply_filter(image, filter_type):
    """Apply the selected color filter or edge detection."""
    filtered_image = image.copy()
    
    if filter_type == 'red tint':
        filtered_image[..., 1] = 0 # Green channel to 0
        filtered_image[..., 2] = 0 # Blue channel to 0
    elif filter_type == 'green tint':
        filtered_image[..., 0] = 0 # Blue channel to 0
        filtered_image[..., 2] = 0 # Red channel to 0
    elif filter_type == 'blue tint':
        filtered_image[..., 0] = 0 # Green channel to 0
        filtered_image[..., 1] = 0 # Red channel to 0
    elif filter_type == 'sobel':
        # Apply Sobel edge detection
        sobelx = cv2.Sobel(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = cv2.sqrt(cv2.add(cv2.abs(sobelx), cv2.abs(sobely).astype('uint8')))
        combined = cv2.cvtColor(sobel_combined.astype(np.uint8), cv2.COLOR_GRAY2BGR)
        filtered_image = combined
    elif filter_type == 'canny':
        edges = cv2.Canny(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    return filtered_image

# Load the image
image_path = 'example.jpg' # Provide your image path
image = cv2.imread(image_path)

if image is None:
    print('Error: Image not found!')
    exit()

filter_type = 'original' # Default filter type

print('Press the following keys to apply filters:')
print('r - Red Tint')
print('g - Green Tint')
print('b - Blue Tint')
print('s - Sobel (Edge Detection)')
print('c - Canny (Edge Detection)')
print('q - Quit')

while True:
    # Apply the selected filter
    filtered_image = apply_filter(image, filter_type)
    
    # Display the filtered image
    cv2.imshow('Filtered Image', filtered_image)
    
    # Wait for key
    key = cv2.waitKey(0) & 0xff
    
    # Key map for selecting filters
    if key == ord('r'):
        filter_type = 'red tint'
    elif key == ord('g'):
        filter_type = 'green tint'
    elif key == ord('b'):
        filter_type = 'blue tint'
    elif key == ord('s'):
        filter_type = 'sobel'
    elif key == ord('c'):
        filter_type = 'canny'
    elif key == ord('q'):
        break
    else:
        print('Invalid key! Please use "r", "g", "b", "s", "c", or "q".')

cv2.destroyAllWindows()

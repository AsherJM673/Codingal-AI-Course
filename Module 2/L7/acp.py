import cv2

# Define the image path
input_image_path = "example.jpg"  # Replace with your image filename

# Load the image
image = cv2.imread(input_image_path)
if image is None:
    print("Error: Could not load image.")
    exit()

# Predefined sizes: (width, height)
sizes = [(640, 480), (320, 240), (160, 120)]

for idx, (w, h) in enumerate(sizes):
    resized = cv2.resize(image, (w, h))
    window_name = f"Resized {w}x{h}"
    
    # Display the resized image
    cv2.imshow(window_name, resized)
    cv2.waitKey(0)  # Wait for key press

    # Save the resized image
    output_filename = f"resized_{w}x{h}.jpg"
    cv2.imwrite(output_filename, resized)
    print(f"Saved {output_filename}")

cv2.destroyAllWindows()

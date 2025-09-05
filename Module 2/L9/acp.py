import cv2

# Load the image
image = cv2.imread('youtube.png')
if image is None:
    raise FileNotFoundError("Could not find 'youtube.png'.")

# Get image dimensions
height, width, _ = image.shape

# Define line and text position
y_pos = height // 2  # Middle of the image vertically

# Draw bi-directional arrow
cv2.arrowedLine(image, (0, y_pos), (width, y_pos), (0, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image, (width, y_pos), (0, y_pos), (0, 255, 0), 3, tipLength=0.05)

# Annotate width
text = f"Width: {width} px"
font = cv2.FONT_HERSHEY_SIMPLEX
text_size = cv2.getTextSize(text, font, 1, 2)[0]
text_x = (width - text_size[0]) // 2
text_y = y_pos - 10
cv2.putText(image, text, (text_x, text_y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Save or display the result
cv2.imwrite('annotated_image.jpg', image)
# cv2.imshow("Width Annotation", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

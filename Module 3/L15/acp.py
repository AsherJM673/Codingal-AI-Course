import cv2
import numpy as np

# Set up webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initial shape position and size
shape_x, shape_y, shape_size = 200, 200, 50

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Convert to HSV for color filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for skin color in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask to detect skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Apply the mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours (hand shape) in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, draw them
    if contours:
        # Get largest contour
        cnt = max(contours, key=cv2.contourArea)
        if cv2.contourArea(cnt) > 500:  # filter small regions
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Get the center of the hand for further tracking or interaction
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # Red dot at center

            # Move shape based on hand's position
            shape_x = center_x
            shape_y = center_y

    # Draw a shape (circle) on the screen that moves with the hand
    cv2.circle(frame, (shape_x, shape_y), shape_size, (0, 82, 255), -1)

    # Display the original frame and the detected hand
    cv2.imshow("Hand Tracker", frame)
    cv2.imshow("Filtered Frame", result)

    # Exit when 'q' or 'Esc' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

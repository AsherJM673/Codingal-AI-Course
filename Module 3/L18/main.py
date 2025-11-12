import cv2
import numpy as np
import time


filters = [None, 'GREYSCALE', 'SEPIA', 'NEGATIVE', 'BLUR']
current_filter = 0


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

last_action_time = 0
debounce_time = 1

def apply_filter(frame, filter_type):
    if filter_type == 'GreyScale':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'SEPIA':
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, sepia_filter)
        return np.clip(sepia_frame, 0, 255).astype(np.uint8)
    elif filter_type == 'NEGATIVE':
            return cv2.bitwise_not(frame)
    elif filter_type == 'BLUR':
         return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame  

while True:
     ret, frame = cap.read()
     if not ret:
          break
     
     fram = cv2.flip(frame, 1)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray, (35, 35), 0)
     _, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
     countours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if countours:
    max_contour = max(countours, key=lambda x: cv2.contourArea(x))
    if cv2.contourArea(max_contour) > 10000:
        hull = cv2.convexHull(max_contour)
        cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)
        hull_area = cv2.contourArea(hull)
        contour_area = cv2.contourArea(max_contour)
        ratio = contour_area / hull_area if hull_area != 0 else 0
        current_time = time.time()
        if ratio > 0.75 and current_time - last_action_time > debounce_time:
            cv2.putText(frame, "Picture Captured!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imwrite(f"gesture_capture_{int(time.time())}.jpg", frame)
            last_action_time = current_time
        elif 0.4 < ratio < 0.7 and current_time - last_action_time > debounce_time:
            current_filter = (current_filter + 1) % len(filters)
            last_action_time = current_time
            print(f"Switched to filter: {filters[current_filter]}")

filtered_img = apply_filter(frame, filters[current_filter])
if filters[current_filter] == 'GRAYSCALE':
    cv2.imshow("Gesture-Controlled Photo App", cv2.cvtColor(filtered_img, cv2.COLOR_GRAY2BGR))
else:
    cv2.imshow("Gesture-Controlled Photo App", filtered_img)

if cv2.waitKey(1) & 0xFF == ord('q'):

    cap.release()
cv2.destroyAllWindows()


import cv2 
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
pyautogui.FAILSAFE = False 
scroll_speed = 100

print("Hand Gesture Scrolling Started (Press 'q' to exit)")

while True:
    ret, frame = cap.read()
    if not ret:
        print("ERROR: Camera is not corking!")
        break
    
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 30, 60], dtype=np.uint8)
    upper_skin = np.array([20, 150, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=lambda x: cv2.contourArea(x))
        if cv2.contourArea(max_contour) > 4000:
            hull = cv2.convexHull(max_contour)
            cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)

            hull_area = cv2.contourArea(hull)
            contour_area = cv2.contourArea(max_contour)

            if contour_area > 0:
                ratio = hull_area / contour_area 

                if ratio > 1.7:
                 pyautogui.scroll(scroll_speed)
                 cv2.putText(frame, "Scroll Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

                elif ratio < 1.3:
                 pyautogui.scroll(-scroll_speed)
                 cv2.putText(frame, "Scroll Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                else:
                
                   cv2.putText(frame, "Neutral", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 3)
    cv2.imshow("Hand Gesture Scroll Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
                   
                
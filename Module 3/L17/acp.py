import cv2
import mediapipe as mp
import pyautogui
import time


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
prev_y = None
scroll_inertia = 0
last_scroll_time = time.time()

def smooth_scroll(delta, last):
    now = time.time()
    if now - last > 0.03:  
        pyautogui.scroll(int(delta))
        return now
    return last

def get_landmark_y(landmarks, idx, frame_shape):
    h, w, _ = frame_shape
    return int(landmarks.landmark[idx].y * h)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    index_y = None
    thumb_y = None

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        
        mp_drawing.draw_landmarks(
            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        
        index_y = get_landmark_y(hand_landmarks, mp_hands.HandLandmark.INDEX_FINGER_TIP, frame.shape)
        thumb_y = get_landmark_y(hand_landmarks, mp_hands.HandLandmark.THUMB_TIP, frame.shape)

        
        pinch_dist = abs(index_y - thumb_y)
        pinch = pinch_dist < 40  

        if pinch:
            
            if prev_y is not None:
                delta = prev_y - index_y
                
                scroll_inertia = 0.7 * scroll_inertia + 0.3 * delta * 2  
                last_scroll_time = smooth_scroll(scroll_inertia, last_scroll_time)
            prev_y = index_y
        else:
            prev_y = None
            scroll_inertia *= 0.7  

    cv2.putText(frame, "Pinch Index+Thumb & Move Hand Up/Down to Scroll", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow('Gesture Scroll', frame)
    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()

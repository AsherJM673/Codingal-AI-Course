import cv2
import mediapipe as mp
import numpy as np

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Pycaw init for volume control
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    vol_range = volume.GetVolumeRange()
    min_vol = vol_range[0]
    max_vol = vol_range[1]
except Exception as e:
    print(f"Error initializing Pycaw: {e}")
    exit()

# Webcam setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from webcam.")
        break

    img = cv2.flip(img, 1)  # Flip the image for a mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_handedness.classification[0].label  # 'Left' or 'Right'
            hand_landmarks_list = hand_landmarks.landmark
            connections = mp_hands.HAND_CONNECTIONS

            # Get tip of the thumb and index finger
            thumb_tip = hand_landmarks_list[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks_list[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            thumb_pos = (int(thumb_tip.x * img.shape[1]), int(thumb_tip.y * img.shape[0]))
            index_pos = (int(index_tip.x * img.shape[1]), int(index_tip.y * img.shape[0]))

            cv2.circle(img, thumb_pos, 15, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 15, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (255, 0, 0), 3)

            length = hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)

            # Control label = mp_handedness (e.g., control volume with right hand)
            hand_label = f"{label} hand"
            if label == "Right":
                new_vol = np.interp(length, [0.03, 0.30], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(new_vol, None)

    cv2.imshow("Hand Gesture Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Pycaw init for volume control
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    vol_range = volume.GetVolumeRange()
    min_vol = vol_range[0]
    max_vol = vol_range[1]
except Exception as e:
    print(f"Error initializing Pycaw: {e}")
    exit()

# Webcam setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from webcam.")
        break

    img = cv2.flip(img, 1)  # Flip the image for a mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_handedness.classification[0].label  # 'Left' or 'Right'
            hand_landmarks_list = hand_landmarks.landmark
            connections = mp_hands.HAND_CONNECTIONS

            # Get tip of the thumb and index finger
            thumb_tip = hand_landmarks_list[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks_list[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            thumb_pos = (int(thumb_tip.x * img.shape[1]), int(thumb_tip.y * img.shape[0]))
            index_pos = (int(index_tip.x * img.shape[1]), int(index_tip.y * img.shape[0]))

            cv2.circle(img, thumb_pos, 15, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 15, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (255, 0, 0), 3)

            length = hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)

            # Control label = mp_handedness (e.g., control volume with right hand)
            hand_label = f"{label} hand"
            if label == "Right":
                new_vol = np.interp(length, [0.03, 0.30], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(new_vol, None)

    cv2.imshow("Hand Gesture Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

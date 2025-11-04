import cv2
import numpy as np

from utils import AutoInitUtils, initializeLandmarks
from sample import test_list, all
import controller.signal_control as sc

# Initialize hand tracking
max_num_hands = 2
min_detection_confidence = 0.5
min_tracking_confidence = 0.7

# Prepare hand controller
ctr = sc.HandController()

cap = cv2.VideoCapture(0)

def auto_init():
    ctr.auto_init_sc(hand=ctr.HAND_RIGHT)
    if not ctr.hand_sc.init_success:
        print("Initialization could not access the webcam.")
        return False
    return True

while True:
    ret, img = cap.read()
    if not ret:
        print("Image could not be read from webcam.")
        break

    img = cv2.flip(img, 1)  # Flip the image for a mirror effect
    results = ctr.hand_sc.multi_hand_process(img)
    if results.multi_hand_landmarks and ctr.hand_sc.multi_handedness:
        # Mark the tip of the thumb hand index
        hand_lms = results.multi_hand_landmarks[ctr.hand_sc.hand_index[0]]
        hand_label = ctr.hand_sc.multi_handedness[ctr.hand_sc.hand_index[0]].classification[0].label
        thumb_tip = sc.get_landmark_idx('THUMB_TIP')
        thumb_x = int(hand_lms.landmark[thumb_tip].x * img.shape[1])
        thumb_y = int(hand_lms.landmark[thumb_tip].y * img.shape[0])

        # Draw circle at the tip
        cv2.circle(img, (thumb_x, thumb_y), 10, (0, 255, 0), -1)
        controlling_thumb_pos = (thumb_x, thumb_y)

        # Calculate the distance between thumb and index finger
        thumb_ip_idx = sc.get_landmark_idx('THUMB_IP')
        thumb_ip_x = int(hand_lms.landmark[thumb_ip_idx].x * img.shape[1])
        thumb_ip_y = int(hand_lms.landmark[thumb_ip_idx].y * img.shape[0])
        dist = np.sqrt((thumb_x - thumb_ip_x)**2 + (thumb_y - thumb_ip_y)**2)

        # If thumb label = 'Right', control values with the right hand
        if hand_label == 'Right':
            ctr.update_signal_state('signal', dist, hand_label)
            print("Hand {} controlling signal state, dist: {}".format(hand_label, dist))
            cv2.putText(img, "Signal: {:.2f}".format(dist), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)

        elif hand_label == 'Left':
            ctr.update_signal_state('bright', dist, hand_label)
            print("Hand {} controlling brightness, dist: {}".format(hand_label, dist))
            cv2.putText(img, "Brightness: {:.2f}".format(dist), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
        
        # original landmarks for brightness
        orig_landmarks = [sc.get_landmark_idx(x) for x in ['THUMB_TIP', 'THUMB_IP']]
        for orig_idx in orig_landmarks:
            orig_x = int(hand_lms.landmark[orig_idx].x * img.shape[1])
            orig_y = int(hand_lms.landmark[orig_idx].y * img.shape[0])
            cv2.circle(img, (orig_x, orig_y), 10, (0,255,120), 2)

    # Show the video feed with annotations
    cv2.imshow('Webcam View with Brightness Controller', img)

    # Release the webcam and close all windows
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()

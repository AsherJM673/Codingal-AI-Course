from deepface import DeepFace
import cv2

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)

    # Analyze the face (age, gender, emotion)
    try:
        result = DeepFace.analyze(frame, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        info = result[0]

        # Show info on screen
        text = f"{info['dominant_emotion']} | {info['gender']} | Age: {info['age']}"
        cv2.putText(frame, text, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    except:
        cv2.putText(frame, "No face detected", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Face Analyzer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

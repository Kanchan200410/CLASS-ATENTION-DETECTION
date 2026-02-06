import cv2
from utils.camera import start_camera, read_frame, stop_camera
from utils.face_detector import detect_face_landmarks
from utils.attention_logic import check_attention

cap = start_camera()

while True:
    frame = read_frame(cap)
    if frame is None:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = detect_face_landmarks(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            status, color = check_attention(face_landmarks, w)

            cv2.putText(
                frame,
                status,
                (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                color,
                3
            )

    cv2.imshow("Student Attention System", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

stop_camera(cap)

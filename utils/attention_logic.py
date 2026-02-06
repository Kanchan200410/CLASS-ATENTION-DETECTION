def check_attention(face_landmarks, frame_width):
    # Nose landmark index = 1
    nose = face_landmarks.landmark[1]
    nose_x = int(nose.x * frame_width)

    if nose_x < frame_width * 0.35 or nose_x > frame_width * 0.65:
        return "NOT ATTENTIVE", (0, 0, 255)
    else:
        return "ATTENTIVE", (0, 255, 0)

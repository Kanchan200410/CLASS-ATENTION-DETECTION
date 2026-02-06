import cv2

def start_camera():
    cap = cv2.VideoCapture(0)
    return cap

def read_frame(cap):
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.flip(frame, 1)
    return frame

def stop_camera(cap):
    cap.release()
    cv2.destroyAllWindows()

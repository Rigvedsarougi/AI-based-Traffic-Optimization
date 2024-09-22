import cv2
import numpy as np

def get_camera_feed(video_source=0):
    cap = cv2.VideoCapture(video_source)
    return cap

def detect_vehicles(frame):
    detected_vehicles = np.random.randint(0, 10)  
    return detected_vehicles

if __name__ == "__main__":
    cap = get_camera_feed()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        vehicle_count = detect_vehicles(frame)
        print(f"Detected {vehicle_count} vehicles")
        cv2.imshow('Traffic Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

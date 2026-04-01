import cv2
from src.config import VIDEO_PATH
from src.detection.pose_detector import PoseDetector
from src.logic.pushup_counter import PushupCounter
from src.visualization.draw import draw_counter

def main():
    cap = cv2.VideoCapture(VIDEO_PATH)

    detector = PoseDetector()
    counter = PushupCounter()
    
    # frame_skip = 5
    # frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Frame Skipping
        # frame_count += 1
        # if frame_count % frame_skip != 0:
        #     continue

        frame = cv2.resize(frame, (640, 480))
        
        timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))

        result = detector.process(frame, timestamp_ms)

        if result.pose_landmarks:
            landmarks = result.pose_landmarks[0]

            angle, count = counter.update(landmarks)

            detector.draw(frame, result)
            draw_counter(frame, count)

        cv2.imshow("Push-up Counter", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
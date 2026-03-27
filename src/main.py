import cv2
from src.config import VIDEO_PATH
from src.detection.pose_detector import PoseDetector
from src.logic.pushup_counter import PushupCounter
from src.visualization.draw import draw_counter

def main():
    cap = cv2.VideoCapture(VIDEO_PATH)

    detector = PoseDetector()
    counter = PushupCounter()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        result = detector.process(frame)

        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark

            angle, count = counter.update(
                landmarks,
                detector.mp_pose
            )

            detector.draw(frame, result)
            draw_counter(frame, count)

        cv2.imshow("Push-up Counter", frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
from src.utils.angle import calculate_angle
from src.config import ANGLE_DOWN_THRESHOLD, ANGLE_UP_THRESHOLD

class PushupCounter:
    def __init__(self):
        self.counter = 0
        self.stage = None

    def update(self, landmarks):
        # MediaPipe landmark indices
        # Left side
        shoulder = [landmarks[11].x, landmarks[11].y]
        elbow    = [landmarks[13].x, landmarks[13].y]
        wrist    = [landmarks[15].x, landmarks[15].y]

        angle = calculate_angle(shoulder, elbow, wrist)

        if angle < ANGLE_DOWN_THRESHOLD:
            self.stage = "down"

        if angle > ANGLE_UP_THRESHOLD and self.stage == "down":
            self.stage = "up"
            self.counter += 1
            print(self.counter)

        return angle, self.counter
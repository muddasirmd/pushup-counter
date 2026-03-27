from src.utils.angle import calculate_angle
from src.config import ANGLE_DOWN_THRESHOLD, ANGLE_UP_THRESHOLD

class PushupCounter:
    def __init__(self):
        self.counter = 0
        self.stage = None

    def update(self, landmarks, mp_pose):
        shoulder = [
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
        ]

        elbow = [
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
        ]

        wrist = [
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
        ]

        angle = calculate_angle(shoulder, elbow, wrist)

        if angle < ANGLE_DOWN_THRESHOLD:
            self.stage = "down"

        if angle > ANGLE_UP_THRESHOLD and self.stage == "down":
            self.stage = "up"
            self.counter += 1

        return angle, self.counter
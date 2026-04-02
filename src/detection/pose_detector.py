import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from src.config import MODEL_PATH

class PoseDetector:
    def __init__(self, model_path=MODEL_PATH):
        BaseOptions = python.BaseOptions
        PoseLandmarker = vision.PoseLandmarker
        PoseLandmarkerOptions = vision.PoseLandmarkerOptions
        VisionRunningMode = vision.RunningMode

        options = PoseLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.VIDEO,
            num_poses=1
        )

        self.detector = PoseLandmarker.create_from_options(options)

    # returns: result.pose_landmarks → list of detected body joints
    def process(self, frame, timestamp_ms):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

        result = self.detector.detect_for_video(mp_image, timestamp_ms)
        return result

    def draw(self, frame, result):
        if not result.pose_landmarks:
            return frame

        for pose_landmarks in result.pose_landmarks:
            for landmark in pose_landmarks:
                h, w, _ = frame.shape
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

        return frame
import cv2

def draw_counter(frame, counter):
    cv2.putText(
        frame,
        f'Push-ups: {counter}',
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
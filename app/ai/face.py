import cv2
import numpy as np
import math
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh


def detect_head_direction(landmarks, frame_shape):

    h, w = frame_shape[:2]

    image_points = np.array([
        (landmarks.landmark[1].x * w, landmarks.landmark[1].y * h),
        (landmarks.landmark[152].x * w, landmarks.landmark[152].y * h),
        (landmarks.landmark[33].x * w, landmarks.landmark[33].y * h),
        (landmarks.landmark[263].x * w, landmarks.landmark[263].y * h),
        (landmarks.landmark[61].x * w, landmarks.landmark[61].y * h),
        (landmarks.landmark[291].x * w, landmarks.landmark[291].y * h),
    ], dtype=np.float64)

    model_points = np.array([
        (0.0, 0.0, 0.0),
        (0.0, -63.6, -12.5),
        (-43.3, 32.7, -26.0),
        (43.3, 32.7, -26.0),
        (-28.9, -28.9, -24.1),
        (28.9, -28.9, -24.1),
    ])

    focal_length = w
    center = (w / 2, h / 2)

    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype=np.float64)

    dist_coeffs = np.zeros((4, 1))

    success, rotation_vector, translation_vector = cv2.solvePnP(
        model_points,
        image_points,
        camera_matrix,
        dist_coeffs,
        flags=cv2.SOLVEPNP_ITERATIVE
    )

    if not success:
        return "Center", "Center", 0.0, 0.0, 0.0

    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    projection_matrix = np.hstack((rotation_matrix, translation_vector))
    _, _, _, _, _, _, euler = cv2.decomposeProjectionMatrix(projection_matrix)

    pitch = float(euler[0])
    yaw = float(euler[1])
    roll = float(euler[2])

    if yaw < -15:
        horizontal = "Left"
    elif yaw > 15:
        horizontal = "Right"
    else:
        horizontal = "Center"

    if pitch < -15:
        vertical = "Up"
    elif pitch > 15:
        vertical = "Down"
    else:
        vertical = "Center"

    return horizontal, vertical, yaw, pitch, roll


def calculate_eye_contact(horizontal_history):

    center = horizontal_history.count("Center")

    if len(horizontal_history) == 0:
        return 0

    return round(
        center / len(horizontal_history) * 100,
        2
    )


def analyze_face(video_path):

    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(str(video_path))

    total_frames = 0
    detected_frames = 0

    horizontal_history = []
    vertical_history = []

    while True:

        success, frame = cap.read()

        if not success:
            break

        total_frames += 1

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:

            detected_frames += 1

            landmarks = results.multi_face_landmarks[0]

            horizontal, vertical, yaw, pitch, roll = detect_head_direction(
                landmarks,
                frame.shape
            )

            horizontal_history.append(horizontal)
            vertical_history.append(vertical)

    cap.release()
    face_mesh.close()

    face_percentage = 0

    if total_frames:

        face_percentage = round(
            detected_frames / total_frames * 100,
            2
        )

    eye_contact = calculate_eye_contact(
        horizontal_history
    )

    print("Horizontal:", {
        "Center": horizontal_history.count("Center"),
        "Left": horizontal_history.count("Left"),
        "Right": horizontal_history.count("Right")
    })

    print("Vertical:", {
        "Center": vertical_history.count("Center"),
        "Up": vertical_history.count("Up"),
        "Down": vertical_history.count("Down")
    })

    return {

        "face_detected": detected_frames,

        "total_frames": total_frames,

        "face_percentage": face_percentage,

        "eye_contact": eye_contact,

        "looking_left": horizontal_history.count("Left"),

        "looking_right": horizontal_history.count("Right"),

        "looking_up": vertical_history.count("Up"),

        "looking_down": vertical_history.count("Down"),

        "confidence": (
            "Excellent"
            if eye_contact >= 90
            else
            "Good"
            if eye_contact >= 75
            else
            "Needs Improvement"
        )

    }
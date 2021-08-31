import numpy as np

from models.landmark import PoseLandmark

landmark_index = {'nose': 0,
                  'left_eye_inner': 1,
                  'left_eye': 2,
                  'left_eye_outer': 3,
                  'right_eye_inner': 4,
                  'right_eye': 5,
                  'right_eye_outer': 6,
                  'left_ear': 7,
                  'right_ear': 8,
                  'mouth_left': 9,
                  'mouth_right': 10,
                  'left_shoulder': 11,
                  'right_shoulder': 12,
                  'left_elbow': 13,
                  'right_elbow': 14,
                  'left_wrist': 15,
                  'right_wrist': 16,
                  'left_pinky_1': 17,
                  'right_pinky_1': 18,
                  'left_index_1': 19,
                  'right_index_1': 20,
                  'left_thumb_2': 21,
                  'right_thumb_2': 22,
                  'left_hip': 23,
                  'right_hip': 24,
                  'left_knee': 25,
                  'right_knee': 26,
                  'left_ankle': 27,
                  'right_ankle': 28,
                  'left_heel': 29,
                  'right_heel': 30,
                  'left_foot_index': 31,
                  'right_foot_index': 32}


def calculate_angle(a, b, c):
    radians = np.arctan2(c.y - b.y, c.x - b.x) - np.arctan2(a.y - b.y, a.x - b.x)
    angle2 = np.abs(radians * 180.0 / np.pi)

    if angle2 > 180.0:
        angle2 = 360 - angle2

    return angle2


def euclidean_distance(a, b):
    return np.sqrt(np.square(a.x - b.x) + np.square(a.y - b.y) + np.square(a.z - b.z))

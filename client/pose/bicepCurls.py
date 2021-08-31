import time

import numpy as np

from pose.exerciseBase import *


class BicepsCurls(Exercise):
    def __init__(self, reps=10):
        super().__init__(reps, "Biceps curls")
        self.start_time = None
        self.is_too_fast = False
        self.start_left_elbow_position = None
        self.start_right_elbow_position = None

    def is_start(self, landmarks):
        angle_left = calculate_angle(landmarks[landmark_index["left_shoulder"]],
                                     landmarks[landmark_index["left_elbow"]],
                                     landmarks[landmark_index["left_wrist"]])

        angle_right = calculate_angle(landmarks[landmark_index["right_shoulder"]],
                                      landmarks[landmark_index["right_elbow"]],
                                      landmarks[landmark_index["right_wrist"]])

        # return angle_right < 80 and angle_right < 80

        if angle_left >= 160 and angle_right >= 160 and landmarks[
            landmark_index["right_wrist"]].y > landmarks[landmark_index["right_elbow"]].y and landmarks[
            landmark_index["left_wrist"]].y > landmarks[landmark_index["left_elbow"]].y:
            if self.start_time != None:
                if time.time() - self.start_time < 1:
                    self.is_too_fast = True
            self.start_time = time.time()

            self.start_left_elbow_position = landmarks[landmark_index["left_elbow"]]
            self.start_right_elbow_position = landmarks[landmark_index["right_elbow"]]
            return True
        return False

    def is_end(self, landmarks):
        angle_left = calculate_angle(landmarks[landmark_index["left_shoulder"]],
                                     landmarks[landmark_index["left_elbow"]],
                                     landmarks[landmark_index["left_wrist"]])

        angle_right = calculate_angle(landmarks[landmark_index["right_shoulder"]],
                                      landmarks[landmark_index["right_elbow"]],
                                      landmarks[landmark_index["right_wrist"]])

        # print(self.compute_percentage_done(angle_left))

        # return angle_left > 150 and angle_right > 150

        return angle_left <= 20 and angle_right <= 20 and landmarks[
            landmark_index["right_wrist"]].y < landmarks[landmark_index["right_elbow"]].y and landmarks[
                   landmark_index["left_wrist"]].y < landmarks[landmark_index["left_elbow"]].y

    def check_errors(self, landmarks):
        if self.is_too_fast:
            self.is_too_fast = False
            self.error = True
            return 0, "You are doing the exercise too fast, slow it down"
        if not self.check_arm_movement(landmarks):
            self.error = True
            return 0, "Move only the forearms keeping the rest of the body fixed"
        return 1, "You are doing good, keep it up"

    def check_arm_movement(self, landmarks):
        if self.start_left_elbow_position is None or self.start_right_elbow_position is None:
            return True

        right_dist = euclidean_distance(landmarks[landmark_index["right_elbow"]], self.start_right_elbow_position)
        left_dist = euclidean_distance(landmarks[landmark_index["left_elbow"]], self.start_left_elbow_position)

        return right_dist < 0.2 and left_dist < 0.2

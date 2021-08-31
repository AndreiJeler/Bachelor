from pose.exerciseBase import *


class Squat(Exercise):
    def __init__(self):
        super().__init__(10, "Squats")
        self.start_left_shoulder_position = None
        self.start_right_shoulder_position = None

    def is_start(self, landmarks):
        angle_left = calculate_angle(landmarks[landmark_index["left_hip"]],
                                     landmarks[landmark_index["left_knee"]],
                                     landmarks[landmark_index["left_ankle"]])

        angle_right = calculate_angle(landmarks[landmark_index["right_hip"]],
                                      landmarks[landmark_index["right_knee"]],
                                      landmarks[landmark_index["right_ankle"]])

        # return angle_right < 80 and angle_right < 80

        if angle_left >= 170 and angle_right >= 170:
            self.start_left_shoulder_position = landmarks[landmark_index["left_shoulder"]]
            self.start_right_shoulder_position = landmarks[landmark_index["right_shoulder"]]
            return True
        return False

    def is_end(self, landmarks):
        angle_left = calculate_angle(landmarks[landmark_index["left_hip"]],
                                     landmarks[landmark_index["left_knee"]],
                                     landmarks[landmark_index["left_ankle"]])

        angle_right = calculate_angle(landmarks[landmark_index["right_hip"]],
                                      landmarks[landmark_index["right_knee"]],
                                      landmarks[landmark_index["right_ankle"]])

        return angle_left <= 100 and angle_right <= 100 and \
               self.is_close_y(landmarks[landmark_index["left_hip"]],
                               landmarks[landmark_index["left_knee"]]) \
               and self.is_close_y(landmarks[landmark_index["right_hip"]],
                                   landmarks[landmark_index["right_knee"]])

    def check_errors(self, landmarks):
        if not self.check_knee_carv(landmarks):
            self.error = True
            return 0, 'Try to keep your legs fixed, do not get the knees close or raise the feet up'
        if not self.check_back_arch(landmarks):
            self.error = True
            return 0, "Try to keep your back straight, do not bend it"
        return 1, "You are doing good, keep it up"

    def check_knee_carv(self, landmarks):
        return euclidean_distance(landmarks[landmark_index["left_knee"]], landmarks[landmark_index["right_knee"]]) > 0.1

    def is_close_y(self, l1, l2):
        return abs(l1.y - l2.y) <= 0.1

    def is_close_z(self, l1, l2):
        return abs(l1.z - l2.z) <= 0.5

    def check_back_arch(self, landmarks):
        if self.start_left_shoulder_position is None or self.start_right_shoulder_position is None:
            return True

        return self.is_close_z(landmarks[landmark_index["right_shoulder"]],
                               self.start_right_shoulder_position) and self.is_close_z(
            landmarks[landmark_index["left_shoulder"]], self.start_right_shoulder_position)

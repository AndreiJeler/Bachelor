from pose.exerciseBase import *


class ShoulderPress(Exercise):
    def __init__(self, reps=10):
        super().__init__(reps, "Shoulder press")

    def is_start(self, landmarks):
        angle_left = calculate_angle(landmarks[landmark_index["left_shoulder"]],
                                     landmarks[landmark_index["left_elbow"]],
                                     landmarks[landmark_index["left_wrist"]])

        angle_right = calculate_angle(landmarks[landmark_index["right_shoulder"]],
                                      landmarks[landmark_index["right_elbow"]],
                                      landmarks[landmark_index["right_wrist"]])

        # return angle_right < 80 and angle_right < 80

        return angle_left <= 80 and angle_right <= 80 and landmarks[
            landmark_index["right_wrist"]].y < landmarks[landmark_index["right_shoulder"]].y and landmarks[
                   landmark_index["left_wrist"]].y < landmarks[landmark_index["left_shoulder"]].y

    def is_end(self, landmarks):
        angle_left = calculate_angle(landmarks[landmark_index["left_shoulder"]],
                                     landmarks[landmark_index["left_elbow"]],
                                     landmarks[landmark_index["left_wrist"]])

        angle_right = calculate_angle(landmarks[landmark_index["right_shoulder"]],
                                      landmarks[landmark_index["right_elbow"]],
                                      landmarks[landmark_index["right_wrist"]])

        # print(self.compute_percentage_done(angle_left))

        # return angle_left > 150 and angle_right > 150

        return angle_left >= 165 and angle_right >= 165 and landmarks[
            landmark_index["right_elbow"]].y < landmarks[landmark_index["right_shoulder"]].y and landmarks[
                   landmark_index["left_elbow"]].y < landmarks[landmark_index["left_shoulder"]].y

    def compute_percentage_done(self, angle):
        return np.interp(angle, (80, 160), (0, 100))

    def check_errors(self, landmarks):
        if not self.check_extension(landmarks):
            self.error = True
            return 0, "Try to keep your wrists(hands) right above the elbows"
        return 1, "You are doing good, keep it up"

    def check_extension(self, landmarks):
        return self.get_dist_x(landmarks[landmark_index["right_wrist"]],
                               landmarks[landmark_index["right_elbow"]]) < 0.15 \
               and self.get_dist_x(landmarks[landmark_index["left_wrist"]],
                                   landmarks[landmark_index["left_elbow"]]) < 0.15

    def get_dist_x(self, l1, l2):
        return abs(l1.x - l2.x)

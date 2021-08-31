import mediapipe as mp
import cv2
from utilities.poseUtils import *


class Exercise:
    def __init__(self, max_reps, exercise_name):
        self._reps = 0
        self.good_reps = 0
        self._mistakes = []
        self._max_reps = max_reps
        self._exercise_name = exercise_name
        self._current_stage = None
        self.error = False

    def set_reps(self, reps):
        self._max_reps = reps

    def check_rep(self, landmarks):
        if self._current_stage == None:
            if self.is_start(landmarks):
                self._current_stage = "start"
        elif self._current_stage == "start":
            if self.is_end(landmarks):
                self._current_stage = "end"
        elif self._current_stage == "end":
            if self.is_start(landmarks):
                self._current_stage = "start"
                self._reps += 1
                if not self.error:
                    self.good_reps += 1
                self.error = False
        return self._current_stage, self._reps

    def is_start(self, landmarks):
        pass

    def is_end(self, landmarks):
        pass

    def check_errors(self, landmarks):
        pass

    def is_done(self):
        return self._reps >= self._max_reps

    def reset_vals(self):
        pass

    def get_reps(self):
        return self._reps

    def run(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            cv2.destroyAllWindows()
            cap = cv2.VideoCapture("good-20.mp4")
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark

                    calculate_angle(landmarks[landmark_index["left_shoulder"]], landmarks[landmark_index["left_elbow"]],
                                    landmarks[landmark_index["left_wrist"]])
                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow(self._exercise_name, image)

                if cv2.waitKey(10) & 0xFF == ord('q') | self._reps >= self._max_reps:
                    break

            cap.release()
            cv2.destroyAllWindows()

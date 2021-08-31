from pose.exerciseBase import Exercise
import os
import tensorflow as tf
import numpy


class ExerciseNeuralNetwork(Exercise):
    def __init__(self, max_reps, exercise_name, correctness_model_location, reps_model_location, exercise_model):
        super().__init__(max_reps, exercise_name)
        self.correctness_path = correctness_model_location
        self.reps_path = reps_model_location
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

        self.reps_model = tf.keras.models.load_model(reps_model_location)
        self.correctness_model = tf.keras.models.load_model(correctness_model_location)
        self.previous_frames = []
        self.current_frame = 0
        self.exercise_model = exercise_model

    def check_repetition_status_ml(self, landmarks):
        self.current_frame += 1
        if self.current_frame % 5 != 0:
            return self._current_stage

        if self.exercise_model.name != "Squats":
            landmarks = landmarks[:25]

        row = list(numpy.array(
            [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in
             landmarks]).flatten())
        row = numpy.array(row).reshape(1, len(landmarks) * 4)

        predict = self.reps_model.predict(row)
        final_predict = numpy.argmax(predict)

        state = self.exercise_model.reps_labels[str(final_predict)]
        return state

    def make_correctness_check(self, landmarks):
        try:
            if self.exercise_model.name != "Squats":
                landmarks = landmarks[:25]

            row = list(numpy.array(
                [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in
                 landmarks]).flatten())
            row = row[36:]
            nr_landmarks = 64

            if self.exercise_model.name == "Squats":
                row = row[:16] + row[56:]
                nr_landmarks = 56

            self.previous_frames.append(row)

            if len(self.previous_frames) == 10:
                predict = self.correctness_model.predict(numpy.array(self.previous_frames).reshape(1, 10, nr_landmarks))
                final_predict = numpy.argmax(predict)
                form_name = self.exercise_model.correctness_labels[str(final_predict)]

                self.previous_frames.pop(0)
                self.previous_frames.pop(0)
                self.previous_frames.pop(0)
                self.previous_frames.pop(0)
                self.previous_frames.pop(0)

                return form_name, final_predict

            return None, None
        except Exception as ex:
            print("Correctness check error: " + str(ex))

    def check_errors(self, landmarks):
        try:
            form_name, pred_id = self.make_correctness_check(landmarks)
            if form_name is None:
                return 2, "No prediction made"
            if form_name is not "good":
                self.error = True
            return 1 if form_name == "good" else 0, self.exercise_model.correctness_explanations[str(pred_id)]
        except Exception as ex:
            print("Correctness check error: " + str(ex))

    def check_rep(self, landmarks):
        new_state = self.check_repetition_status_ml(landmarks)
        if self._current_stage == None:
            if new_state == "start":
                self._current_stage = "start"
        elif self._current_stage == "start":
            if new_state == "end":
                self._current_stage = "end"
        elif self._current_stage == "end":
            if new_state == "start":
                self._current_stage = "start"
                self._reps += 1
                if not self.error:
                    self.good_reps += 1
                self.error = False
        return self._current_stage, self._reps

    def reset_vals(self):
        self.previous_frames = []
        self.current_frame = 0

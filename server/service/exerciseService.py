import json

from Data.exercise import Exercise


class ExerciseService:
    @staticmethod
    def get_all():
        exercises_json = []
        exercises = Exercise.objects()
        for e in exercises:
            exercises_json.append(
                {"id": str(e.id), "name": e.name, "body_region": e.body_region, "difficulty": e.difficulty,
                 "reps_labels": e.reps_labels, "correctness_labels": e.correctness_labels,
                 "reps_explanations": e.reps_explanations,
                 "correctness_explanations": e.correctness_explanations})
        return json.dumps(exercises_json)

    @staticmethod
    def get_picture(id):
        try:
            exercise = Exercise.objects(id=id).get()
            return exercise.icon_location
        except Exception:
            raise Exception("No exercise with given id!")

    @staticmethod
    def get_start_picture(id):
        try:
            exercise = Exercise.objects(id=id).get()
            return exercise.start_picture
        except Exception:
            raise Exception("No exercise with given id!")

    @staticmethod
    def get_end_picture(id):
        try:
            exercise = Exercise.objects(id=id).get()
            return exercise.end_picture
        except Exception:
            raise Exception("No exercise with given id!")

    @staticmethod
    def get_exercise(id):
        try:
            exercise = Exercise.objects(id=id).get()
            return exercise
        except Exception:
            raise Exception("No exercise with given id!")

    @staticmethod
    def get_reps_model(id):
        try:
            exercise = Exercise.objects(id=id).get()
            return exercise.reps_model_location
        except Exception:
            raise Exception("No exercise with given id!")

    @staticmethod
    def get_correctness_model(id):
        try:
            exercise = Exercise.objects(id=id).get()
            return exercise.correctness_model_location
        except Exception:
            raise Exception("No exercise with given id!")

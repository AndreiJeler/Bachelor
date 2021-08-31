import json

from Data.activity import Activity
from Data.exercise import Exercise
from Data.set import Set


class ActivityService:
    @staticmethod
    def get_history_exercise(user, exercise_id):
        history_json = []
        if exercise_id == '-1':
            activities = Activity.objects(user=user).order_by('-date')
        else:
            try:
                exercise = Exercise.objects(id=exercise_id).get()
            except Exception:
                raise Exception("No exercise with this id!")
            activities = Activity.objects(user=user, exercise=exercise).order_by('-date')
        for act in activities:
            sets_json = []
            for set in act.sets:
                sets_json.append(
                    {"id": str(set.id), "nr_reps": set.nr_reps, "seconds": set.seconds, "good_reps": set.good_reps,
                     "details": set.details})
            history_json.append(
                {"id": str(act.id), "exercise_name": act.exercise.name, "sets": sets_json, "date": act.date})
        return json.dumps(history_json, default=str)

    @staticmethod
    def add_new_activity(exercise, user, date, sets):
        activity = Activity(exercise=exercise, user=user)
        activity.save()
        for s in sets:
            set = Set(nr_reps=s["nr_reps"], good_reps=s["good_reps"], seconds=s["seconds"], details=s["details"],
                      activity=activity)
            set.save()
            activity.sets.append(set)
        activity.save()
        return activity

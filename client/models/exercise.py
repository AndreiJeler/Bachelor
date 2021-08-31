import json


class ExerciseModel:
    def __init__(self, id, name, body_region, difficulty, reps_labels, reps_explanations, correctness_labels,
                 correctness_explanations, pic="resources/profile.png", start_pic="resources/profile.png",
                 end_pic="resources/profile.png", correctness_model="/", reps_model="/"):
        self.name = name
        self.body_region = body_region
        self.difficulty = difficulty
        self.id = id
        self.pic = pic
        self.start_pic = start_pic
        self.end_pic = end_pic
        self.reps_explanations = reps_explanations
        self.reps_labels = reps_labels
        self.correctness_labels = correctness_labels
        self.correctness_explanations = correctness_explanations
        self.correctness_model = correctness_model
        self.reps_model = reps_model

    def to_net_json(self):
        temp_dict = {"Id": self.id, "Name": self.name, "Difficulty": self.difficulty, "EndPic": self.end_pic,
                     "StartPic": self.start_pic, "BodyRegion": self.body_region, "Pic": self.pic,
                     "CorrectnessLabels": str(self.correctness_labels),
                     "CorrectnessExplanations": str(self.correctness_explanations), "RepsLabels": str(self.reps_labels),
                     "RepsExplanations": str(self.reps_explanations),
                     "RepsModel": self.reps_model, "CorrectnessModel": self.correctness_model}

        return json.dumps(temp_dict, default=str)

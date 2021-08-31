class SetActivity:
    def __init__(self, reps, good_reps, sec, details):
        self.reps = reps
        self.good_reps = good_reps
        self.sec = sec
        self.details = details

    def to_json_format(self):
        return {"nr_reps": self.reps, "good_reps": self.good_reps, "seconds": self.sec, "details": self.details}

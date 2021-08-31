import time


class Activity:
    def __init__(self, e_id):
        self.date = time.time()
        self.e_id = e_id
        self.sets = []

    def to_json_format(self):
        return {"date": self.date, "e_id": self.e_id, "sets": [set.to_json_format() for set in self.sets]}

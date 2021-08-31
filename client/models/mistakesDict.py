class MistakesDictionary:
    def __init__(self):
        self.mistakes = {}

    def check_rep(self, rep):
        return rep in self.mistakes.keys()

    def add_mistake(self, rep, mistake):
        if not self.check_rep(rep):
            self.mistakes[rep] = mistake
            return True
        return False

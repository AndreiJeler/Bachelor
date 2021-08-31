import mongoengine


class Exercise(mongoengine.Document):
    name = mongoengine.StringField(required=True, unique=True)
    body_region = mongoengine.StringField()
    correctness_model_location = mongoengine.StringField(default="")
    reps_model_location = mongoengine.StringField(default="")
    model_version = mongoengine.IntField(default=1)
    difficulty = mongoengine.StringField(default="Easy")
    icon_location = mongoengine.StringField(default="")
    correctness_labels = mongoengine.StringField()
    correctness_explanations = mongoengine.StringField()
    reps_labels = mongoengine.StringField()
    reps_explanations = mongoengine.StringField()
    start_picture = mongoengine.StringField()
    end_picture = mongoengine.StringField()

    meta = {
        'db_alias': 'bachelor',
        'collection': 'exercises'
    }

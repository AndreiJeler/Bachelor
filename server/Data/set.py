import mongoengine



class Set(mongoengine.Document):
    nr_reps = mongoengine.IntField(default=0)
    good_reps = mongoengine.IntField(default=0)
    seconds = mongoengine.FloatField()
    activity = mongoengine.ReferenceField("Activity")
    details = mongoengine.StringField(default="")

    meta = {
        'db_alias': 'bachelor',
        'collection': 'sets'
    }

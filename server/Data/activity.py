import datetime
import mongoengine


class Activity(mongoengine.Document):
    exercise = mongoengine.ReferenceField('Exercise')
    sets = mongoengine.ListField(mongoengine.ReferenceField('Set'))
    date = mongoengine.DateTimeField(default=datetime.datetime.now())
    user = mongoengine.ReferenceField('User')

    meta = {
        'db_alias': 'bachelor',
        'collection': 'activities'
    }

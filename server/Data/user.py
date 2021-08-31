import mongoengine


class User(mongoengine.Document):
    email = mongoengine.EmailField(max_length=50, required=True, unique=True)
    name = mongoengine.StringField(max_length=50, required=True)
    password = mongoengine.StringField(max_length=1000, required=True)
    isActivated = mongoengine.BooleanField(required=True)
    profile = mongoengine.StringField(default="resources/images/profile.png")

    activities = mongoengine.ListField(mongoengine.ReferenceField('Activity'))

    meta = {
        'db_alias': 'bachelor',
        'collection': 'users'
    }

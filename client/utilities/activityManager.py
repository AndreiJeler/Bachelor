import json

from clients.httpSingleton import HTTPSingleton
from models.activity import Activity


class ActivityManager:
    __instance__ = None

    def __init__(self, e_id):
        ActivityManager.__instance__ = Activity(e_id)

    @staticmethod
    def create_activity(e_id):
        ActivityManager(e_id)

    @staticmethod
    def add_set(set):
        ActivityManager.__instance__.sets.append(set)

    @staticmethod
    def get_activity():
        return ActivityManager.__instance__

    @staticmethod
    def post_activity():
        HTTPSingleton.__activity_client__.save_activity(ActivityManager.__instance__.to_json_format())
        ActivityManager.__instance__ = None

    @staticmethod
    def reset():
        ActivityManager.__instance__ = None

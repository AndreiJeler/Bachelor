from clients.activityClient import ActvitiyClient
from clients.exerciseClient import ExerciseClient
from clients.userClient import UserClient


class HTTPSingleton:
    __user_client__: UserClient = None
    __is_instanced__ = False
    __exercise_client__: ExerciseClient = None
    __activity_client__: ActvitiyClient = None

    def __init__(self, env_file=None):
        if HTTPSingleton.__is_instanced__ is False:
            HTTPSingleton.__is_instanced__ = True
            HTTPSingleton.__user_client__ = UserClient()
            HTTPSingleton.__exercise_client__ = ExerciseClient()
            HTTPSingleton.__activity_client__ = ActvitiyClient()
        else:
            raise Exception("Instance was already initialized")

    @staticmethod
    def get_user_client():
        if HTTPSingleton.__is_instanced__ is False:
            HTTPSingleton()
        return HTTPSingleton.__user_client__

    @staticmethod
    def get_exercise_client():
        if HTTPSingleton.__is_instanced__ is False:
            HTTPSingleton()
        return HTTPSingleton.__exercise_client__

    @staticmethod
    def get_activity_client():
        if HTTPSingleton.__is_instanced__ is False:
            HTTPSingleton()
        return HTTPSingleton.__activity_client__

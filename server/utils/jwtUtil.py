import datetime

from env.environmentSingleton import EnvironmentSingleton
import jwt


class JWTUtils:
    def __init__(self):
        self.__secret = EnvironmentSingleton.get_instance()["SECRET"]

    def encode_token(self, id, username):
        return jwt.encode(self.get_jwt_payload(id, username), self.__secret)

    def decode_token(self, token):
        return jwt.decode(token, self.__secret, algorithms=["HS256"])

    def get_jwt_payload(self, id, username):
        return {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow(),
            "id": str(id),
            "email": username
        }

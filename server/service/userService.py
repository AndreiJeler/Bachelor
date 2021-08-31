from service.emailService import EmailService
from utils.jwtUtil import JWTUtils
from utils.passwordHashing import PasswordHashing
from Data.user import User
from random import randint


class UserService:
    def __init__(self, jwt):
        self.__jwt_utils: JWTUtils = jwt

    def get_user(self, email):
        try:
            user = User.objects(email=email).get()
            return user
        except Exception as ex:
            raise Exception("No user with this email!")

    def add_user(self, email, password, name):
        try:
            user = User(email=email, password=str(PasswordHashing.hash_password(password, email)), isActivated=True,
                        name=name)
            user.save()
        except Exception as ex:
            raise Exception(f"{ex}")

    def login(self, email, password):
        try:
            user = User.objects(email=email).get()
            if str(user.password) != str(PasswordHashing.hash_password(password, email)):
                raise Exception("Password not good")
            return self.__jwt_utils.encode_token(user.id, user.email)
        except Exception as ex:
            raise Exception("Email or/and password are invalid")

    def decode_token(self, token):
        try:
            user_dict = self.__jwt_utils.decode_token(token)
            user = User.objects(id=user_dict["id"]).get()
            return user
        except Exception:
            raise Exception("Invalid token, user not authenticated")

    def get_pic_path(self, id):
        try:
            user = User.objects(id=id).get()
            return user.profile
        except Exception:
            raise Exception("No user with this id!")

    def change_password(self, user, current, new_pass):
        user_pass = user.password
        current = PasswordHashing.hash_password(current, user.email)
        if str(user_pass) != str(current):
            raise Exception("The current password is incorrect!")
        user.password = str(PasswordHashing.hash_password(new_pass, user.email))
        user.save()

    def password_forgotten(self, email):
        user = self.get_user(email)
        new_pass = str(randint(10000000, 99999999))
        user.password = str(PasswordHashing.hash_password(new_pass, user.email))
        user.save()
        EmailService.send_temp_password(email, new_pass)

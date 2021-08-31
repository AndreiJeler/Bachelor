import json
import time

import mongoengine

from service.activityService import ActivityService
from env.environmentSingleton import EnvironmentSingleton
from service.exerciseService import ExerciseService

import mimetypes
import os

from utils.dtoConverter import DTOConverter
from env.servicesSingleton import *
import flask
from flask import jsonify, request, send_file


class Server:
    def __init__(self):
        self.__user_service: UserService = ServicesSingleton.get_user_service()

    def start_server(self):
        app = flask.Flask(__name__, static_url_path='')
        app.config["DEBUG"] = True

        @app.route('/', methods=['GET'])
        def home():
            return "<h1>Hmmmm... It seems that you found me!</h1>"

        @app.route('/api/v1/user/login', methods=['GET'])
        def login():
            email = request.json.get('email')
            password = request.json.get('password')
            try:
                token = self.__user_service.login(email, password)
                return {"token": token}
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route('/api/v1/user/forgot-password', methods=['PUT'])
        def forgot_password():
            email = request.json.get('email')
            try:
                self.__user_service.password_forgotten(email)
                return {"OK": "Password was reseted. The password was sent via email!"}
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route('/api/v1/user/decode', methods=['GET'])
        def decode_user():
            req = request
            token = request.json.get('token')
            try:
                user = self.__user_service.decode_token(token)
                return DTOConverter.convert_to_userDto(user)
            except Exception as ex:
                return {"error": str(ex)}, 401

        @app.route('/api/v1/user/register', methods=['POST'])
        def register():
            email = request.json.get('email')
            password = request.json.get('password')
            name = request.json.get('name')
            try:
                self.__user_service.add_user(email, password, name)
            except Exception as ex:
                return {"error": str(ex)}, 501
            return {"ok": "OK"}

        @app.route('/api/v1/user/profile/<id>', methods=['GET'])
        def get_user_profile_picture(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                path = self.__user_service.get_pic_path(id)
                path = os.path.join(root_dir(), path)
                _, extension = os.path.splitext(path)
                return send_file(path, mimetype=mimetypes.types_map[extension])
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route('/api/v1/user/change-password', methods=['PUT'])
        def change_user_password():
            try:
                token = request.headers.get('Authorization').split(' ')[-1]
            except Exception as ex:
                return {"error": "Please login"}, 401
            try:
                user = self.__user_service.decode_token(token)
            except Exception as ex:
                return {"error": str(ex)}, 401

            current_pass = request.json.get('pass')
            new_pass = request.json.get('new-pass')

            try:
                self.__user_service.change_password(user, current_pass, new_pass)
                return {"OK": "OK"}, 200
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route('/api/v1/exercises', methods=['GET'])
        def get_all_exercises():
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                return ExerciseService.get_all()
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route("/api/v1/exercises/image/<id>", methods=["GET"])
        def get_exercise_image(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                path = ExerciseService.get_picture(id)
                path = os.path.join(root_dir(), path)
                _, extension = os.path.splitext(path)
                return send_file(path, mimetype=mimetypes.types_map[extension])
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route("/api/v1/exercises/start-image/<id>", methods=["GET"])
        def get_start_image(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                path = ExerciseService.get_start_picture(id)
                path = os.path.join(root_dir(), path)
                _, extension = os.path.splitext(path)
                return send_file(path, mimetype=mimetypes.types_map[extension])
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route("/api/v1/exercises/end-image/<id>", methods=["GET"])
        def get_end_image(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                path = ExerciseService.get_end_picture(id)
                path = os.path.join(root_dir(), path)
                _, extension = os.path.splitext(path)
                return send_file(path, mimetype=mimetypes.types_map[extension])
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route("/api/v1/exercises/reps-model/<id>", methods=["GET"])
        def get_reps_model(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                path = ExerciseService.get_reps_model(id)
                path = os.path.join(root_dir(), path)
                _, extension = os.path.splitext(path)
                return send_file(path)
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route("/api/v1/exercises/correctness-model/<id>", methods=["GET"])
        def get_correctness_model(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                path = ExerciseService.get_correctness_model(id)
                path = os.path.join(root_dir(), path)
                _, extension = os.path.splitext(path)
                return send_file(path)
            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route("/api/v1/activities", methods=["POST"])
        def add_activity():
            try:
                # date = request.json.get("date")
                sets = request.json.get("sets")
                exercise_id = request.json.get("e_id")

                date = time.time()
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401

                user = self.__user_service.decode_token(token)
                exercise = ExerciseService.get_exercise(exercise_id)

                activity = ActivityService.add_new_activity(exercise, user, date, sets)

                return {"OK": str(activity.id)}, 200

            except Exception as ex:
                return {"error": str(ex)}, 501

        @app.route('/api/v1/activities/history/<id>', methods=['GET'])
        def get_history_exercise(id):
            try:
                try:
                    token = request.headers.get('Authorization').split(' ')[-1]
                except Exception as ex:
                    return {"error": "Please login"}, 401
                try:
                    user = self.__user_service.decode_token(token)
                except Exception as ex:
                    return {"error": str(ex)}, 401

                return ActivityService.get_history_exercise(user, id)
            except Exception as ex:
                return {"error": str(ex)}, 501

        def root_dir():  # pragma: no cover
            return os.path.abspath(os.path.dirname(__file__))

        app.run()


def global_init(host_url):
    mongoengine.register_connection(host=host_url,
                                    alias='bachelor', name='bachelor')


if __name__ == '__main__':
    environmentSingleton = EnvironmentSingleton("env/.env")
    ServicesSingleton()
    global_init(environmentSingleton.get_instance()["MONGO_URL"])
    server = Server()
    server.start_server()
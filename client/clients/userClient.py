import json

from env.envSingleton import EnvSingleton
from clients.httpClient import HTTPClient
from models.user import User


class UserClient:
    def __init__(self):
        self.API_URL = 'http://127.0.0.1:5000/api/v1/user'

    def login(self, email, password):
        payload = {'email': email, 'password': password}
        res = HTTPClient.make_get(f"{self.API_URL}/login", payload)
        if res is dict and res.keys().__contains__("error"):
            raise Exception(res["error"])
        res_text: dict = json.loads(res.text)
        if res_text.keys().__contains__("error"):
            return res_text
        token = res_text["token"]
        EnvSingleton.set_token(token)
        return res_text

    def forgot_password(self, email):
        payload = {"email": email}
        res = HTTPClient.make_put(f"{self.API_URL}/forgot-password", payload=payload)
        if res is dict and res.keys().__contains__("error"):
            raise Exception(res["error"])
        res_text: dict = json.loads(res.text)
        return res_text

    def decode_token(self, token):
        payload = {'token': token}
        res = HTTPClient.make_get(f"{self.API_URL}/decode", payload)
        if res is dict and res.keys().__contains__("error"):
            raise Exception(res["error"])
        if res.status_code == 401:
            raise Exception(res["error"])
        user = json.loads(res.text)
        user = User(user["id"], user["email"], user["name"])
        return user

    def register(self, email, password, name):
        payload = {'email': email, 'password': password, 'name': name}
        response = HTTPClient.make_post(f"{self.API_URL}/register", payload)
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        return json.loads(response.text)

    def get_profile_pic(self, id):
        response = HTTPClient.make_get(f"{self.API_URL}/profile/" + id,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        filename = "resources/" + response.headers["Content-Disposition"].split('=')[-1]
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename

    def change_password(self, current, new):
        payload = {"pass": current, "new-pass": new}
        response = HTTPClient.make_put(f"{self.API_URL}/change-password", payload,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        if response.text:
            response = json.loads(response.text)
            if response.keys().__contains__('error'):
                raise Exception(response["error"])

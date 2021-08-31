import json

from env.envSingleton import EnvSingleton
from clients.httpClient import HTTPClient


class ActvitiyClient:
    def __init__(self):
        self.API_URL = 'http://127.0.0.1:5000/api/v1/activities'

    def get_history_exercise(self, id):
        res = HTTPClient.make_get(f"{self.API_URL}/history/" + id,
                                  headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if res is dict and res.keys().__contains__("error"):
            raise Exception(res["error"])
        res_text = json.loads(res.text)
        if res_text is dict and res_text.keys().__contains__("error"):
            raise Exception(res_text["error"])
        return res_text

    def save_activity(self, activity):
        res = HTTPClient.make_post(f"{self.API_URL}", payload=activity,
                                   headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if res is dict and res.keys().__contains__("error"):
            raise Exception(res["error"])
        res_text = json.loads(res.text)
        if res_text is dict and res_text.keys().__contains__("error"):
            raise Exception(res_text["error"])
        return res_text

import json

from env.envSingleton import EnvSingleton
from models.exercise import ExerciseModel
from clients.httpClient import HTTPClient


class ExerciseClient:
    def __init__(self):
        self.API_URL = 'http://127.0.0.1:5000/api/v1/exercises'

    def get_all(self):
        res = HTTPClient.make_get(f"{self.API_URL}", headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if res is dict and res.keys().__contains__("error"):
            raise Exception(res["error"])
        res_text = json.loads(res.text)
        if res_text is dict and res_text.keys().__contains__("error"):
            raise Exception(res_text["error"])
        exercises = []
        for e in res_text:
            exercises.append(
                ExerciseModel(e["id"], e["name"], e["body_region"], e["difficulty"], json.loads(e["reps_labels"]),
                              json.loads(e["reps_explanations"]), json.loads(e["correctness_labels"]),
                              json.loads(e["correctness_explanations"])))
        return exercises

    def get_icon(self, id):
        response = HTTPClient.make_get(f"{self.API_URL}/image/" + id,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        filename = "resources/exercises/" + response.headers["Content-Disposition"].split('=')[-1]
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename

    def get_start_pic(self, id):
        response = HTTPClient.make_get(f"{self.API_URL}/start-image/" + id,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        filename = "resources/exercises/" + response.headers["Content-Disposition"].split('=')[-1]
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename

    def get_end_pic(self, id):
        response = HTTPClient.make_get(f"{self.API_URL}/end-image/" + id,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        filename = "resources/exercises/" + response.headers["Content-Disposition"].split('=')[-1]
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename

    def get_reps_model(self, id):
        response = HTTPClient.make_get(f"{self.API_URL}/reps-model/" + id,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        filename = "resources/exercises/" + response.headers["Content-Disposition"].split('=')[-1]
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename

    def get_correctness_model(self, id):
        response = HTTPClient.make_get(f"{self.API_URL}/correctness-model/" + id,
                                       headers={'Authorization': 'Bearer ' + EnvSingleton.get_token()})
        if response is dict and response.keys().__contains__("error"):
            raise Exception(response["error"])
        filename = "resources/exercises/" + response.headers["Content-Disposition"].split('=')[-1]
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        return filename

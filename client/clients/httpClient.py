import requests

from utilities.utils import Utils


class HTTPClient:
    __is_connected__ = True

    @staticmethod
    def make_get(url, payload=None, headers=None):
        if not HTTPClient.__is_connected__:
            return
        if headers is None:
            headers = {}
        if payload is None:
            payload = {}
        try:
            return requests.get(url, json=payload, headers=headers)
        except (requests.ConnectionError, requests.Timeout):
            Utils.showdialog("No connection to the server. The app will run in offline mode.")
            HTTPClient.__is_connected__ = False
            return {"error": "Cannot connect to server"}

    @staticmethod
    def make_put(url, payload=None, headers=None):
        if not HTTPClient.__is_connected__:
            return
        if payload is None:
            payload = {}
        if headers is None:
            headers = {}
        try:
            return requests.put(url, json=payload, headers=headers)
        except (requests.ConnectionError, requests.Timeout):
            Utils.showdialog("No connection to the server. The app will run in offline mode.")
            HTTPClient.__is_connected__ = False
            return {"error": "Cannot connect to server"}

    @staticmethod
    def make_post(url, payload=None, headers=None):
        if not HTTPClient.__is_connected__:
            return
        if headers is None:
            headers = {}
        if payload is None:
            payload = {}
        try:
            return requests.post(url, json=payload, headers=headers)
        except (requests.ConnectionError, requests.Timeout):
            Utils.showdialog("No connection to the server. The app will run in offline mode.")
            HTTPClient.__is_connected__ = False
            return {"error": "Cannot connect to server"}

    @staticmethod
    def check_connection(url):
        timeout = 3
        try:
            _ = requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            return False

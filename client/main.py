import json
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

from env.envSingleton import EnvSingleton
from env.config import ConfigSingleton
from clients.httpClient import HTTPClient
from clients.httpSingleton import HTTPSingleton
from GUI.mainmenu import MainMenu
from GUI.login import LoginForm
from env.userSingleton import UserSingleton
from utilities.constants import SERVER_URL


def check_login():
    token = EnvSingleton.get_token()
    if not token:
        return False
    try:
        user = HTTPSingleton.get_user_client().decode_token(token)
        UserSingleton.set_instance(user)
        ConfigSingleton.set_user(user, ConfigSingleton.get_image())
        return True
    except Exception as ex:
        UserSingleton.set_instance(None)
        showdialog("Session expired! Please login back")
        return False


def showdialog(text):
    msg = QMessageBox()
    msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    # msg.setIcon(QMessageBox.Information)

    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)

    retval = msg.exec_()


if __name__ == '__main__':
    # HTTPSingleton.get_user_client().decode_token(EnvSingleton.get_token())

    # if not HTTPClient.check_connection(SERVER_URL):
    #     showdialog("No connection to the server. The app will run in offline mode.")

    if check_login():
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = MainMenu()
        ui.setupUi(MainWindow)
        MainWindow.show()
        app.exec_()
    else:
        app = QtWidgets.QApplication(sys.argv)
        form = QtWidgets.QMainWindow()
        login_ui = LoginForm()
        login_ui.setupUi(form)
        form.show()
        app.exec_()

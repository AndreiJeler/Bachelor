from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

from pose.bicepCurls import BicepsCurls
from pose.shoulderPress import ShoulderPress
from pose.squat import Squat


class Utils:

    @staticmethod
    def create_class(exercise_name):
        classes = {
            "Squats": Squat(),
            "Shoulder press": ShoulderPress(),
            "Biceps Curls": BicepsCurls()
        }
        return classes[exercise_name]

    @staticmethod
    def showdialog(text):
        msg = QMessageBox()
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # msg.setIcon(QMessageBox.Information)

        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

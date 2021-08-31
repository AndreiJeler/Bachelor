import json
import os

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from clients.httpSingleton import HTTPSingleton
from models.exercise import ExerciseModel
from pose.exerciseBase import Exercise
from pose.exerciseML import ExerciseNeuralNetwork
from GUI.exercise_ui import ExerciseUI
from utilities.utils import Utils


class SelectMenu(object):
    def setupUi(self, Form, exercise):
        Form.setObjectName("Form")
        Form.resize(800, 414)
        Form.setStyleSheet("background-color: #222831; color: #eeeeee; font-size:20px;")
        Form.setWindowFilePath("")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Form = Form
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(Form)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setStyleSheet("QFrame{background-color: #222831;}\n"
                                  "QPushButton{border-radius:5px;}\n"
                                  "QPushButton:hover{background-color: #00adb5;}")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(50, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exercise_name = QtWidgets.QLabel(self.header)
        self.exercise_name.setObjectName("exercise_name")
        self.horizontalLayout.addWidget(self.exercise_name)
        self.close_btn = QtWidgets.QPushButton(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.close_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.close_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QtCore.QSize(25, 25))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header)
        self.body = QtWidgets.QFrame(Form)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image_label = QtWidgets.QLabel(self.body)
        self.image_label.setStyleSheet("")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.image_label.setMaximumSize(319, 353)
        self.image_label.setScaledContents(True)
        self.horizontalLayout_2.addWidget(self.image_label)
        self.frame = QtWidgets.QFrame(self.body)
        self.frame.setStyleSheet("QComboBox{background-color:#393e46;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setContentsMargins(5, 5, 50, 0)
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.diff_label = QtWidgets.QLabel(self.frame)
        self.diff_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.diff_label.setObjectName("diff_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.diff_label)
        self.difficulty = QtWidgets.QLabel(self.frame)
        self.difficulty.setObjectName("difficulty")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.difficulty)
        self.body_label = QtWidgets.QLabel(self.frame)
        self.body_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.body_label.setObjectName("body_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.body_label)
        self.body_part = QtWidgets.QLabel(self.frame)
        self.body_part.setObjectName("body_part")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.body_part)
        self.cmr_label = QtWidgets.QLabel(self.frame)
        self.cmr_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cmr_label.setObjectName("cmr_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cmr_label)
        self.camera_select = QtWidgets.QComboBox(self.frame)
        self.camera_select.setObjectName("camera_select")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.camera_select)
        self.mdl_label = QtWidgets.QLabel(self.frame)
        self.mdl_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mdl_label.setObjectName("mdl_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mdl_label)
        self.model_select = QtWidgets.QComboBox(self.frame)
        self.model_select.setObjectName("model_select")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.model_select)
        self.reps_label = QtWidgets.QLabel(self.frame)
        self.reps_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reps_label.setObjectName("reps_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.reps_label)
        self.reps_select = QtWidgets.QComboBox(self.frame)
        self.reps_select.setObjectName("reps_select")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reps_select)
        self.btn_frame = QtWidgets.QFrame(self.frame)
        self.btn_frame.setMinimumSize(QtCore.QSize(0, 150))
        self.btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frame.setObjectName("btn_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.btn_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_btn = QtWidgets.QPushButton(self.btn_frame)
        self.start_btn.setMinimumSize(QtCore.QSize(200, 75))
        self.start_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.start_btn.setStyleSheet("QPushButton{background-color:#393e46;border-radius:5px;}\n"
                                     "QPushButton:hover{background-color: #00adb5;}")
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout_2.addWidget(self.start_btn, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.btn_frame)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addWidget(self.body)

        self.exercise: ExerciseModel = exercise
        self.exercise_class: Exercise = Utils.create_class(self.exercise.name)
        self.activity_client = HTTPSingleton.get_activity_client()

        self.set_text()

        self.start_btn.clicked.connect(self.start_exercise)
        self.close_btn.clicked.connect(self.Form.close)

        self.video_path = ""
        cv2.destroyAllWindows()

        def move_window(e):
            try:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.Form.move(self.Form.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            except:
                return

        def pressEvent(e):
            self.clickPosition = e.globalPos()

        self.Form.mousePressEvent = pressEvent
        self.header.mouseMoveEvent = move_window

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.set_change_comboboxes()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Select"))
        # self.exercise_name.setText(_translate("Form", "Selected exercise: Squats"))
        self.diff_label.setText(_translate("Form", "Difficulty:"))
        # self.difficulty.setText(_translate("Form", "Hard"))
        self.body_label.setText(_translate("Form", "Body region:"))
        # self.body_part.setText(_translate("Form", "Legs"))
        self.cmr_label.setText(_translate("Form", "Video Input:"))
        self.mdl_label.setText(_translate("Form", "Model:"))
        self.reps_label.setText(_translate("Form", "Reps number:"))
        self.start_btn.setText(_translate("Form", "Start"))

    def set_text(self):
        self.exercise_name.setText("Selected exercise: " + self.exercise.name)
        self.image_label.setPixmap(QtGui.QPixmap(self.exercise.pic))
        self.difficulty.setText(self.exercise.difficulty)
        self.body_part.setText(self.exercise.body_region)
        self.camera_select.addItems(["Webcam", "Kinect", "Select recorded video"])
        self.model_select.addItems(["No model", "NN model"])
        self.reps_select.addItems(["10", "12", "20", "No limit"])

    def set_change_comboboxes(self):
        self.camera_select.currentIndexChanged.connect(self.video_changed)

    def video_changed(self):
        if self.camera_select.currentIndex() == 2:
            self.video_path = self.select_video()[0]
            self.reps_select.setCurrentIndex(3)
            self.reps_select.setVisible(False)
            self.reps_label.setVisible(False)
        else:
            self.video_path = ""
            self.reps_select.setVisible(True)
            self.reps_label.setVisible(True)

        if self.camera_select.currentIndex() == 1:
            self.mdl_label.setVisible(False)
            self.model_select.setVisible(False)
        else:
            self.mdl_label.setVisible(True)
            self.model_select.setVisible(True)

    def start_exercise(self):
        reps = self.reps_select.currentText()
        if reps == "No limit":
            self.exercise_class.set_reps(999)
            reps = 999
        else:
            self.exercise_class.set_reps(int(reps))

        if self.camera_select.currentIndex() == 1:
            json_obj = self.exercise.to_net_json()
            with open("kinect-config.json", "w") as out:
                out.write(json_obj)
            json_obj_2 = json.dumps(
                {"Reps": reps, "IsModelUsed": True if self.model_select.currentIndex() == 1 else False})
            with open("run-config.json", "w") as out_2:
                out_2.write(json_obj_2)
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, "../")
            filename = os.path.join(filename, 'Bachelor-Client/Bachelor-Client/bin/Debug/Bachelor-Client.exe')
            os.system(filename)
            try:
                with open("activity.json", 'r') as inp:
                    temp = inp.readlines()[0]
                    js = json.loads(temp)
                    _ = self.activity_client.save_activity(js)
                os.remove("activity.json")
            except:
                self.Form.close()
                return
            self.Form.close()
            return

        if self.model_select.currentIndex() != 1:
            self.new_mainWindow: QMainWindow = QtWidgets.QMainWindow()
            self.exercise_ui = ExerciseUI()
            self.exercise_ui.setupUi(self.new_mainWindow, self.exercise, self.exercise_class, int(reps),
                                     self.video_path)
            self.Form.close()
            self.new_mainWindow.close()
            cv2.destroyAllWindows()

            # self.new_mainWindow.show()
#            self.Form.close()
        else:
            self.new_mainWindow: QMainWindow = QtWidgets.QMainWindow()
            self.exercise_ui = ExerciseUI()
            self.exercise_class = ExerciseNeuralNetwork(reps, self.exercise.name, self.exercise.correctness_model,
                                                        self.exercise.reps_model, self.exercise)

            self.exercise_ui.setupUi(self.new_mainWindow, self.exercise, self.exercise_class, int(reps),
                                     self.video_path)
            self.Form.close()
            self.new_mainWindow.close()
            cv2.destroyAllWindows()

            # self.new_mainWindow.show()
#            self.Form.close()

    def select_video(self):
        return QFileDialog.getOpenFileName(self.Form, 'Select video',
                                           '', "Video files (*.mp4 *.avi *.gif)")

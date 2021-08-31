import time

import cv2

import imutils
import numpy
from PyQt5 import QtCore, QtWidgets
import mediapipe as mp
import pyshine as ps
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox

from models.mistakesDict import MistakesDictionary
from models.exercise import ExerciseModel
from pose.exerciseBase import Exercise
from utilities.activityManager import ActivityManager
from GUI.set_summary import SetSummary


class ExerciseUI(object):
    def setupUi(self, MainWindow, exercise: ExerciseModel, exercise_class: Exercise, reps=2, video=""):
        ActivityManager.create_activity(exercise.id)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        self.MainWindow: QMainWindow = MainWindow
        self.exercise_name = exercise.name
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #393e46;\n"
                                         "color: #eeeeee;\n"
                                         "font-size:24px;\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exercise_frame = QtWidgets.QFrame(self.centralwidget)
        self.exercise_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exercise_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exercise_frame.setObjectName("exercise_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.exercise_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_frame = QtWidgets.QFrame(self.exercise_frame)
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_label = QtWidgets.QLabel(self.name_frame)
        self.name_label.setStyleSheet("font-size:20px;")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.name_frame)
        self.stream_frame = QtWidgets.QFrame(self.exercise_frame)
        self.stream_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stream_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stream_frame.setObjectName("stream_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stream_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.current_image = QtWidgets.QLabel(self.stream_frame)
        self.current_image.setStyleSheet("")
        self.current_image.setText("")
        self.current_image.setScaledContents(True)
        self.current_image.setObjectName("current_image")
        self.verticalLayout_2.addWidget(self.current_image)
        self.verticalLayout.addWidget(self.stream_frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        self.horizontalLayout.addWidget(self.exercise_frame)
        self.stats_frame = QtWidgets.QFrame(self.centralwidget)
        self.stats_frame.setStyleSheet("")
        self.stats_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stats_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stats_frame.setObjectName("stats_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.stats_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.explanation_frame = QtWidgets.QFrame(self.stats_frame)
        self.explanation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.explanation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.explanation_frame.setObjectName("explanation_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.explanation_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.current_state = QtWidgets.QLabel(self.explanation_frame)
        self.current_state.setObjectName("current_state")
        self.verticalLayout_3.addWidget(self.current_state, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.state_image = QtWidgets.QLabel(self.explanation_frame)
        self.state_image.setText("")
        self.state_image.setScaledContents(True)
        self.state_image.setObjectName("state_image")
        self.verticalLayout_3.addWidget(self.state_image)
        self.explanation_text = QtWidgets.QPlainTextEdit(self.explanation_frame)
        self.explanation_text.setStyleSheet("border:none")
        self.explanation_text.setReadOnly(True)
        self.explanation_text.setObjectName("explanation_text")
        self.verticalLayout_3.addWidget(self.explanation_text)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.addWidget(self.explanation_frame)
        self.frame_3 = QtWidgets.QFrame(self.stats_frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.reps_label = QtWidgets.QLabel(self.frame_3)
        self.reps_label.setObjectName("reps_label")
        self.verticalLayout_4.addWidget(self.reps_label, 0, QtCore.Qt.AlignHCenter)
        self.time_label = QtWidgets.QLabel(self.frame_3)
        self.time_label.setObjectName("time_label")
        self.verticalLayout_4.addWidget(self.time_label, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 15))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.summarry_frame = QtWidgets.QFrame(self.frame_3)
        self.summarry_frame.setStyleSheet("QFrame{border: 0.5px solid #00adb5;} QLabel{border: none;}")
        self.summarry_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.summarry_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.summarry_frame.setObjectName("summarry_frame")
        # self.summarry_frame.setMaximumSize()
        self.summarry_layout = QtWidgets.QVBoxLayout(self.summarry_frame)
        self.summarry_layout.setContentsMargins(0, 0, 0, 0)
        self.summarry_layout.setSpacing(20)
        self.summarry_layout.setObjectName("summarry_layout")

        self.verticalLayout_4.addWidget(self.summarry_frame)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.action_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_btn.sizePolicy().hasHeightForWidth())
        self.action_btn.setSizePolicy(sizePolicy)
        self.action_btn.setStyleSheet("background-color: #222831;")
        self.action_btn.setObjectName("action_btn")
        self.verticalLayout_5.addWidget(self.action_btn)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 7)
        self.verticalLayout_4.setStretch(4, 1)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.stats_frame)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tmp = None
        self.image = None
        self.capture = None

        self.start_time = time.time()
        self.fps_time = time.time()

        self.max_reps = reps

        self.state = None
        self.reps = 0
        self.good_reps = 0
        self.has_started = False
        self.fps = 0

        self.connect_actions()

        self.MainWindow.show()

        self.current_image.setMaximumSize(self.current_image.size())

        self.is_finished = False
        self.exercise = exercise_class
        self.exercise_model: ExerciseModel = exercise

        self.current_rep_label = QLabel("")
        self.current_mistake = QtWidgets.QPlainTextEdit(self.summarry_frame)
        self.current_mistake.setReadOnly(True)
        self.current_mistake.setStyleSheet("border: none;font-size: 18px;")
        self.current_mistake.setFixedHeight(75)
        self.all_mistakes = QtWidgets.QPlainTextEdit(self.summarry_frame)
        self.all_mistakes.setReadOnly(True)
        self.all_mistakes.setMinimumHeight(300)
        # self.all_mistakes.setMaximumHeight(1000)
        self.all_mistakes.setStyleSheet("border: none; font-size:18px; color:red;")
        self.summarry_layout.addWidget(self.current_rep_label)
        self.summarry_layout.addWidget(self.current_mistake)
        self.summarry_layout.addWidget(self.all_mistakes)

        self.summarry_layout.setContentsMargins(3, 10, 0, 0)
        self.summarry_layout.setSpacing(30)

        self.previous_frames = []

        self.mistakes_dict = MistakesDictionary()

        self.is_closed = False
        self.video = video

        if video is "":
            self.start(0)
        else:
            self.start_set()
            self.start(video)

        self.MainWindow.show()

    def connect_actions(self):
        self.action_btn.clicked.connect(self.button_press)

        def closeEvent(event):
            self.is_finished = True
            # self.capture.release()
            cv2.destroyAllWindows()

            if not self.is_closed:
                if self.video != "":
                    self.end_set()
                self.reply = QMessageBox.question(self.MainWindow, 'Save', 'Do you want to save the activity?',
                                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if self.reply == QMessageBox.Yes:
                    ActivityManager.post_activity()
            self.is_closed = True

            # self.MainWindow.close()
            cv2.destroyAllWindows()
            # for i in range(1, 5):
            #     cv2.waitKey(1)
            # time.sleep(3)
            event.accept()

        self.MainWindow.closeEvent = closeEvent

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exercise"))
        self.name_label.setText(_translate("MainWindow", "Current exercise: " + self.exercise_name))
        self.current_state.setText(_translate("MainWindow", "Wait for starting"))
        self.explanation_text.setPlainText(_translate("MainWindow", "Explanations:\nRelaxation time"))
        self.reps_label.setText(_translate("MainWindow", "Number of reps: 0"))
        self.time_label.setText(_translate("MainWindow", "Time Elapsed: 00:00"))
        self.label_3.setText(_translate("MainWindow", "Summary:"))
        self.action_btn.setText(_translate("MainWindow", "Start set"))

    def button_press(self):
        if self.action_btn.text() == "Start set":
            self.start_set()
        else:
            self.end_set()

    def end_set(self):
        self.action_btn.setText("Start set")
        self.has_started = False
        self.reps = 0
        self.good_reps = 0
        elapse = int(time.time() - self.start_time)
        self.start_time = time.time()
        self.state_image.setPixmap(QPixmap())
        self.explanation_text.setPlainText("Explanations:\nRelaxation time")

        self.new_form = QtWidgets.QDialog()
        self.set_summary = SetSummary()
        self.set_summary.setupUi(self.new_form, elapse, self.exercise.get_reps(), self.exercise.good_reps)
        self.new_form.exec_()
        # self.start_wait()

    def start_set(self):
        self.action_btn.setText("End set")
        self.explanation_text.setPlainText("Explanations:\nGet in the starting position")
        self.current_state.setText("Wait for starting position")
        self.start_time = time.time()
        self.state_image.setPixmap(
            QPixmap(self.exercise_model.start_pic).scaled(self.state_image.width(), self.state_image.height()))
        self.has_started = True
        self.current_rep_label.setText("Current repetition is ok")
        self.current_rep_label.setStyleSheet("border:none; color:green;")

    def convert_time(self, seconds):
        minutes = int(seconds / 60)
        seconds = seconds % 60
        if minutes == 0:
            minutes = "00"
        elif minutes < 10:
            minutes = "0" + str(minutes)
        if seconds == 0:
            seconds = "00"
        elif seconds < 10:
            seconds = "0" + str(seconds)
        return str(minutes) + ":" + str(seconds)

    def start(self, capt):
        self.capture = cv2.VideoCapture(capt)
        self.capture.set(3, 640)
        self.capture.set(4, 480)

        cnt = 0
        frames_to_count = 20
        st = 0
        fps = 0

        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        rows = []
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            self.start_time = time.time()
            counter = 0
            while not self.is_finished:
                img, self.image = self.capture.read()
                if not img or self.is_finished:
                    cv2.destroyAllWindows()
                    break

                self.image = imutils.resize(self.image, height=480)
                self.image = imutils.resize(self.image, width=640)

                # Recolor image to RGB
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                self.image.flags.writeable = False

                # Make detection
                results = pose.process(self.image)

                # Recolor back to BGR
                self.image.flags.writeable = True
                self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

                counter += 1
                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark

                    if self.has_started:
                        self.check_rep(landmarks)
                        self.check_error(landmarks)
                        if self.max_reps <= self.reps:
                            self.end_set()

                except Exception as ex:
                    print(str(ex))
                    pass

                # Render detections
                mp_drawing.draw_landmarks(self.image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                if cnt == frames_to_count:
                    try:
                        self.fps = round(frames_to_count / (time.time() - st))

                        st = time.time()
                        cnt = 0
                    except:
                        pass
                cnt += 1

                if not self.is_finished:
                    self.update()
                else:
                    break
                if cv2.waitKey(1) & 0xFF == ord('q') or self.is_finished:
                    break

    def update(self):
        img = self.image

        # Here we add display text to the image
        text = 'FPS: ' + str(self.fps)
        img = ps.putBText(img, text, text_offset_x=20, text_offset_y=30, vspace=20, hspace=10, font_scale=1.0,
                          background_RGB=(10, 20, 222), text_RGB=(255, 255, 255))

        elapse = int(time.time() - self.start_time)

        self.time_label.setText("Time elapsed: " + self.convert_time(elapse))

        self.set_photo(img)

    def set_photo(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.current_image.setPixmap(QPixmap.fromImage(image))

    def check_rep(self, landmarks):
        state, reps = self.exercise.check_rep(landmarks)
        self.check_state(state)

    def check_state(self, state):
        if self.state is None and state == "start":
            self.state = "start"
            self.explanation_text.setPlainText("Explanations:\n" + self.exercise_model.reps_explanations[self.state])
            self.current_state.setText("Current state: Start")
            self.current_rep_label.setText("Current repetition is ok")
            self.current_rep_label.setStyleSheet("border:none; color:green;")
            self.state_image.setPixmap(
                QPixmap(self.exercise_model.end_pic).scaled(self.state_image.width(), self.state_image.height()))
            return
        if self.state == "start" and state == "end":
            self.state = "end"
            self.explanation_text.setPlainText("Explanations:\n" + self.exercise_model.reps_explanations[self.state])
            self.state_image.setPixmap(
                QPixmap(self.exercise_model.start_pic).scaled(self.state_image.width(), self.state_image.height()))
            self.current_state.setText("Current state: End")
            return
        if self.state == "end" and state == "start":
            self.state = "start"
            self.explanation_text.setPlainText("Explanations:\n" + self.exercise_model.reps_explanations[self.state])
            self.state_image.setPixmap(
                QPixmap(self.exercise_model.end_pic).scaled(self.state_image.width(), self.state_image.height()))
            self.current_state.setText("Current state: Start")
            self.reps += 1
            self.reps_label.setText("Number of reps: " + str(self.reps))
            self.current_rep_label.setText("Current repetition is ok")
            self.current_rep_label.setStyleSheet("border:none; color:green;")

    def check_error(self, landmarks):
        code, explanation = self.exercise.check_errors(landmarks)
        if code == 0:
            self.current_mistake.setPlainText(explanation)
            self.current_mistake.setStyleSheet("border:none; color:red; font-size:18px;")
            self.current_rep_label.setText("Current repetition is bad")
            self.current_rep_label.setStyleSheet("border:none;color:red;")
            if self.mistakes_dict.add_mistake(self.reps + 1, explanation):
                self.set_mistakes_text()
        elif code == 1:
            self.current_mistake.setPlainText(explanation)
            self.current_mistake.setStyleSheet("border:none;color:green; font-size:18px;")

    def set_mistakes_text(self):
        text = ""
        for m in self.mistakes_dict.mistakes.keys():
            text += "Rep " + str(m) + ":" + self.mistakes_dict.mistakes[m] + "\n"
        self.all_mistakes.setPlainText(text)

    def set_mistakes_text_slot(self, mistakes):
        text = ""
        for m in mistakes.mistakes.keys():
            text += "Rep " + str(m) + ":" + self.mistakes_dict.mistakes[m] + "\n"
        self.all_mistakes.setPlainText(text)
        print(text)

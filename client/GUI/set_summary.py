from PyQt5 import QtCore, QtGui, QtWidgets

from utilities.activityManager import ActivityManager
from models.set import SetActivity


class SetSummary(object):
    def setupUi(self, Form, seconds, reps, good_reps):
        Form.setObjectName("Form")
        Form.resize(521, 301)
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
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_title = QtWidgets.QLabel(self.header)
        self.header_title.setObjectName("header_title")
        self.horizontalLayout.addWidget(self.header_title)
        self.verticalLayout.addWidget(self.header)
        self.body = QtWidgets.QFrame(Form)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.body)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setContentsMargins(-1, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.seconds_label = QtWidgets.QLabel(self.frame)
        self.seconds_label.setObjectName("seconds_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.seconds_label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.reps_label = QtWidgets.QLabel(self.frame)
        self.reps_label.setObjectName("reps_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reps_label)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.good_reps_label = QtWidgets.QLabel(self.frame)
        self.good_reps_label.setObjectName("good_reps_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.good_reps_label)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.details_edit = QtWidgets.QLineEdit(self.frame)
        self.details_edit.setObjectName("details_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.details_edit)
        self.verticalLayout_2.addWidget(self.frame)
        self.save_btn = QtWidgets.QPushButton(self.body)
        self.save_btn.setMinimumSize(QtCore.QSize(100, 70))
        self.save_btn.setMaximumSize(QtCore.QSize(100, 50))
        self.save_btn.setStyleSheet("QPushButton{background-color:#393e46;border-radius:5px;}\n"
                                    "QPushButton:hover{background-color: #00adb5;}")
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_2.addWidget(self.save_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.setStretch(0, 7)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout.addWidget(self.body)

        self.seconds_label.setText(str(seconds))
        self.reps_label.setText(str(reps))
        self.good_reps_label.setText(str(good_reps))

        self.seconds = seconds
        self.reps = reps
        self.good_reps = good_reps

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.save_btn.clicked.connect(self.save)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header_title.setText(_translate("Form", "Previous set summary:"))
        self.label_1.setText(_translate("Form", "Seconds elapsed:"))
        self.label_2.setText(_translate("Form", "Number of reps:"))
        self.label_5.setText(_translate("Form", "Good reps:"))
        self.label_7.setText(_translate("Form", "Additional details:"))
        self.save_btn.setText(_translate("Form", "Save"))

    def save(self):
        details = self.details_edit.text()
        set = SetActivity(self.reps, self.good_reps, self.seconds, details)
        ActivityManager.add_set(set)
        self.Form.close()

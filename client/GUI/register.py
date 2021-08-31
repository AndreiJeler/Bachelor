import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from utilities.constants import EMAIL_REGEX
from clients.httpSingleton import HTTPSingleton


class RegisterForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 360)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("QPushButton{\n"
                           "background-color: rgba(0, 173, 181, 0.75);\n"
                           "color: #eeeeee;\n"
                           "border-radius: 5px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed{\n"
                           "background-color: rgba(0, 173, 181, 1);\n"
                           "padding-left:5px;\n"
                           "padding-top:5px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "background-color: rgba(0, 173, 181, 1);\n"
                           "}\n"
                           "")
        self.main = QtWidgets.QWidget(Form)
        self.main.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.main.setStyleSheet("font-size: 14px;\n"
                                "")
        self.main.setObjectName("main")
        self.background = QtWidgets.QLabel(self.main)
        self.background.setGeometry(QtCore.QRect(0, 0, 300, 350))
        self.background.setStyleSheet("background-color: #222831;\n"
                                      "border-radius: 15px;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.email_text = QtWidgets.QLineEdit(self.main)
        self.email_text.setGeometry(QtCore.QRect(10, 50, 280, 41))
        self.email_text.setStyleSheet("background-color: #222831;\n"
                                      "color: #eeeeee;\n"
                                      "border: 1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color: #00adb5;\n"
                                      "padding-bottom: 7px;\n"
                                      "")
        self.email_text.setText("")
        self.email_text.setObjectName("email_text")
        self.password_text = QtWidgets.QLineEdit(self.main)
        self.password_text.setGeometry(QtCore.QRect(10, 150, 280, 41))
        self.password_text.setStyleSheet("background-color: #222831;\n"
                                         "color: #eeeeee;\n"
                                         "border: 1px solid rgba(0,0,0,0);\n"
                                         "border-bottom-color: #00adb5;\n"
                                         "padding-bottom: 7px;\n"
                                         "")
        self.password_text.setText("")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.register_btn = QtWidgets.QPushButton(self.main)
        self.register_btn.setGeometry(QtCore.QRect(75, 290, 150, 40))
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_btn.setObjectName("register_btn")
        self.pushButton = QtWidgets.QPushButton(self.main)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 31, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: #222831; color: #00adb5; font-size: 24px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_register)
        self.confirm_password_text = QtWidgets.QLineEdit(self.main)
        self.confirm_password_text.setGeometry(QtCore.QRect(10, 200, 280, 41))
        self.confirm_password_text.setStyleSheet("background-color: #222831;\n"
                                                 "color: #eeeeee;\n"
                                                 "border: 1px solid rgba(0,0,0,0);\n"
                                                 "border-bottom-color: #00adb5;\n"
                                                 "padding-bottom: 7px;\n"
                                                 "")
        self.confirm_password_text.setText("")
        self.confirm_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_text.setObjectName("confirm_password_text")
        self.name_text = QtWidgets.QLineEdit(self.main)
        self.name_text.setGeometry(QtCore.QRect(10, 100, 280, 41))
        self.name_text.setStyleSheet("background-color: #222831;\n"
                                     "color: #eeeeee;\n"
                                     "border: 1px solid rgba(0,0,0,0);\n"
                                     "border-bottom-color: #00adb5;\n"
                                     "padding-bottom: 7px;\n"
                                     "")
        self.name_text.setText("")
        self.name_text.setObjectName("name_text")
        self.error = QtWidgets.QLabel(self.main)
        self.error.setGeometry(QtCore.QRect(0, 250, 300, 20))
        self.error.setStyleSheet("color: red\n""")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")

        self.user_service = HTTPSingleton.get_user_client()
        self.register_btn.clicked.connect(self.make_register)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.form = Form

        def move_window(e):
            try:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.form.move(self.form.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            except:
                return

        def pressEvent(e):
            try:
                self.clickPosition = e.globalPos()
            except:
                return

        self.form.mousePressEvent = pressEvent
        self.form.mouseMoveEvent = move_window

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.email_text.setPlaceholderText(_translate("Form", "Email"))
        self.password_text.setPlaceholderText(_translate("Form", "Password"))
        self.register_btn.setText(_translate("Form", "Register"))
        self.pushButton.setText(_translate("Form", "X"))
        self.confirm_password_text.setPlaceholderText(_translate("Form", "Confirm password"))
        self.name_text.setPlaceholderText(_translate("Form", "Name"))

    def close_register(self):
        from GUI.login import LoginForm
        self.login_form = LoginForm()
        self.login_form.setupUi(self.form)
        self.form.show()

    def make_register(self):
        email = self.email_text.text()
        if not re.search(EMAIL_REGEX, email):
            self.error.setText("Invalid email format")
            return
        password = self.password_text.text()
        confirm_pass = self.confirm_password_text.text()
        if password != confirm_pass:
            self.error.setText("The passwords are not the same")
            return
        name = self.name_text.text()
        res: dict = self.user_service.register(email, password, name)
        if res.keys().__contains__("error"):
            self.error.setText(res['error'])
            return
        self.showdialog("Registered successfully")

    def showdialog(self, text):
        msg = QMessageBox()
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # msg.setIcon(QMessageBox.Information)

        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.close_register)

        retval = msg.exec_()

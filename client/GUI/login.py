import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox
from env.config import ConfigSingleton
from GUI.forgotPassword import ForgotPassword
from clients.httpSingleton import HTTPSingleton
from utilities.constants import EMAIL_REGEX

from GUI.loadingScreen import LoadingScreen
from GUI.register import RegisterForm
from env.userSingleton import UserSingleton


class LoginForm(QWidget):
    def setupUi(self, Form):
        ConfigSingleton.reset_user()
        self.loading = None
        self.user_service = HTTPSingleton.get_user_client()
        Form.setObjectName("Form")
        Form.resize(371, 477)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
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
        self.form: QWidget = Form
        self.main = QtWidgets.QWidget(Form)
        self.main.setGeometry(QtCore.QRect(10, 10, 300, 450))
        self.main.setStyleSheet("font-size: 14px;\n"
                                "")
        self.main.setObjectName("main")
        self.background = QtWidgets.QLabel(self.main)
        self.background.setGeometry(QtCore.QRect(0, 0, 300, 450))
        self.background.setStyleSheet("background-color: #222831;\n"
                                      "border-radius: 15px;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.image = QtWidgets.QLabel(self.main)
        self.image.setGeometry(QtCore.QRect(100, 30, 100, 100))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        pixmap = QPixmap('resources/fitness.png')
        pixmap = pixmap.scaledToWidth(100)
        pixmap = pixmap.scaledToHeight(100)
        self.image.setPixmap(pixmap)
        self.email_text = QtWidgets.QLineEdit(self.main)
        self.email_text.setGeometry(QtCore.QRect(10, 160, 280, 41))
        self.email_text.setStyleSheet("background-color: #222831;\n"
                                      "color: #eeeeee;\n"
                                      "border: 1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color: #00adb5;\n"
                                      "padding-bottom: 7px;\n"
                                      "")
        self.email_text.setText("")
        self.email_text.setObjectName("email_text")
        self.password_text = QtWidgets.QLineEdit(self.main)
        self.password_text.setGeometry(QtCore.QRect(10, 220, 280, 41))
        self.password_text.setStyleSheet("background-color: #222831;\n"
                                         "color: #eeeeee;\n"
                                         "border: 1px solid rgba(0,0,0,0);\n"
                                         "border-bottom-color: #00adb5;\n"
                                         "padding-bottom: 7px;\n"
                                         "")
        self.password_text.setText("")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.error_label = QtWidgets.QLabel(self.main)
        self.error_label.setGeometry(QtCore.QRect(0, 270, 300, 20))
        self.error_label.setStyleSheet("color: red")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.login = QtWidgets.QPushButton(self.main)
        self.login.setGeometry(QtCore.QRect(75, 310, 150, 40))
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.login_method)
        self.register_btn = QtWidgets.QPushButton(self.main)
        self.register_btn.setGeometry(QtCore.QRect(75, 370, 150, 40))
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_btn.setObjectName("register_btn")
        self.forgot = QtWidgets.QLabel(self.main)
        self.forgot.setGeometry(QtCore.QRect(0, 415, 300, 20))
        self.forgot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot.setStyleSheet("#forgot{\n"
                                  "color: #eeeeee;\n"
                                  "}\n"
                                  "\n"
                                  "#forgot:hover{\n"
                                  "color: #00adb5;\n"
                                  "}")
        self.forgot.setAlignment(QtCore.Qt.AlignCenter)
        self.forgot.setObjectName("forgot")
        self.pushButton = QtWidgets.QPushButton(self.main)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 31, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: #222831; color: #00adb5; font-size: 24px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_window)
        self.register_btn.clicked.connect(self.open_register)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        def move_window(e):
            try:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.form.move(self.form.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            except Exception:
                pass

        def pressEvent(e):
            try:
                self.clickPosition = e.globalPos()
            except Exception:
                pass

        def open_forgot(event):
            self.widget_pass = QtWidgets.QWidget()
            self.forgot_pass = ForgotPassword()
            self.forgot_pass.setupUi(self.widget_pass)
            # self.form.hide()
            # self.widget_pass.show()

        self.form.mousePressEvent = pressEvent
        self.form.mouseMoveEvent = move_window
        self.forgot.mousePressEvent = open_forgot

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.email_text.setPlaceholderText(_translate("Form", "Email"))
        self.password_text.setPlaceholderText(_translate("Form", "Password"))
        self.login.setText(_translate("Form", "Log in"))
        self.register_btn.setText(_translate("Form", "Register"))
        self.forgot.setText(_translate("Form", "Forgot your password?"))
        self.pushButton.setText(_translate("Form", "X"))

    def close_window(self):
        self.form.close()

    def login_method(self):
        email = self.email_text.text()
        password = self.password_text.text()
        if not re.search(EMAIL_REGEX, email):
            self.error_label.setText("Invalid email format")
            return
        self.loading = LoadingScreen()
        result: dict = self.user_service.login(email, password)
        self.loading.stop_loading()
        if result.keys().__contains__("error"):
            self.error_label.setText(result["error"])
            return
        user = self.user_service.decode_token(result["token"])
        UserSingleton.set_instance(user)
        ConfigSingleton.set_user(user, ConfigSingleton.get_image())
        self.open_main()

    def open_register(self):
        self.register_form = RegisterForm()
        self.register_form.setupUi(self.form)
        self.form.show()

    def open_main(self):
        self.MainWindow = QtWidgets.QMainWindow()
        from mainmenu import MainMenu
        self.mainmenu_ui = MainMenu()
        self.mainmenu_ui.setupUi(self.MainWindow)
        self.form.hide()
        self.MainWindow.show()

    def showdialog(self, text):
        msg = QMessageBox()
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # msg.setIcon(QMessageBox.Information)

        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

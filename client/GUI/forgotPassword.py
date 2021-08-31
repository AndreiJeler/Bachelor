from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from clients.httpSingleton import HTTPSingleton


class ForgotPassword(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(355, 182)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Form.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.setStyleSheet("QWidget{\n"
                           "background-color: #222831;\n"
                           "font-size: 18px;\\n\n"
                           "}\n"
                           "\n"
                           "QPushButton{\n"
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
        self.Form = Form
        self.email_text = QtWidgets.QLineEdit(Form)
        self.email_text.setGeometry(QtCore.QRect(30, 50, 300, 40))
        self.email_text.setMinimumSize(QtCore.QSize(300, 40))
        self.email_text.setStyleSheet("background-color: #222831;\n"
                                      "color: #eeeeee;\n"
                                      "border: 1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color: #00adb5;\n"
                                      "padding-bottom: 7px;\n"
                                      "")
        self.email_text.setText("")
        self.email_text.setObjectName("email_text")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(102, 110, 150, 40))
        self.btn.setMinimumSize(QtCore.QSize(150, 40))
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn.setObjectName("btn")
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(320, 0, 41, 23))
        self.close_btn.setStyleSheet("QPushButton{\n"
                                     "background-color: #222831;\n"
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
                                     "}")
        self.close_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setObjectName("close_btn")

        self.btn.clicked.connect(self.action_btn)
        self.close_btn.clicked.connect(lambda _: self.Form.close())
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Form.show()
        self.user_service = HTTPSingleton.get_user_client()

        def move_window(e):
            try:
                if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                    self.Form.move(self.Form.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            except:
                return

        def pressEvent(e):
            try:
                self.clickPosition = e.globalPos()
            except:
                return

        self.Form.mousePressEvent = pressEvent
        self.Form.mouseMoveEvent = move_window

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.email_text.setPlaceholderText(_translate("Form", "Email"))
        self.btn.setText(_translate("Form", "Reset password"))

    def action_btn(self):
        try:
            email = self.email_text.text()
            res = self.user_service.forgot_password(email)
            if res.keys().__contains__("error"):
                self.showdialog(res["error"], True)
            else:
                self.showdialog(res["OK"])
                self.Form.close()
        except Exception as ex:
            self.showdialog(str(ex), True)

    def showdialog(self, text, error=False):
        msg = QMessageBox()
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        if error:
            msg.setIconPixmap(QPixmap('resources/error.png'))
        else:
            msg.setIconPixmap(QPixmap('resources/success.png'))
        msg.setStyleSheet("background-color:#393e46; color:#eeeeee;")
        # msg.setIcon(QMessageBox.Information)

        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

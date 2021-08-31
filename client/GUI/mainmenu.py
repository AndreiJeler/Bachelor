import copy

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFrame, QStackedWidget, QMessageBox

from env.config import ConfigSingleton
from env.envSingleton import EnvSingleton
from models.exercise import ExerciseModel
from clients.httpSingleton import HTTPSingleton
from GUI.login import LoginForm
from GUI.selectMenu import SelectMenu
from env.userSingleton import UserSingleton


class MainMenu(object):
    def setupUi(self, MainWindow: QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.MainWindow: QMainWindow = MainWindow
        self.full_screen = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font-size: 16px;\n"
                                         "color: #eeeeee;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setStyleSheet("background-color: #222831;\n"
                                  "border: none;\n"
                                  "")
        self.header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setLineWidth(0)
        self.header.setObjectName("header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_btn = QtWidgets.QPushButton(self.header)
        self.menu_btn.setMinimumSize(QtCore.QSize(75, 50))
        self.menu_btn.setMaximumSize(QtCore.QSize(75, 50))
        self.menu_btn.setStyleSheet("QFrame{background-color: #222831;}\n"
                                    "\n"
                                    "QPushButton{\n"
                                    "border-radius:5px;}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: #00adb5;\n"
                                    "}")
        self.menu_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/hamburger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QtCore.QSize(50, 50))
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_3.addWidget(self.menu_btn)
        self.name_frame = QtWidgets.QFrame(self.header)
        self.name_frame.setStyleSheet("")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.name_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.name_label = QtWidgets.QLabel(self.name_frame)
        self.name_label.setStyleSheet("")
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_4.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.name_frame)
        self.header_btns = QtWidgets.QFrame(self.header)
        self.header_btns.setMinimumSize(QtCore.QSize(150, 50))
        self.header_btns.setMaximumSize(QtCore.QSize(150, 50))
        self.header_btns.setStyleSheet("QFrame{background-color: #222831;}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "border-radius:5px;}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #00adb5;\n"
                                       "}")
        self.header_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_btns.setObjectName("header_btns")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_btns)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimize_btn = QtWidgets.QPushButton(self.header_btns)
        self.minimize_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.minimize_btn.setStyleSheet("")
        self.minimize_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QtCore.QSize(25, 25))
        self.minimize_btn.setObjectName("minimize_btn")
        self.horizontalLayout.addWidget(self.minimize_btn)
        self.full_btn = QtWidgets.QPushButton(self.header_btns)
        self.full_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.full_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.full_btn.setStyleSheet("")
        self.full_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.full_btn.setIcon(icon2)
        self.full_btn.setIconSize(QtCore.QSize(25, 25))
        self.full_btn.setObjectName("full_btn")
        self.horizontalLayout.addWidget(self.full_btn)
        self.close_btn = QtWidgets.QPushButton(self.header_btns)
        self.close_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.close_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close_btn.setStyleSheet("")
        self.close_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QtCore.QSize(25, 25))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.horizontalLayout_3.addWidget(self.header_btns)
        self.verticalLayout.addWidget(self.header)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("background-color: #393e46;\n"
                                "color: #eeeeee;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_menu: QFrame = QtWidgets.QFrame(self.body)
        self.left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.left_menu.setStyleSheet("QFrame{\n"
                                     "background-color: #222831;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "padding: 5px 10px;\n"
                                     "border: none;\n"
                                     "border-radius: 10px;\n"
                                     "background-color: #222831;\n"
                                     "color: #eeeeee;\n"
                                     "font-size: 14px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "background-color:rgba(57, 62, 70, 1);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "background-color:rgba(57, 62, 70, 0.9);\n"
                                     "}")
        self.left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu.setLineWidth(0)
        self.left_menu.setObjectName("left_menu")
        self.left_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self.left_menu)
        self.left_layout.setContentsMargins(10, 5, 0, 0)
        self.left_layout.setSpacing(20)
        self.left_layout.setObjectName("formLayout")
        self.exercises_btn = QtWidgets.QPushButton(self.left_menu)
        self.exercises_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.exercises_btn.setMaximumSize(QtCore.QSize(150, 40))
        self.exercises_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exercises_btn.setAutoFillBackground(False)
        self.exercises_btn.setStyleSheet("background-image: url(\"./resources/icons/sport.png\");\n"
                                         "background-repeat: none;\n"
                                         "padding-left: 50px;\n"
                                         "background-position: center left;\n"
                                         "border-left: 5px solid #00adb5;\nborder-bottom: 2px solid #00adb5;\n")
        self.current_selected = self.exercises_btn
        self.exercises_btn.setObjectName("exercises_btn")
        self.left_layout.addWidget(self.exercises_btn)
        self.history_btn = QtWidgets.QPushButton(self.left_menu)
        self.history_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.history_btn.setMaximumSize(QtCore.QSize(150, 40))
        self.history_btn.setStyleSheet("background-image: url(\"./resources/icons/book.png\");\n"
                                       "background-repeat: none;\n"
                                       "padding-left: 50px;\n"
                                       "background-position: center left;")
        self.history_btn.setObjectName("history_btn")
        self.left_layout.addWidget(self.history_btn)
        self.profile_btn = QtWidgets.QPushButton(self.left_menu)
        self.profile_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.profile_btn.setMaximumSize(QtCore.QSize(150, 40))
        self.profile_btn.setStyleSheet("background-image: url(\"./resources/icons/user.png\");\n"
                                       "background-repeat: none;\n"
                                       "padding-left: 50px;\n"
                                       "background-position: center left;")
        self.profile_btn.setObjectName("profile_btn")
        self.left_layout.addWidget(self.profile_btn)
        self.horizontalLayout_2.addWidget(self.left_menu)
        self.frame_2 = QtWidgets.QFrame(self.body)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.left_menu)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(400, 40))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 100)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.logout_btn = QtWidgets.QPushButton(self.frame_3)
        self.logout_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.logout_btn.setMaximumSize(QtCore.QSize(150, 40))
        self.logout_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logout_btn.setStyleSheet("background-image: url(\"./resources/icons/logout.png\");\n"
                                      "background-repeat: none;\n"
                                      "padding-left: 50px;\n"
                                      "background-position: center left;")
        self.logout_btn.setObjectName("logout_btn")
        self.left_layout.addWidget(self.frame_3, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget: QStackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.exercises_page = QtWidgets.QWidget()
        self.exercises_page.setObjectName("exercises_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.exercises_page)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.exercise_selection_frame = QtWidgets.QFrame(self.exercises_page)
        self.exercise_selection_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.exercise_selection_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exercise_selection_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exercise_selection_frame.setObjectName("exercise_selection_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.exercise_selection_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.exercise_selection_label = QtWidgets.QLabel(self.exercise_selection_frame)
        self.exercise_selection_label.setObjectName("exercise_selection_label")
        self.horizontalLayout_9.addWidget(self.exercise_selection_label)
        self.exercise_selection_combo = QtWidgets.QComboBox(self.exercise_selection_frame)
        self.exercise_selection_combo.setMinimumSize(QtCore.QSize(300, 30))
        self.exercise_selection_combo.setMaximumSize(QtCore.QSize(300, 30))
        self.exercise_selection_combo.setStyleSheet("QComboBox{color: #eeeeee; background-color: #393e46;}\n"
                                                    "QComboBox:selected{color: #eeeeee; background-color: #393e46;}\n"
                                                    "")
        self.exercise_selection_combo.setObjectName("exercise_selection_combo")
        self.horizontalLayout_9.addWidget(self.exercise_selection_combo)
        self.verticalLayout_8.addWidget(self.exercise_selection_frame, 0, QtCore.Qt.AlignLeft)
        self.exercises_list_frame = QtWidgets.QFrame(self.exercises_page)
        self.exercises_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exercises_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exercises_list_frame.setObjectName("exercises_list_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.exercises_list_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(self.exercises_list_frame)
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1088, 591))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.verticalLayout_8.addWidget(self.exercises_list_frame)
        self.stackedWidget.addWidget(self.exercises_page)
        self.history_page = QtWidgets.QWidget()
        self.history_page.setObjectName("history_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.history_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.history_selection_frame = QtWidgets.QFrame(self.history_page)
        self.history_selection_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.history_selection_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history_selection_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.history_selection_frame.setObjectName("history_selection_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.history_selection_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 50, 0)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.select_label = QtWidgets.QLabel(self.history_selection_frame)
        self.select_label.setMaximumSize(QtCore.QSize(130, 16777215))
        self.select_label.setObjectName("select_label")
        self.horizontalLayout_8.addWidget(self.select_label)
        self.exercise_combo = QtWidgets.QComboBox(self.history_selection_frame)
        self.exercise_combo.setMinimumSize(QtCore.QSize(300, 30))
        self.exercise_combo.setMaximumSize(QtCore.QSize(300, 30))
        self.exercise_combo.setAutoFillBackground(False)
        self.exercise_combo.setStyleSheet("QComboBox{color: #eeeeee; background-color: #393e46;}\n"
                                          "QComboBox:selected{color: #eeeeee; background-color: #393e46;}\n"
                                          "")
        self.exercise_combo.setEditable(False)
        self.exercise_combo.setCurrentText("")
        self.exercise_combo.setMaxVisibleItems(15)
        self.exercise_combo.setMaxCount(10000)
        self.exercise_combo.setObjectName("exercise_combo")
        self.horizontalLayout_8.addWidget(self.exercise_combo)
        self.verticalLayout_4.addWidget(self.history_selection_frame, 0, QtCore.Qt.AlignLeft)
        self.history_table_frame = QtWidgets.QFrame(self.history_page)
        self.history_table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history_table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.history_table_frame.setObjectName("history_table_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.history_table_frame)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.history_table = QtWidgets.QTableWidget(self.history_table_frame)
        self.history_table.setStyleSheet("border: 1px solid #00adb5;\n color:#222831\n; background-color:#eeeeee\n")
        self.history_table.setObjectName("history_table")
        self.verticalLayout_5.addWidget(self.history_table)
        self.verticalLayout_4.addWidget(self.history_table_frame)
        self.stackedWidget.addWidget(self.history_page)
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.profile_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.profile_frame = QtWidgets.QFrame(self.profile_page)
        self.profile_frame.setStyleSheet("")
        self.profile_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_frame.setObjectName("profile_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.profile_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.picture_frame = QtWidgets.QFrame(self.profile_frame)
        self.picture_frame.setMaximumSize(QtCore.QSize(16777215, 225))
        self.picture_frame.setStyleSheet("")
        self.picture_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picture_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_frame.setObjectName("picture_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.picture_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.picture_label = QtWidgets.QLabel(self.picture_frame)
        self.picture_label.setMinimumSize(QtCore.QSize(200, 200))
        self.picture_label.setMaximumSize(QtCore.QSize(200, 200))
        self.picture_label.setText("")
        self.picture_label.setScaledContents(True)
        self.picture_label.setObjectName("picture_label")
        self.horizontalLayout_6.addWidget(self.picture_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.picture_frame)
        self.frame = QtWidgets.QFrame(self.profile_frame)
        self.frame.setStyleSheet("color: #eeeeee;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.name_layout = QtWidgets.QFormLayout()
        self.name_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.name_layout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.name_layout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.name_layout.setContentsMargins(200, -1, 200, -1)
        self.name_layout.setHorizontalSpacing(15)
        self.name_layout.setVerticalSpacing(50)
        self.name_layout.setObjectName("name_layout")
        self.email_profile_label = QtWidgets.QLabel(self.frame)
        self.email_profile_label.setObjectName("email_profile_label")
        self.name_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.email_profile_label)
        self.name_profile_label = QtWidgets.QLabel(self.frame)
        self.name_profile_label.setObjectName("name_profile_label")
        self.name_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name_profile_label)
        self.email_text_profile = QtWidgets.QLineEdit(self.frame)
        self.email_text_profile.setEnabled(False)
        self.email_text_profile.setStyleSheet("border: none; border-bottom: 1px solid #00adb5;")
        self.email_text_profile.setObjectName("email_text_profile")
        self.name_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.email_text_profile)
        self.name_text_profile = QtWidgets.QLineEdit(self.frame)
        self.name_text_profile.setEnabled(False)
        self.name_text_profile.setStyleSheet("border: none; border-bottom: 1px solid #00adb5;")
        self.name_text_profile.setObjectName("name_text_profile")
        self.name_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_text_profile)
        self.pass_label = QtWidgets.QLabel(self.frame)
        self.pass_label.setObjectName("pass_label")
        self.name_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pass_label)
        self.password_text_profile = QtWidgets.QLineEdit(self.frame)
        self.password_text_profile.setStyleSheet("border: none; border-bottom: 1px solid #00adb5;")
        self.password_text_profile.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text_profile.setObjectName("password_text_profile")
        self.name_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_text_profile)
        self.confirm_label = QtWidgets.QLabel(self.frame)
        self.confirm_label.setObjectName("confirm_label")
        self.name_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.confirm_label)
        self.confirm_text_profile = QtWidgets.QLineEdit(self.frame)
        self.confirm_text_profile.setStyleSheet("border: none; border-bottom: 1px solid #00adb5;")
        self.confirm_text_profile.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_text_profile.setObjectName("confirm_text_profile")
        self.name_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirm_text_profile)
        self.change_pass_btn = QtWidgets.QPushButton(self.frame)
        self.change_pass_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.change_pass_btn.setStyleSheet("QPushButton{\n"
                                           "border-radius:5px;\n"
                                           "border: 1px solid #00adb5;\n"
                                           "font-size: 20px;}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: #00adb5;\n"
                                           "}")
        self.change_pass_btn.setObjectName("change_pass_btn")
        self.name_layout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.change_pass_btn)
        self.horizontalLayout_7.addLayout(self.name_layout)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.profile_frame)
        self.stackedWidget.addWidget(self.profile_page)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.exercise_combo.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.user_service = HTTPSingleton.get_user_client()
        self.exercise_service = HTTPSingleton.get_exercise_client()
        self.activity_service = HTTPSingleton.get_activity_client()

        self.exercises = []
        self.all_exercises = []
        self.current_exercise: ExerciseModel = None

        self.history_table.setColumnCount(5)
        history_headers = ["Exercise name", "Date", "Number of repetitions", "Duration", "Details"]
        self.history_table.setHorizontalHeaderLabels(history_headers)
        self.history_table.setColumnWidth(0, 200)
        self.history_table.setColumnWidth(1, 200)
        self.history_table.setColumnWidth(2, 200)
        self.history_table.setColumnWidth(3, 200)
        # self.history_table.setColumnWidth(4, 200)
        self.history_table.horizontalHeader().setStretchLastSection(True)

        self.exercises_frames = []

        self.get_profile_pic()
        self.get_exercises()

        self.connect_buttons()
        self.name_label.setText("Welcome " + UserSingleton.get_instance().name)
        self.email_text_profile.setText(UserSingleton.get_instance().email)
        self.name_text_profile.setText(UserSingleton.get_instance().name)

        self.exercise_selection_combo.addItem("All body regions")
        self.exercise_selection_combo.addItem("Legs")
        self.exercise_selection_combo.addItem("Shoulders")
        self.exercise_selection_combo.addItem("Biceps")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_label.setText(_translate("MainWindow", "Welcome First Name Last Name"))
        # self.exercises_btn.setText(_translate("MainWindow", "Exercises"))
        # self.history_btn.setText(_translate("MainWindow", "History"))
        # self.profile_btn.setText(_translate("MainWindow", "Profile"))
        self.select_label.setText(_translate("MainWindow", "Select exercise:"))
        self.email_profile_label.setText(_translate("MainWindow", "Email:"))
        self.name_profile_label.setText(_translate("MainWindow", "Name:"))
        self.pass_label.setText(_translate("MainWindow", "Current Password:"))
        self.confirm_label.setText(_translate("MainWindow", "New password:"))
        self.change_pass_btn.setText(_translate("MainWindow", "Change password"))
        self.exercise_selection_label.setText(_translate("MainWindow", "Select body region:"))
        # self.logout_btn.setText(_translate("MainWindow", "Logout"))

    def connect_buttons(self):
        self.close_btn.clicked.connect(self.MainWindow.close)
        self.minimize_btn.clicked.connect(self.MainWindow.showMinimized)
        self.full_btn.clicked.connect(self.maximize)
        self.menu_btn.clicked.connect(self.slide_left_menu)
        self.exercises_btn.clicked.connect(lambda: self.set_current_page(self.exercises_page, self.exercises_btn))
        self.history_btn.clicked.connect(lambda: self.set_current_page(self.history_page, self.history_btn))
        self.profile_btn.clicked.connect(lambda: self.set_current_page(self.profile_page, self.profile_btn))
        self.logout_btn.clicked.connect(self.logout)
        self.change_pass_btn.clicked.connect(self.change_pass)
        self.exercise_combo.currentIndexChanged.connect(self.exercise_changed)

        def move_window(e):
            try:
                if not self.MainWindow.isMaximized():
                    if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                        self.MainWindow.move(self.MainWindow.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
            except:
                return

        def pressEvent(e):
            try:
                self.clickPosition = e.globalPos()
            except:
                return

        self.MainWindow.mousePressEvent = pressEvent
        self.header.mouseMoveEvent = move_window
        self.exercise_selection_combo.currentIndexChanged.connect(self.select_body_region)

    def select_body_region(self):
        if self.exercise_selection_combo.currentIndex() == 0:
            for frame in self.exercises_frames:
                frame[0].setVisible(True)
        else:
            for frame in self.exercises_frames:
                frame[0].setVisible(True)
            for frame in self.exercises_frames:
                if frame[1].body_region != self.exercise_selection_combo.currentText():
                    frame[0].setVisible(False)

    def slide_left_menu(self):
        width = self.left_menu.width()
        if width == 150:
            new_width = 0
            self.exercises_btn.setText("")
            self.history_btn.setText("")
            self.profile_btn.setText("")
            self.logout_btn.setText("")
        else:
            new_width = 150
            self.exercises_btn.setText("Exercises")
            self.history_btn.setText("History")
            self.profile_btn.setText("Profile")
            self.logout_btn.setText("Logout")

        self.animation = QPropertyAnimation(self.left_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        self.animation2 = QPropertyAnimation(self.logout_btn, b"minimumWidth")
        self.animation2.setDuration(300)
        self.animation2.setStartValue(width)
        self.animation2.setEndValue(new_width)
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation2.start()

    def maximize(self):
        if self.full_screen == 0:
            self.full_screen = 1
            self.MainWindow.showMaximized()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/icons/miniscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.full_btn.setIcon(icon)
        else:
            self.full_screen = 0
            self.MainWindow.showNormal()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/icons/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.full_btn.setIcon(icon)

    def set_current_page(self, page, btn):
        self.current_selected.setStyleSheet(self.current_selected.styleSheet().replace(
            "border-left: 5px solid #00adb5;\nborder-bottom: 2px solid #00adb5;\n", ""))
        self.current_selected = btn
        self.stackedWidget.setCurrentWidget(page)
        if page == self.history_page:
            self.retrieve_history()
        btn.setStyleSheet(btn.styleSheet() + "border-left: 5px solid #00adb5;\nborder-bottom: 2px solid #00adb5;\n")

    def get_profile_pic(self):
        if not ConfigSingleton.get_image():
            path = self.user_service.get_profile_pic(UserSingleton.get_instance().id)
            img = QPixmap(path)
            self.picture_label.setPixmap(img)
            ConfigSingleton.set_image(path)
        else:
            self.picture_label.setPixmap(QPixmap(ConfigSingleton.get_image()))

    def logout(self):
        EnvSingleton.removeToken()
        UserSingleton.set_instance(None)
        ConfigSingleton.reset_user()
        form = QtWidgets.QMainWindow()
        login_ui = LoginForm()
        login_ui.setupUi(form)
        form.show()
        self.MainWindow.close()

    def change_pass(self):
        try:
            self.user_service.change_password(self.password_text_profile.text(), self.confirm_text_profile.text())
            self.showdialog("Password changed!")
        except Exception as ex:
            self.showdialog(str(ex))

    def showdialog(self, text):
        msg = QMessageBox()
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # msg.setIcon(QMessageBox.Information)

        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

    def get_exercises(self):
        self.exercises = self.exercise_service.get_all()
        self.exercise_combo.clear()
        self.exercise_combo.addItems(["All exercises"] + [ex.name for ex in self.exercises])
        self.all_exercises = copy.deepcopy(self.exercises)
        self.retrieve_history()

        self.add_exercises_btns()

    def add_exercises_btns(self):
        row = 0
        column = 0
        for e in self.exercises:
            ex = ConfigSingleton.get_exercise_id(e.id)
            if not ex:
                ex = {"id": e.id, "body_region": e.body_region, "difficulty": e.difficulty, "name": e.name,
                      "reps_labels": str(e.reps_labels), "reps_explanations": str(e.reps_explanations),
                      "correctness_labels": str(e.correctness_labels),
                      "correctness_explanations": str(e.correctness_explanations)}
                ConfigSingleton.add_exercise(ex)

            image = self.exercise_service.get_icon(e.id)
            ConfigSingleton.set_exercise_icon(e.id, image)
            e.pic = image

            start_pic = self.exercise_service.get_start_pic(e.id)
            ConfigSingleton.set_exercise_start_picture(e.id, start_pic)
            e.start_pic = start_pic

            end_pic = self.exercise_service.get_end_pic(e.id)
            ConfigSingleton.set_exercise_end_picture(e.id, end_pic)
            e.end_pic = end_pic

            reps_model = self.exercise_service.get_reps_model(e.id)
            ConfigSingleton.set_exercise_reps_model(e.id, reps_model)
            e.reps_model = reps_model

            correctness_model = self.exercise_service.get_correctness_model(e.id)
            ConfigSingleton.set_exercise_correctness_model(e.id, correctness_model)
            e.correctness_model = correctness_model

            self.add_exercise_widget(e, row, column)
            column += 1
            if column == 5:
                row += 1
                column = 0

        ConfigSingleton.save_config_file()

    def exercise_changed(self):
        current_id = self.exercise_combo.currentIndex()
        if current_id == 0:
            self.current_exercise = None
        else:
            self.current_exercise = self.exercises[current_id - 1]
        self.retrieve_history()

    def retrieve_history(self):
        if self.current_exercise:
            history = self.activity_service.get_history_exercise(self.current_exercise.id)
        else:
            history = self.activity_service.get_history_exercise("-1")
        table_data = []
        for h in history:
            for s in h["sets"]:
                table_data.append(
                    {"name": h["exercise_name"], "nr_reps": s["nr_reps"], "seconds": s["seconds"], "date": h["date"],
                     "details": s["details"]})
        self.history_table.setRowCount(len(table_data))
        row = 0
        for data in table_data:
            self.history_table.setItem(row, 0, QtWidgets.QTableWidgetItem(data["name"]))
            self.history_table.setItem(row, 1, QtWidgets.QTableWidgetItem(data["date"][:10]))
            self.history_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data["nr_reps"])))
            self.history_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data["seconds"]) + " seconds"))
            self.history_table.setItem(row, 4, QtWidgets.QTableWidgetItem(data["details"]))
            row += 1

    def add_exercise_widget(self, exercise, row, column):
        self.exercise_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.exercise_frame.setMinimumSize(QtCore.QSize(200, 300))
        self.exercise_frame.setMaximumSize(QtCore.QSize(200, 300))
        self.exercise_frame.setStyleSheet("background-color: #222831;")
        self.exercise_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exercise_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exercise_frame.setObjectName(exercise.name + "_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.exercise_frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(exercise.name + "_layout")
        self.exercise_name_label = QtWidgets.QLabel(self.exercise_frame)
        self.exercise_name_label.setMinimumSize(QtCore.QSize(0, 30))
        self.exercise_name_label.setMaximumSize(QtCore.QSize(200, 30))
        self.exercise_name_label.setAutoFillBackground(False)
        self.exercise_name_label.setStyleSheet("")
        self.exercise_name_label.setLineWidth(0)
        self.exercise_name_label.setObjectName(exercise.name + "_name")
        self.exercise_name_label.setText(exercise.name)
        self.verticalLayout_10.addWidget(self.exercise_name_label, 0, QtCore.Qt.AlignHCenter)
        self.exercise_image = QtWidgets.QLabel(self.exercise_frame)
        self.exercise_image.setLineWidth(0)
        self.exercise_image.setPixmap(QtGui.QPixmap(exercise.pic))
        self.exercise_image.setScaledContents(True)
        self.exercise_image.setObjectName(exercise.name + "_image")
        self.verticalLayout_10.addWidget(self.exercise_image)
        self.gridLayout.addWidget(self.exercise_frame, row, column, 1, 1,
                                  QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.exercise_frame.mousePressEvent = lambda _: self.open_exercise(exercise)
        self.exercises_frames.append([self.exercise_frame, exercise])

    def open_exercise(self, exercise):
        self.new_form = QtWidgets.QWidget()
        self.select_menu = SelectMenu()
        self.select_menu.setupUi(self.new_form, exercise)
        self.new_form.show()
        # self.new_mainWindow: QMainWindow = QtWidgets.QMainWindow()
        # self.exercise_ui = ExerciseUI()
        # self.exercise_ui.setupUi(self.new_mainWindow, exercise)
        # self.new_mainWindow.show()

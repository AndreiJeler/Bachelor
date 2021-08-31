from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QSize

from PyQt5.QtWidgets import QWidget, QLabel


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(100, 100)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie = QMovie('resources/loading.gif')
        self.movie.setScaledSize(QSize().scaled(100, 100, Qt.KeepAspectRatio))
        self.label_animation.setMovie(self.movie)
        self.movie.start()

        self.show()

    def stop_loading(self):
        self.movie.stop()
        self.close()

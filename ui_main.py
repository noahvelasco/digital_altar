from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QFont, QFontDatabase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Altar")
        self.showFullScreen()

# Load custom medieval font
        font_id = QFontDatabase.addApplicationFont("fonts/OldLondon.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        self.setStyleSheet("background-color: black;")
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(font_family, 350))  # Use the custom font
        self.label.setStyleSheet("color: white;")
        self.setCentralWidget(self.label)
        self.update_time()

    def update_time(self):
        now = QTime.currentTime()
        self.label.setText(now.toString("hh:mm:ss"))

    def show_pray_message(self):
        self.label.setText("☩")

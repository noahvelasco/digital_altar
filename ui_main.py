from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Altar")
        self.setGeometry(100, 100, 480, 320)
        self.setStyleSheet("background-color: black;")

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Times", 48))
        self.label.setStyleSheet("color: white;")
        self.setCentralWidget(self.label)

        self.update_time()

    def update_time(self):
        now = QTime.currentTime()
        self.label.setText(now.toString("hh:mm:ss"))

    def show_pray_message(self):
        self.label.setText("🙏 Pray 🙏")

from PySide6.QtWidgets import QApplication,QMainWindow, QLabel
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QFont, QFontDatabase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Altar")
        
        # FULLSCREEN MODE
        #self.showFullScreen()

        # CUSTOM SCREEN SIZE MODE
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        width = screen_size.width() * 0.75  # 75% of screen width
        height = screen_size.height() * 0.5  # 50% of screen height
        self.setFixedSize(int(width), int(height))

# Load custom medieval font
        font_id = QFontDatabase.addApplicationFont("fonts/OldLondon.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        self.setStyleSheet("background-color: black;")
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont(font_family, 365))  # Use the custom font
        self.label.setStyleSheet("color: white;")
        self.setCentralWidget(self.label)
        self.update_time()

    def update_time(self):
        now = QTime.currentTime()
        self.label.setText(now.toString("hh:mm:ss"))

    def show_pray_message(self):
        self.label.setText("☩")


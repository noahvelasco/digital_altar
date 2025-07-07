from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from ui_main import MainWindow
from bell_scheduler import schedule_bells
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Start the bell scheduler
schedule_bells(window)

# Update the clock every second
timer = QTimer()
timer.timeout.connect(window.update_time)
timer.start(1000)

sys.exit(app.exec())

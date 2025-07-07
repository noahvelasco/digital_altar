# Digital Altar

A simple Python app for Raspberry Pi that shows the time and plays church bells at prayer times, displaying a reminder message.

---

## Getting Started

### Dependencies

This project requires:

- **Python 3.13+**
- **PySide6** — for the graphical user interface (Qt6)
- **APScheduler** — for scheduling prayer bell times
- **simpleaudio** — for playing bell sound files (WAV)

---

### Setup Instructions

1. **Clone or download the repository** and open a terminal in the root of the folder.

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Install dependencies**

    ```bash
    pip install pyside6 apscheduler simpleaudio
    ```

4. **Run the app**

    ```bash
    python main.py
    ```

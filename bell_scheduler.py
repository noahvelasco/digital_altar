from apscheduler.schedulers.background import BackgroundScheduler
import threading
import simpleaudio
import datetime

BELL_TIMES = [(6, 0), (12, 0), (22, 21)]  # 6 AM, 12 PM, 6 PM

def play_bell():
    try:
        wave_obj = simpleaudio.WaveObject.from_wave_file("assets/church_bell.wav")
        wave_obj.play()
    except Exception as e:
        print("Error playing bell:", e)

def show_and_ring(window):
    play_bell()
    window.show_pray_message()

    # After 10 seconds, revert to clock
    def restore_clock():
        window.update_time()
    threading.Timer(60, restore_clock).start()

def schedule_bells(window):
    scheduler = BackgroundScheduler()
    for hour, minute in BELL_TIMES:
        scheduler.add_job(lambda w=window: show_and_ring(w), 'cron', hour=hour, minute=minute)
    scheduler.start()

import psutil
import time
import os

COUNTDOWN_TIME = 10

def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    return round(percent)

def clean_terminal():
    os.system('clear')

def print_battery_histogram(percentage):
    bar_length = 20
    filled_length = int(bar_length * percentage / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'Battery: {percentage}% [{bar}]')

if __name__ == "__main__":
    clean_terminal()
    try:
        countdown_seconds = COUNTDOWN_TIME
        battery_percentage = get_battery_percentage()

        while True:
            print_battery_histogram(battery_percentage)
            print(f'Updating in {countdown_seconds}s', flush=True)
            time.sleep(1)
            countdown_seconds -= 1
            clean_terminal()

            if countdown_seconds == 0:
                countdown_seconds = COUNTDOWN_TIME
                battery_percentage = get_battery_percentage()

    except KeyboardInterrupt:
        print("\nExiting...")

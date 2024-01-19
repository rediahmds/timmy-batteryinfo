import psutil
import time
import os
from asciichartpy import plot

COUNTDOWN_TIME = 10
MAX_HISTORY_LENGTH = 30  # Adjust this value based on your preference
history = []

def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    return round(percent)

def clean_terminal():
    os.system('clear')

def print_battery_chart(history):
    chart_length = min(MAX_HISTORY_LENGTH, len(history))
    chart_data = history[-chart_length:]
    
    chart = plot(chart_data, {'height': 10, 'format': '{:3.2f}', 'suffix': ' %'})
    print(f"\nBattery Usage Chart:\n{chart}\n")

if __name__ == "__main__":
    clean_terminal()
    try:
        countdown_seconds = COUNTDOWN_TIME
        battery_percentage = get_battery_percentage()

        while True:
            history.append(battery_percentage)

            print(f"\rBattery: {battery_percentage}% - Updating in {countdown_seconds}s", flush=True)
            print_battery_chart(history)

            time.sleep(1)
            countdown_seconds -= 1
            clean_terminal()

            if countdown_seconds == 0:
                countdown_seconds = COUNTDOWN_TIME
                battery_percentage = get_battery_percentage()
                # history = []  # Clear history after printing the chart

    except KeyboardInterrupt:
        print("\nExiting...")

import psutil
import time
import os

# from DOGZILLALib import DOGZILLA

# g_dog = DOGZILLA()

COUNTDOWN_TIME = 10

def get_battery_percentage():
    battery = psutil.sensors_battery()
    percent = battery.percent
    # batt = g_dog.read_battery()
    return round(percent)
  
def clean_terminal():
		os.system('clear')

if __name__ == "__main__":
    clean_terminal()
    try:
        countdown_seconds = COUNTDOWN_TIME
        battery_percentage = get_battery_percentage()

        while True:
            print(f"\rBattery: {battery_percentage}% - Updating in {countdown_seconds}s", flush=True)
            time.sleep(1)
            countdown_seconds -= 1
            clean_terminal()
            
            if countdown_seconds == 0:
                countdown_seconds = COUNTDOWN_TIME
                battery_percentage = get_battery_percentage()
                
    except KeyboardInterrupt:
        print("\nExiting...")

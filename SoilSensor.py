import RPi.GPIO as GPIO
import time

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def check_sensor():
    """检查传感器状态并打印信息"""
    if GPIO.input(channel):
        print("Water Detected!")
    else:
        print("No Water Detected!")

total_seconds = 4 * 24 * 60 * 60
interval_seconds = 3 * 60 * 60

start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > total_seconds:
        break
    if int(elapsed_time) % interval_seconds == 0:
        check_sensor()
    time.sleep(1)

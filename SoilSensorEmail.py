import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

# GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

from_email_addr = "1320401599@qq.com"
from_email_pass = "wfagroqwcpmfjfda"
to_email_addr = "1320401599@qq.com"


def send_email(status):
    msg = EmailMessage()
    body = status
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Plant Status Update'
    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print('Email sent')
    server.quit()


while True:
    sensor_value = GPIO.input(channel)
    print(sensor_value)
    if sensor_value==0:
        status = "Water NOT needed"
    else:
        status =  "Please water your plant"
    print(status)
    send_email(status)
    time.sleep(20)

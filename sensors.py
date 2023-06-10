import RPi.GPIO as GPIO
import sqlite3
from time import sleep


INPUT_PINS = [2, 3, 17, 27]
CAST_PIN = 2
PINS_TO_SPELLS = {3: 1, 17: 2, 27: 3}
QUERY = "update foo set spell=%d where id=1;"
DELAY = .3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in INPUT_PINS:
    GPIO.setup(pin, GPIO.IN)

conn = sqlite3.connect('data.db')


selected_pin = 0  # 0 -> no pin selected
while True:
    for pin in INPUT_PINS:
        if (GPIO.input(pin) == False):
            if pin == CAST_PIN and selected_pin > 0:
                conn.execute(QUERY % PINS_TO_SPELLS[selected_pin])
                conn.commit()
                selected_pin = 0
            elif pin != CAST_PIN:
                selected_pin = pin
            sleep(DELAY)

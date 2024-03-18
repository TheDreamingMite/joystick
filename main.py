import OPi.GPIO as GPIO
import time

print("Start!")

GPIO.setmode(GPIO.BOARD)

button_pin = 7

GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        button_state = GPIO.input(button_pin)
        print(button_state)
        if button_state == GPIO.LOW:
            print("+")
        else:
            print("-")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
print("Stop!")

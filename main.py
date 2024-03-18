import OPi.GPIO as GPIO
import time

print("Start!")

GPIO.setmode(GPIO.BOARD)

button_pin = 7

GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        button_state = GPIO.input(button_pin)

        if button_state == GPIO.LOW:
            print("Кнопка нажата")
        else:
            print("Кнопка отпущена")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
print("Hi! Stop!")

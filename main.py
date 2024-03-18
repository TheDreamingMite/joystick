import OPi.GPIO as GPIO
import time

print("Hi! Start!!")

# Установка режима нумерации пинов (в данном случае, по названию пина)
GPIO.setmode(GPIO.BOARD)

# Номер GPIO пина, к которому подключена кнопка
button_pin = 1

# Установка пина как вход
GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        # Считываем состояние кнопки
        button_state = GPIO.input(button_pin)

        # Если кнопка нажата (LOW)
        if button_state == GPIO.LOW:
            print("Кнопка нажата")
        else:
            print("Кнопка отпущена")

        # Ждем некоторое время перед повторной проверкой
        time.sleep(0.1)

except KeyboardInterrupt:
    # Выход из программы при нажатии Ctrl+C
    GPIO.cleanup()
print("Hi! Stop!")

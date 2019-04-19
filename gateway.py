import keyboard
import serial
import time

while True:
    with serial.Serial('/dev/ttyACM0', 115200) as ser:
        token = ser.read()
        # print(token)

    if token == b'l':
        # print("keyboard write")
        # keyboard.write(' ')
        keyboard.press_and_release('left')

    elif token == b'r':
        keyboard.press_and_release('right')
    elif token == b'u':
        # keyboard.press_and_release('up')
        keyboard.write(' ')

    # keyboard.wait('esc')

    # time.sleep(1)
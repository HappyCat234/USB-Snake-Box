from digitalio import DigitalInOut, Direction, Pull
import touchio
import board
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import os
from digitalio import DigitalInOut, Direction, Pull

button1 = DigitalInOut(board.D2)
button1.direction = Direction.INPUT

button2 = DigitalInOut(board.D0)
button2.direction = Direction.INPUT

button3 = DigitalInOut(board.D3)
button3.direction = Direction.INPUT

button4 = DigitalInOut(board.D4)
button4.direction = Direction.INPUT

time.sleep(1)
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)
while button1.value == False and button2.value == False and button3.value == False and button4.value == False:
    pass
if button1.value:
    print("Button 1 pressed")
    scripttext = open("script1.txt")
elif button2.value:
    print("Button 2 pressed")
    scripttext = open("script2.txt")
elif button3.value:
    print("Button 3 pressed")
    scripttext = open("script3.txt")
elif button4.value:
    print("Button 4 pressed")
    scripttext = open("script4.txt")
script = scripttext.readlines()
script = [x.strip() for x in script]
print("running")
for line in script:
    
    splittext = line.split(" ")

    command = splittext[0]
    parameter = ""
    for section in splittext[1:]:
        parameter = parameter + section
        if section != splittext[:-1]:
            parameter = parameter + " "
           
    print(command + " " + parameter)
    if command == "STRING":
        layout.write(parameter)
    elif command == "GUI" or command == "WINDOWS":
        kbd.press(Keycode.GUI)
        parameter = "Keycode." + parameter
        try:
            kbd.press(eval(parameter))
        except SyntaxError:
            print("no parameter")
        kbd.release_all()
    elif command == "APP" or command == "MENU":
        kbd.press(Keycode.APPLICATION)
        kbd.release_all()
    elif command == "SHIFT":
        kbd.press(Keycode.SHIFT)
        if command == "PAGEUP":
            kbd.press(Keycode.PAGE_UP)
        elif command == "PAGEDOWN":
            kbd.press(Keycode.PAGE_DOWN)
        elif command == "UPARROW":
            kbd.press(Keycode.UP_ARROW)
        elif command == "DOWNARROW":
            kbd.press(Keycode.DOWN_ARROW)
        elif command == "LEFTARROW":
            kbd.press(Keycode.LEFTARROW)
        elif command == "RIGHTARROW":
            kbd.press(Keycode.RIGHTARROW)
        else:
            parameter = "Keycode." + parameter
            kbd.press(eval(parameter))
        kbd.release_all()
        
    elif command == "ALT":
        kbd.press(Keycode.ALT)
        parameter = "Keycode." + parameter
        kbd.press(eval(parameter))
        kbd.release_all()
    elif command == "CONTROL" or command == "CTRL":
        kbd.press(Keycode.CONTROL)
        parameter = "Keycode." + parameter
        kbd.press(eval(parameter))
        kbd.release_all()
    elif command == "DELAY":
        time.sleep(int(parameter) / 1000)
    elif command == "REM":
        print("comment")
    elif command == "DOWN":
        kbd.press(Keycode.DOWN_ARROW)
    else:
        command = "Keycode." + command
        print("pressing command key")
        kbd.press(eval(command))
        kbd.release_all()
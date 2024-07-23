# Use pynput to control keyboard or mouse,  execute keystrokes or record keystrokes.
# library pyautogui can move your mouse intermittently to make it appear you are online.

import sys
from time import sleep
from pynput.keyboard import Key, Controller, Listener
# from pynput.mouse import Button, Controller, Listener



# We can always stop a keyboard listener by returning False from a callback function i.e. on_press or on_release

def on_press(k):
    global keys

    if hasattr(k,'char'):  # Returns True only if a character has been pressed => key.char will exist
        string = k.char.replace("'","\'")
    elif k == Key.space:
        string = ' '
    elif k == Key.enter:
        string = '\n'
    else:
        print(f'NON-CHAR PRESSED: {k}')
        return True
    print(f'KEY PRESSED:{string}')
    keys.append(string)


def on_release(k):
    print(f'KEY RELEASED:{k}')
    if k == Key.esc:
        return False  # EXIT THE PROGRAM

if __name__ == '__main__':


    keyboard = Controller()
    sleep(5)  # give chance to switch apps to p-touch editor
    # Hit CTRL-P and then ENTER
    for x in range(1,7):
        keyboard.press(Key.ctrl_l)
        keyboard.press('p')
        keyboard.release('p')
        keyboard.release(Key.ctrl_l)
        sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(3)
        print(f'sticker {x} has been printed!')
    sys.exit()

    # You can auto-control the keyboard
    keyboard.press('a')  # keyboard auto enters 'a'
    keyboard.release('a')  # Make sure to always release keys that you press using code

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    keyboard.type('hello')  # keyboard enters a full string


    recorded_keys = []
    with Listener(on_press=on_press, on_release=on_release) as l:
        l.join()  # do not confuse with str.join()

 # Equivalent to
 #    l = Listener(on_press=on_press, on_release=on_release)
 #    l.start()   -> starts listenting
 #    l.join()    -> flow returns here when on_press or on_release returns False

    main_string = "".join(recorded_keys)
    with open(r'myfiles\keys.txt', 'a') as f:
        f.write(main_string)

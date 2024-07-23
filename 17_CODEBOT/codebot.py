from botcore import leds, motors, LEFT, RIGHT, buttons, spkr
from time import sleep

# Battery-USB switch
# Hit Reboot button to rerun last program


leds.user_num(0,True)  # Leds are numbered 0-7  - user red 'BYTE' leds
leds.user(0b01010101)  # set leds using binary
leds.user([False, True, False, True, False, True, False, True]) # same as above using lists



leds.ls_num(0, True)     # Leds are numbered 0,1,2,3,4  - line sensor green leds
leds.ls(0b11111)         # set all leds on using binary

leds.prox_num(0, True)  # Leds are numbered 0,1  - proximity sensor green leds
leds.prox(0b11)         # using binary


motors.enable(True)
motors.run(LEFT, 75)  # Runs forward 75%   range=-100 to 100
sleep(1)
motors.enable(False)


if buttons.was_pressed(0):
    pass # button-0 has been pressed
elif buttons.was_pressed(1):
    pass # button-1 has been pressed


spkr.pitch(500) # Starts 500hz tone
spkr.off()      # Stops playing sound

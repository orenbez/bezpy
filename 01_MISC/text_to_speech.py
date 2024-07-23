
from playsound import playsound
playsound(r'myfiles\hollow.mp3')  # play sound clip


import pyttsx3
speaker = pyttsx3.init()
speaker.say('Testing, testing. This is a test.')
speaker.runAndWait() # executes above speech and continutes flow when completed.
speaker.stop()
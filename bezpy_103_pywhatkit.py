# Automate sending whatsapp messages
# Creates logfile PyWhatKit_DB.txt


# requires 'pip install pywhatkit'
# requires 'pip install flask'
from pywhatkit import sendwhatmsg, sendwhatmsg_instantly, system

# requires google chrome to be open will log into web.whatsapp.com

system() # 'Windows'
sendwhatmsg_instantly('+14012687383', 'test message')


# must must be programed for at least 2 mins in the future
sendwhatmsg('+14012687383', 'test message', time_hour=11, time_min=30, wait_time=5, tab_close=False, close_time=3)   # time_hour=00-23 ,  time_minute=00-59
# program will pause until time of sending


# >>> dir(pywhatkit)  
# ['__VERSION__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__path__', '__spec__', 'ascii_art', 'cancel_shutdown', 'core', 'handwriting', 'image_to_ascii_art', 'info', 'mail',
# 'misc', 'open_web', 'playonyt', 'remotekit', 'sc', 'search', 'send_hmail', 'send_mail', 'sendwhatmsg',
# 'sendwhatmsg_instantly', 'sendwhatmsg_to_group', 'sendwhatmsg_to_group_instantly', 'sendwhats_image', 'show_history',
# 'shutdown', 'start_server', 'system', 'take_screenshot', 'text_to_handwriting',
# 'web_screenshot', 'whats']
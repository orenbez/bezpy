# https://pypi.org/project/win10toast/
# On Windows 10 see Settings->'Focus assist'  SET TO OFF to view notifications
# Also check Settings->'Notifications & actions'
# optional .ico files can be used. Use http://icoconvert.com/ to create .ico files
# threaded show_toast() commands will permit you to continue to with code during notification

from platform import system, release
from win10toast import ToastNotifier
from playsound import playsound

notification_duration = 3  # Seconds

if system() == 'Windows' and release() == '10':
    toaster = ToastNotifier()
    toaster.show_toast('Title1')  # Default message, duration, and icon),
    playsound(r'myfiles\hollow.mp3')  # play sound clip

    # flow is paused until duration is complete
    toaster.show_toast('Title2', 'Message2 is not threaded', duration=notification_duration , icon_path=r".\myfiles\icon.ico")
    print('This will only print when Message2 duration is complete')
    input('Press Return to continue')

    # flow is not paused, the show_toast function is threaded
    toaster.show_toast('Title3', 'Message3 is threaded', duration=notification_duration , icon_path=r".\myfiles\icon.ico", threaded=True)
    while toaster.notification_active():
        print('Message 3 is currently active')

# simmilar notification using the 'plyer' library
from plyer import notification
notification.notify(title = 'testing', message = 'message', app_icon = r".\myfiles\icon.ico",  timeout = 10)
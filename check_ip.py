# On startup this program will notify you if your external ipaddress has changes

# place in directory C:\ip_address  ...
#   1) check_ip.py   2) bezpy_11_send_email.py

# place in directory %ALLUSERSPROFILE%\Microsoft\Windows\Start Menu\Programs\Startup ...
#   check_ip.bat which contains line python C:\ip_address\check_ip.py


from datetime import datetime
import json
from urllib.request import urlopen
from bezpy_11_send_email import send

IP_FILE = r'C:\ip_address\ip_address.json'
LOCATION = 'OREN'

def get_ip_address() -> str:
    url = 'https://api.ipify.org'
    return urlopen(url).read().decode('utf-8')


def read_ip_address():
    """reads ip-address from json file"""
    with open(IP_FILE, 'r') as f:
        try: 
            return json.load(f)
        except json.JSONDecodeError:
            return None

def set_ip_address(data):
    with open(IP_FILE, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    new_ip = get_ip_address()
    previous = read_ip_address()
    prev_ip = previous.get('ip')

    print(f'{prev_ip=}\n{new_ip=}')
    if new_ip != prev_ip:
        updated = dict(ip=new_ip, last_change=datetime.now().isoformat())
        set_ip_address(updated)
        print('ip_address changed')
        message =  f'{updated=}<br>{previous=}<br><b>Update If Required</b><br>1) FTP Server (FTP Traffic-In) <br>2) Remote Desktop File <br>3) Warn Albert to update his Camera app'
        send('bezoren@gmail.com', f"{LOCATION}'s IP Address Changed", message)
    else:
        print('ip_address has not changed')

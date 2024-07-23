import os
import json
from pprint import pprint
from datetime import timedelta as td
from dateutil.relativedelta import relativedelta as rd
from datetime import datetime as dt
from datetime import timezone
from time import ctime

# def utc_to_local(utc_dt):
#     return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

# def ios_dt(ticks):
#     secs = ticks/1000000000
#     utc = dt(2001, 1, 1) + rd(seconds=secs)
#     return utc_to_local(utc)


emoji_map = {
    '\u00e2\u009d\u00a4\u00ef\u00b8\u008f': '❤',
    '\u00e2\u0080\u0099': "'",
    '\u00e2\u0080\u009c': '"',
    '\u00f0\u009f\u0091\u008d': '👍',
    '\u00e2\u0080\u0099': '’',
}


def display_messages(chat):
    line_len = 150
    path = os.path.join(dir, chat, 'message_1.json')
    with open(path, 'r') as fp:
        insta = json.load(fp)
        participants = [x['name'] for x in insta['participants']]
        messages = reversed(insta['messages'])
        title = {insta['title']}
    print(f"{title=}")
    print(f'{participants=}')
    for x in messages: 
        sender = x['sender_name']
        et = x['timestamp_ms']/1000  # epoch_time
        msg = x.get('content')
        if msg:
            for k, v in emoji_map.items():
                msg = msg.replace(k, v)
            print(f"""{sender[0].upper()}: {msg.ljust(line_len)[:line_len]} ... [{ctime(et)}|{sender}]""")

# decode_insta(r'\u00e2\u0080\u0099')
def decode_insta(char):
    char.replace(r'\u00', r'\x')
    b'\xf0\x9f\x91\x8d'.decode('utf-8')  # '👍'

def check_titles(src):
    for file in os.listdir(src):
        path = os.path.join(src, file, 'message_1.json')
        with open(path, 'r') as fp:
            insta = json.load(fp)
            participants = [x['name'] for x in insta['participants']]
            title = insta['title']
        if 'hak' in title.lower() or 'hak' in ''.join(participants).lower() or 'hak' in file.lower():
            print(f'{title=}, {participants=}, {file=}')


if __name__ == '__main__':
    #dir = r'C:\T2\instagram-tamarbezalely-2024-04-29-c741bS8m\your_instagram_activity\messages\inbox'
    #src = r'D:\Instagram_3\your_instagram_activity\messages\inbox'
    dir = r'C:\TT\your_instagram_activity\messages\inbox'
    #check_titles(src)
    display_messages('micheletabaroki_869842227736813')





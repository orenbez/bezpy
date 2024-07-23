# Hack for Debbie G to extract her messages from iphone.
# sqlite database was located here and renamed 3d.db
# iMyfone_SMS_Backup\2019_01_31__10_55_22\acebe377f71e25dc655d71ed3c59bcb725e87ec8\3d\3d0d7e5fb2ce288813306e4d4636395e047a3d28


import pandas as pd 
import sqlite3
import shutil
import sys, os
from datetime import timedelta as td
from dateutil.relativedelta import relativedelta as rd
from datetime import datetime as dt
from datetime import timezone
from pandas import ExcelWriter # needs pip install openpyxl
from tabulate import tabulate

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

# converts ios iphone timestamp to datetime
def ios_dt(ticks):
    secs = ticks/1000000000
    utc = dt(2001, 1, 1) + rd(seconds=secs)
    return utc_to_local(utc)


def dispt(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))


def check_debbie_phone():
    conn = sqlite3.connect('D:\\dump\\3d.sqlite')
    cr = conn.cursor()

    cr.execute("select name from sqlite_master where type = 'table'")
    print(cr.fetchall()) # lists all tables

    # select * from handle where id = '+15169675383';
    # select * from message where handle_id in (366, 365)  order by ROWID ASC
    df = pd.read_sql("select ROWID,text,handle_id,service,account,date, is_from_me from message where handle_id in (366,365)  order by ROWID ASC;", conn)
    df['date'] = [ ios_dt(df['date'].iloc[i]) for i in range(len(df))]


    cr.close()
    conn.close()

    writer = ExcelWriter('DebbieG.xlsx')
    df.to_excel(writer,'iphone_messages', index=False) # name sheet and supress the index column being printed
    writer.save()  # same as writer.close()


def integrity_check(file):
    conn = sqlite3.connect(file)
    cr = conn.cursor()
    try:
        cr.execute("PRAGMA quick_check")
        if os.path.getsize(file) > 0:
            return True
    except sqlite3.DatabaseError:
        #print(f'{file} is an invalid file type')
        conn.close()
    return False


def check_tamar_phone():
    """ returns valid db files as a list"""
    root_dir = r'D:\Media\Media\Library\SMS\Attachments'

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = f'{root}\{file}'
            # if integrity_check(file_path):
            if file.startswith('7463799528'):
                print(file_path)


def check_instagram():
    """ returns valid db files as a list"""
    root_dir = r'D:\Instagram'

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = f'{root}\{file}'
            if file.startswith('ig_'):
                print(file_path)
            # if file.endswith('.db'):
            #     if integrity_check(file_path):
            #         print(file_path)


def read_whats_app():
    # see https://medium.com/@Med1um1/extracting-whatsapp-messages-from-backups-with-code-examples-49186de94ab4
    conn = sqlite3.connect('D:\\dump\\ChatStorage.sqlite')
    cr = conn.cursor()
    #result = pd.read_sql("SELECT NAME FROM sqlite_master WHERE type='table'", conn)
    #dispt(result)

    #result = pd.read_sql("SELECT * FROM ZWAMESSAGE", conn)
    result = pd.read_sql("SELECT * FROM ZWABLACKLISTITEM", conn)

    # List of Columns
    #print('\n'.join([str(i + 1) + ' ' + x for i, x in enumerate(df.columns)]))

    pd.set_option('display.max_columns', 20)  # Max number of columns displayed, note number of columns = df.shape[1]
    pd.set_option('display.width', 5000)  # Max chars display on one line
    pd.set_option('max_colwidth', 200)

    get_df_by_number = lambda df, num: df[df.ZTOJID.str.contains(num).fillna(False) | df.ZFROMJID.str.contains(num).fillna(False)]
    get_df_by_contact_name = lambda df, name: df[df.ZPUSHNAME.str.contains(name).fillna(False)]
    get_df_by_chat_session_id = lambda df, sid: df[df.ZCHATSESSION == sid]
    grep_for_message_text = lambda df, txt: df[df.ZTEXT.str.contains(txt).fillna(False)]
    timestamp_to_apple = lambda x: datetime.fromtimestamp(x) + (datetime.datetime(2001, 1, 1) - datetime.fromtimestamp(0))

    # 01. Z_PK — seems like a serial number
    # 02. Z_ENT to ZFILTEREDRECIPIENTCOUNT — seem less important
    # 03. ZFLAGS — seems to indicate message state
    # 04. ZGROUPEVENTTYPE — seems to be related to group chats
    # 05. ZISFROMME — message is from me… it is 1 for messages sent by this user and 0 for messages received
    # 06. ZMESSAGEERRORSTATUS to ZSPOTLIGHTSTATUS — seems like general statuses
    # 07. ZSTARRED — did we star the message
    # 08. ZCHATSESSION — unique identifier denoting a chat session
    # 09. ZGROUPMEMBER — haven’t gotten to look at this one yet
    # 10. ZLASTSESSION — last chat session? didn’t dig into it
    # 11. ZMEDIAITEM — seems related to media item indexing, might be an identifier to one of the other tables
    # 12. ZMESSAGEINFO and ZPARENTMESSAGE — seem simple enough to figure out from the names
    # 13. ZMESSAGEDATE — message creation date probably (see date format discussion below)
    # 14. ZSENTDATE — message sent date probably (see date format discussion below)
    # 15. ZFROMJID — from who did we get it (if it is an incoming message)
    # 16. ZMEDIASECTIONID — seems related to media storage for media messages, doesn’t show in messages without media
    # 17. ZPHASH - hmmm... not sure
    # 18. ZPUSHNAME — seems like the contact name on your phone
    # 19. ZSTANZAID — some conversation / media id indicator. Format seems different in media messages and text messages
    # 20. ZTEXT — message text
    # 21. ZTOJID — to whom did we send it (if it is an outgoing message)

    df = get_df_by_number(result, '6468730404')
    df[['ZTEXT','ZISFROMME']]
    df[['ZCHATSESSION', 'ZMESSAGEDATE','ZMEDIASECTIONID', 'ZISFROMME', 'ZTEXT']]
    #df2[['ZISFROMME', 'ZCHATSESSION', 'ZMESSAGEDATE', 'ZFROMJID', 'ZTOJID', 'ZMEDIASECTIONID', 'ZTEXT']]


if __name__ == '__main__':
    check_instagram()
    #read_whats_app()
    # with open('table_names.txt') as f:
    #     for line in f:
    #         file = f.readline().strip()
    #         conn = sqlite3.connect(file)
    #         cr = conn.cursor()
    #         cr.execute("select name from sqlite_master where type = 'table'")
    #         result = cr.fetchall()
    #         if result:
    #             print(file, result)

    # with open('table_names.txt') as f:
    #     for line in f:
    #         file_path = f.readline().strip()
    #         if file_path:
    #             file_name = file_path.split('\\')[-1]
    #             dest = 'D:\\iMazing\\dump\\' + file_name + ('.db' if not file_name.endswith('.db') else '')
    #             print(file_path, dest)
    #             shutil.copy2(src=file_path, dst=dest)




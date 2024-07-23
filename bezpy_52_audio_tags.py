# Mutagen is a Python module to handle audio metadata
# Note was unsuccessful with eyed3 to modify ID3 media tags specifically to delete any text in the 'Title' tag

import os
from time import localtime
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd
from mutagen.mp4 import MP4, MP4StreamInfoError


def clean_tags(file):
    try:
        x = MP4(file)  # access meta data for MP4 file
    except MP4StreamInfoError:
        print(f'WARNING: {file} is not a MP4 file')
        return

    try:
        if x['©nam']:  # if file has a 'title'
            x.clear()  # clears all description tags
            x.save()
            print(f'tags removed for {x.filename}')
    except:
        pass


def inspect_files(src):
    # Time stamp 10 days ago from now. Format converted to time.struct_time to compare with modifed time
    ten_days_ago = (dt.now() - rd(days=10)).timetuple()
    os.chdir(src)
    dir = src.replace("D:\\D", "")
    for file in os.listdir():
        if os.path.isfile(file):
            modified = localtime(os.path.getmtime(file))  # Format struct_time for last modified time of file
            if modified > ten_days_ago:  # last modified date is within 10-days
                print(f'Checking ... "D:{dir}\{file}"')
                x = file.rfind('.')
                extension = file[x:]
                if extension in ('.html', '.htm'):
                    new = file[:x] + '.mp4'
                    try:
                        os.rename(file, new)
                    except PermissionError:
                        print(f'{file} is currently in use.')
                        continue
                    else:
                        print(f'renamed file to {new}')
                    clean_tags(new)

                elif extension == '.mp4':
                    clean_tags(file)
                else:
                    continue

dirs = [r'D:\D', 'D:\D\TV', r'D:\D\Movies', r'D:\D\Movie Kids', ]

for src in dirs:
    inspect_files(src)




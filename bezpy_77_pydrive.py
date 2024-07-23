# Access your google drive with python
# https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# 1) Create json file from https://medium.com/@chingjunetao/simple-way-to-access-to-google-service-api-a22f4251bb52
# 2) Requires client_secrets.json in same directory as this script
# 3) ON google cloud platform  APIs & Services -> OAuth consent screen ->  Test Users (then add yourself)
# client_id = '946152693561-61jc0hd02soudbene2e78am4deb1t4u5.apps.googleusercontent.com'

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

folder_id = '1q91gDckI9Npe0QfgTxXytqoVz43d6Nhw'  # FOLDER 'DMV RECORDS'
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

file_dict = {}

for file in file_list:
    if file.get('title').endswith('png'):
        file_dict[file.get('title')] = file.get('embedLink')


x = pd.read_excel('temp.xlsx', sheet_name='Sheet1', skiprows=0, usecols='A:B', dtype=object)
x['VIN'] = x['VIN'] + ".png"
x['LINK'] = x.apply(lambda x: f"""HYPERLINK("{file_dict[x['VIN']]}", "{x['PLATE']}")""", axis=1)
x.to_excel('out.xlsx', sheet_name='Sheet1', index=False, freeze_panes=(1,0))


# Alternatively use library 'gspread'
# READ https://towardsdatascience.com/turn-google-sheets-into-your-own-database-with-python-4aa0b4360ce7
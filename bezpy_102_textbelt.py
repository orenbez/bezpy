import requests

data = {'phone': '5164247985',
        'message': 'Msg for Oren',
        'key': 'textbelt'}   # <--- need api key from https://textbelt.com/ for more than one free text
          

resp = requests.post('https://textbelt.com/text', data=data)
r = resp.json()

# Examples 
# {"success": true, "quotaRemaining": 40, "textId": 12345}
# {"success": false, "quotaRemaining": 0, "error": "Out of quota"}
# {"success": false, "error": "Incomplete request"}


#  $3/50 texts
#  $5/200 texts
#  $10/1000 texts
#  $23/2500 texts
#  $45/5000 texts



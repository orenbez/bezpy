# TRY THIS: https://hackingandslacking.com/ssh-scp-in-python-with-paramiko-6f864d48c1aa?source=bookmarks---------1----------------------------
# https://medium.com/featurepreneur/ssh-in-python-using-paramiko-e08fd8a039f7

# SFTP (Secure File Transfer Protocol)
# SCP(Secure Copy Protocol).

# REQUIRES pip install paramiko

import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # validate your trust with the machine for the first time you try to connect to the server.
ssh_client.connect(hostname='hostname', port='PORT', username='dummy', password='mypassword')


USERNAME = 'username'
PASSWORD = 'pass'
PRIVATE_KEY_FILE = 'file'

# Alternatively for Password and Private key-based auth:
transport = paramiko.Transport()
transport.start_client()
transport.auth_password(USER_NAME, PASSWORD)
pkey = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE) transport.auth_publickey(USER_NAME, pkey)



OTP = 'otp'
# For Password and OTP-based auth:
transport = paramiko.Transport()
transport.start_client()
transport.auth_interactive(username, handler)
def handler(self, title, instructions, prompt_list):
  answers = []
  for prompt_, _ in prompt_list:
    prompt = prompt_.strip().lower()
    if prompt.startswith('password'):
      answers.append(PASSWORD)
    elif prompt.startswith('verification'):
      answers.append(OTP)
    else:
      raise ValueError('Unknown prompt: {}'.format(prompt_))
  return answers



import keyring    # requires pip install keyring
# import keyrings.alt # this is required for linux platforms
# import hvac # this is for Hashicorp Vault
# Sets and retreives passwords from 
# Windows "Control Panel\User Accounts\Credential Manager"
# TO ADD MANUALLY in Credential Manager: Generic Credential -> 'add a Generic Credential"
# Note that the 'Windows Credentials -> Windows Credentials" settings are for credentials accessed by windows' own applications only and Windows OS
# Note that the 'Windows Credentials -> Generic Credentials" settings are for credentials accessed by all other applications
# see https://keyring.readthedocs.io/en/latest/


keyring.set_password('group-name', 'user1' ,'pass1')  # Sets up in Windows Credentials -> Generic Credentials
keyring.set_password('groupname2', 'user2' ,'pass2')  # Sets up in Windows Credentials -> Generic Credentials. Stored under 'groupname2'
keyring.set_password('groupname2', 'user3' ,'pass3')  # Sets up in Windows Credentials -> Generic Credentials  (ADDS TO groupname2). Note now stores 'user2'  under 'user2@groupname2' and user3 as 'groupname2'

keyring.get_password('groupname2', 'user2')      # pass2
keyring.get_password('groupname2', 'user1')      # will fail silently since no such group/user combination and return None
keyring.get_password('groupname2', None)         # returns None

cred = keyring.get_credential('groupname2', 'user2') # returns credential object
cred.username   # user2
cred.password   # pass2

cred = keyring.get_credential('groupname2', None)  # You have two users and not specified which one you want, returns the latest user that was added 
cred.username   # user3
cred.password   # pass3

cred = keyring.get_credential('groupname2', 'user4')  # user4 does not exist but will capture the latest user as above 
cred.username   # user3
cred.password   # pass3

cred = keyring.get_credential('group-name', None)  # Only one user in this group, so you are not required to specify
cred.username   # user1
cred.password   # pass2
cred = keyring.get_credential('missing-group-name', None)  # this will return None since 'missing-group-name' is not stored

try:
    keyring.delete_password('groupname', 'passKey1')
except keyring.errors.PasswordDeleteError: 
    print('Unable to delete password')


# also note configuration file settings and the .set_keyring() method
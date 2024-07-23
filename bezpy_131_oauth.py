# https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
# Video: https://oauth.net/
# https://blog.miguelgrinberg.com/post/oauth-authentication-with-flask
# https://pythonhosted.org/Flask-OAuth/
# https://flask-oauthlib.readthedocs.io/en/latest/oauth2.html


# OAuth2 Tutorial

# =================================================================================================================================
# 4 Roles
# =================================================================================================================================
# 1. Resource Owner: The resource owner is the user who authorizes an application to access their account. e.g Google
# 2. Client: The client is the application that wants to access the user’s account. e.g YOU
# 3. Resource Server: The resource server hosts the protected user accounts.  e.g any application
# 4. Authorization Server: The authorization server verifies the identity of the user then issues access tokens to the application.


# 1. Authorization Code Link: Resource Owner e.g. google receives authorization request from client
#       https://cloud.digitalocean.com/v1/oauth/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=CALLBACK_URL&scope=read
# 2. Client clicks 'accept'
# 3. Application recieves Authorization Code
#       https://dropletbook.com/callback?code=AUTHORIZATION_CODE
# 4. Application requests Access Token with AUTH CODE and some client secret
#       https://cloud.digitalocean.com/v1/oauth/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=CALLBACK_URL
# 5. Application Receives Access Token
#       {"access_token":"ACCESS_TOKEN","token_type":"bearer","expires_in":2592000,"refresh_token":"REFRESH_TOKEN","scope":"read","uid":100101,"info":{"name":"Mark E. Mark","email":"mark@thefunkybunch.com"}}


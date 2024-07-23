# ======================================================================================================================
# http:  module from the standard library, provides a HTTP client interface.

# The following modules appear to have been removed from the standard library
# httplib, Cookie, ipaddr, htmlentitydefs, httpauth
# ======================================================================================================================
# also see bezpy_25_call_api.py

# http.client    low-level HTTP protocol client
# http.server    basic HTTP server classes based on socketserver
# http.cookies
# http.cookiejar

import http.client
conn = http.client.HTTPSConnection("medium.com")
conn.request("GET", "/")
r = conn.getresponse()
print(f'status={r.status}')
l = r.readlines()  # list of html lines in binary



import http.server
PORT = 8888
server_address = ("", PORT)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Server active on the port :", PORT) # Server active on the port : 8888
httpd = server(server_address, handler)
httpd.serve_forever()   # You can check the server on localhost:8888

# ======================================================================================================================
# Http Status Codes
# ======================================================================================================================
# 200 – OK. The request was successful. The answer itself depends on the method used (GET, POST, etc.) and the API specification.
# 201 - Created – request fulfilled and new resource created (POST/PUT)
# 204 – No Content. The server successfully processed the request and did not return any content.
# 301 – Moved Permanently. The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.
# 400 – Bad Request. The server cannot process the request because the client-side errors (incorrect request format).
# 401 – Unauthorized. Occurs when authentication was failed, due to incorrect credentials or even their absence.
# 403 – Forbidden. Access to the specified resource is denied.
# 404 – Not Found. The requested resource was not found on the server.
# 405 - Method Not Allowed, unless you want to modify the collection itself
# 500 – Internal Server Error. Occurs when an unknown error has occurred on the server.




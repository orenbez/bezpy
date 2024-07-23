import requests           # Use the requests library to simplify making a REST API call from Python
from bezpy_11_send_email import send
from time import sleep 

count = 0
while True:
    count +=1
    url2 = 'https://shop.parks.ny.gov/store/special-events'

    print (f'Attempt: {count}')
    try:
        response2 = requests.get(url2)       # response object
    except requests.exceptions.ConnectionError:
        print('requests.exceptions.ConnectionError')
        continue
    print(response2.status_code, bool(response2)) # True if the response is < 400
    sleep(15)
    if bool(response2):
        send(['obezalely@tscinsurance.com'], 'WEBSITE OPEN', 'in')

    # Http Status Codes
    # 200 – OK. The request was successful. The answer itself depends on the method used (GET, POST, etc.) and the API specification.
    # 201 - Created – request fulfilled and new resource created (POST/PUT)
    # 204 – No Content. The server successfully processed the request and did not return any content.
    # 301 – Moved Permanently. The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.
    # 400 – Bad Request. The server cannot process the request because the client-side errors (incorrect request format).
    # 401 – Unauthorized. Occurs when authentication was failed, due to incorrect credentials or even their absence.
    # 403 – Forbidden. Access to the specified resource is denied.
    # 404 – Not Found. The requested resource was not found on the server.
    # 500 – Internal Server Error. Occurs when an unknown error has occurred on the server.




# accessing data via SOAP API
# https://medium.com/@kazitoufiq/using-python-zeep-package-for-accessing-data-via-soap-api-9f5e2e7a6c11
# https://python-zeep.readthedocs.io/en/master


# https://webkul.com/blog/python-soap-clients-with-zeep/
# Working with SOAP based web services can sometimes be a time taking task when you have to write the complete XML for making API requests and then parse the response xml to fetch the desired results.
# The best thing about Zeep is that you don’t have to write the XML at all. You just create a dictionary with all the relevant request data, and it will create the XML for you.

# Requires `pip install zeep`
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport

wsdl = "https://wsvc.cdiscount.com/MarketplaceAPIService.svc?wsdl"

session = Session()
session.auth = HTTPBasicAuth('<username>', '<password>')

#An additional argument 'transport' is passed with the authentication details
client = Client(wsdl, transport=Transport(session=session))
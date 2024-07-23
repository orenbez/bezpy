# https://pypi.org/project/WooCommerce/  API version 3.0.0
# API Documentation: https://woocommerce.github.io/woocommerce-rest-api-docs/#introduction
from pprint import pprint
from woocommerce import API

# Generate API credentials:  WooCommere -> Settings -> Advanced Settings -> Rest API
# Database File Path: /home1/ecusadco/public_html/wp-content/uploads/woocommerce_uploads/86KW1JyR1qkKmvHoYqeS227BNKcsJYgF-GeoLite2-Country.mmdb

# -------------------------------------------------------------
# Option|Type |Required| Description
# -------------------------------------------------------------
# url|string|yes|Your Store URL, example: http://woo.dev/
# consumer_key|string|yes|Your API consumer key
# consumer_secret|string|yes|Your API consumer secret
# version|string|noAPI version, default is wc/v3
# timeout|integer|no|Connection timeout, default is 5
# verify_ssl|bool|no|Verify SSL when connect, use this option as False when need to test with self-signed certificates
# query_string_auth|bool|no|Force Basic Authentication as query string when True and using under HTTPS, default is False
# user_agent|string|no|Set a custom User-Agent, default is WooCommerce-Python-REST-API/3.0.0
# oauth_timestamp|integer|no|Custom timestamp for requests made with oAuth1.0a
# wp_api|bool|no|Set to False in order to use the legacy WooCommerce API (deprecated)

URL = 'http://box5726.temp.domains/~ecusadco'
CONSUMER_KEY = 'ck_68f7b6bf1ac194d36ec5fb8fc542da38b0a1e3dc'
CONSUMER_SECRET = 'cs_5f38097c81569dc65d70d1563ddcdfe7c2b99c2f'
VERSION = "wc/v3"
wcapi = API(url=URL,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            version=VERSION)

# endpoint|string|WooCommerce API endpoint, example: 'customers', 'products', 'order/12'
# data|dictionary|Data that will be converted to JSON

# wcapi.get(endpoint, **kwargs)
# wcapi.post(endpoint, data, **kwargs)
# wcapi.put(endpoint, data), **kwargs
# wcapi.delete(endpoint, **kwargs)
# wcapi.options(endpoint, **kwargs)


pprint(wcapi.get("products").json())
pprint(wcapi.get("customers").json())

# >>> r = wcapi.get("products")
# >>> r.status_code # 200
# >>> r.headers['content-type'] # 'application/json; charset=UTF-8'
# >>> r.encoding # 'UTF-8'
# >>> r.text # u'{"products":[{"title":"Flying Ninja","id":70,...' // Json text
# >>> r.json()# {u'products': [{u'sold_individually': False,... // Dictionary data
# >>> wcapi.delete("products/100", params={"force": True}).json()
# >>> wcapi.get("products", params={"per_page": 20})
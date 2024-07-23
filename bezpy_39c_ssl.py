# SSL module is a standard Python module and is widely used across the Python ecosystem, especially for distributed systems with programs that need to communicate securely
# https://docs.python.org/3/library/ssl.html
# provides functions and classes to use the following to secure communication both server and client side:
# Secure Sockets Layer (SSL)   -- now deprecated (since 2011 for SSLv2 and 2015 for SSLv3)
# Transport Layer Security (TLS)   -- developers should use at least TLS 1.1 

import ssl  
ssl.get_default_verify_paths()
# DefaultVerifyPaths(cafile=None, capath=None, openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='C:\\Program Files\\Common Files\\SSL/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='C:\\Program Files\\Common Files\\SSL/certs')

# remote = ssl.wrap_socket(s, ca_certs= CA, cert_reqs=ssl.CERT_REQUIRED, ssl_version = ssl.PROTOCOL_SSLv3)  -- DEPRECATED
# remote = ssl.wrap_socket(s, ca_certs= CA, cert_reqs=ssl.CERT_REQUIRED, ssl_version = ssl.PROTOCOL_TLS)

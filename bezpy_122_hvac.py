# For Hashicorp Vault, use keyring library for windows credential vault
# https://hvac.readthedocs.io/en/stable/overview.html
# requires `pip install hvac`    # currently  hvac-2.0.0

import hvac

class HashicorpVaultExample:

    def __init__(self, url, token, verify=False, namespace=None):
        self.url = url
        self.token = token
        self.namespace = namespace
        self.verify = verify

    def get_client(self):
        self.client = hvac.Client(url=self.url, token=self.token, verify=self.verify, namespace=self.namespace)
        if self.client.is_authenticated():
            pass
        else:
            raise Exception("Invalid Hashicorp Vault Token Specified")

    def new_secret(self, service_id):
        return self.client.create_role_secret_id(role_name=service_id)['data']['secret_id']

    def secret_version(self, group_id):
        return self.client.secrets.kv.v2.read_secret_version(path=group_id)['data']['data']   # <-- this is for the KV Version_2 Engine

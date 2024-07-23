# tomlib is in the standard library as of 3.11
# TOML is a file format for configuration files.  (c.f with  JSON, INI, YAML, HOCON)
# TOML = Tom's Obvious, Minimal Language
# A new module for parsing TOML files (WRITING NOT YET SUPPORTED)
# READ ME: https://realpython.com/python-toml


import tomllib
from pprint import pprint

# FILES
with open(r'.\myfiles\settings.toml', 'rb') as f:
    data = tomllib.load(f)
pprint(data)

# STRINGS
settings = """
[python]
version = 3.11
release_manager = "Pablo Galindo Salgado"
is_beta = true
beta_release = 3
release_date = 2022-06-01
peps = [657, 654, 678, 680, 673, 675, 646, 659]

[toml]
version = 1.0
release_date = 2021-01-12
"""
data = tomllib.loads(settings)
pprint(data)
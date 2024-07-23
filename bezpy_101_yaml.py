# YAML is a human-readable data-serialization language. 
# YAML files are created with extensions “.yml” or “.yaml”
# It is a superset of JSON with additional features such as comments, anchors, alias etc
# It is commonly used for configuration files and in applications where
# data is being stored or transmitted. YAML targets many of the same communications applications as XML but has a
# minimal syntax which intentionally differs from SGML. It uses both Python-style indentation to indicate nesting,
# and a more compact format that uses [...] for lists and {...} for maps thus JSON files are valid YAML 1.2.
# data types supported by YAML are boolean, string, integer, float, arrays, dictionaries

# READ https://realpython.com/python-yaml/
# READ https://dev.to/developertharun/yaml-tutorial-using-yaml-with-python-pyyaml-443d
# READ THIS https://betterprogramming.pub/10-things-you-might-not-know-about-yaml-b0589da547c

import yaml  # requires 'pip install pyyaml'

d = {"name": "Colbeh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}


# Returns yaml string
yaml.dump(d)  

# Writes yaml file
with open(r'.\myfiles\sample_out.yaml', 'w') as y:
    yaml.dump(d, y)                # Note: dump vs safe_dump (only stores simple yaml tags for safety)

# reads yaml file as a dictionary
with open(r'.\myfiles\sample_out.yaml', "r") as str:
    result = yaml.safe_load(str)   # Note: load vs safe_load (only reads simple yaml tags for safety)
    result.get('name') # Colbeh
# except yaml.YAMLError
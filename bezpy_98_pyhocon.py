# ===========================================================================================================
# pyhocon is a HOCON (Human-Optimized Configuration Object Notation) parser for Python
# requires `pip install pyhocon`
# ===========================================================================================================
# Documentation: https://pythonhosted.org/pyhocon/
# It is new format which is super set of JSON file type
# It is used to store configuration file like toml or ini
# hocon files created with extension .conf or .hocon

# ===========================================================================================================
# HOCON SYNTAX RULES
# ===========================================================================================================
# 1. parenthesis ({}) to Root element is ignored
# 2. You can use key and value with separator (: or =)
# 3. Double quotes to key and values are not required and optional
# 4. Single Quotes will fail if used for keys but will be recognized as part of the value i.e. \'  char  in the value (see sample2.hocon)
# 4. Objects or array attributes are separated by new line
# 5. Comments always starts with # or //
# 6. Key/Values are case sensitive
# 7. Tabs are not allowed, Some editors allows spaces

# -----------------------------------------------------------------
# array/list values
# -----------------------------------------------------------------
#   emptyArray: []
#   intArray: [11, 12, 13]
#   stringArray: ["one", "two", "three"]
#   booleanArray: [true, false]

# -----------------------------------------------------------------
# nesting (dev1 & dev2 are the same)
# -----------------------------------------------------------------
# dev1: {
#         username: username,
#         password: password,
# }
# dev2 {
#         username: username,
#         password: password,
# }

# -----------------------------------------------------------------
# comments  (extension to JSON)
# -----------------------------------------------------------------
# // this is inline comment 
# '#' this is another inline comment

# NOTE use '\#' to add '#' to a value IN THE HOCON FILE

#
# ------------------------------------------------------------------------------------
# include statements are allowed to append to the configuration   (extension to JSON)
# ------------------------------------------------------------------------------------
# include "database.conf"   <---- this adds to the configuration from an external file, use double quotes
# dev: {
#   hostname: dev.site.com,   <-------- note dev.site.com is one string
#   username: username,
#   password: password,
#   key1.key2: value          <-------- note key1.key2 is a path, full path is dev.key1.key2
# }
#
# -----------------------------------------------------------------
# Substitution variable using ${} syntax  (extension to JSON)
# -----------------------------------------------------------------
# devprofile {
#       hostname: dev
#     }
#  devpath: ${devprofile.hostname}:8080   <--------- value="dev:8080"
# ===========================================================================================================


from pyhocon import ConfigFactory       # same as 'from pyhocon.config_parser import ConfigFactory'
from pyhocon import ConfigTree          # same as 'from pyhocon.config_tree import ConfigTree'
from pyhocon import HOCONConverter
from pyhocon.exceptions import ConfigMissingException, ConfigException
from pyparsing.exceptions import ParseException


hocon_file_path1 = r'.\myfiles\sample.hocon'
hocon_file_path2 = r'.\myfiles\sample2.hocon'
hocon_string =  """// braces {} for root values not required
                    application=myapp
                    "key"="value",
                    dev: {
                            host: dev.com
                            port: 8080   # xxx
                            a.b: XXX
                    }
                    test {
                            host: test.com  // comment 1
                            port: 8081      # comment 2
                    }
                    role: {
                            id: 24
                            name: 'admin'
                            active: false
                    }
                    all: {
                                roles: [
                                admin
                                sales
                                support
                                ]
                            }
                    devprofile {
                        hostname: dev
                    }
                    devpath: ${devprofile.hostname}:8080
                    types:{
                              config_tree_value={key:value}
                              list_value=[1, 2, 3]
                              string_value='test   '
                              int_value=42
                              float_value=3.14
                              bool_value=true
                              null_value=null  
                    }"""

def get_config_tree_from_file(path) -> ConfigTree:
    return ConfigFactory.parse_file(path)   # I think default parameter is resolve=True to resolve substitutions


def get_config_tree_from_string(strg) -> ConfigTree:
    return ConfigFactory.parse_string(strg)   # I think default parameter is resolve=True to resolve substitutions


config_tree = get_config_tree_from_file(hocon_file_path1)
assert config_tree.get('devpath') == 'dev:8080'

config_tree = get_config_tree_from_file(hocon_file_path2)
assert config_tree.get('key a') == 'value'
assert config_tree.get('key f') == 'value'
assert config_tree.get('key27') == "'value'"

res_json = HOCONConverter.to_json(config_tree)                # converts to json string
res_properties = HOCONConverter.to_properties(config_tree)    # converts to properties string  (.properties file, simmilar to .ini)
res_yaml = HOCONConverter.to_yaml(config_tree)                # converts to yaml string

ct = get_config_tree_from_string(hocon_string)     # config tree is like an OrderedDict
assert ct.get('application') == 'myapp'
assert ct.get('dev').get('host') == 'dev.com'
assert ct.get('dev.host') == 'dev.com'
assert ct.get('dev.a') == ConfigTree([('b', 'XXX')])   # compare with OrderedDict([('b', 'XXX')])   # this is a sub config_tree
assert ct.get('dev.a.b') == 'XXX'
assert ct.get('test.host') == 'test.com'
assert ct.get('test2.host', 'missing_key') == 'missing_key'  # submit a default value which is returned as 'test2.host' does not exist
assert ct['test']['port'] == 8081    # implicitly requests int
assert ct.get_int('role.id') == 24   # explicitly requests int, will raise exception if not int
assert ct.get('role.active') == False
assert ct.get('all.roles') == ['admin', 'sales', 'support']
assert ct.get('devpath') == 'dev:8080'

# These are all True
assert isinstance(ct.get_config('types'), ConfigTree)
assert isinstance(ct.get_config('types.config_tree_value'), ConfigTree)
assert isinstance(ct.get_list('types.list_value'), list)
assert isinstance(ct.get_string('types.string_value'), str)
assert isinstance(ct.get_int('types.int_value'), int)
assert isinstance(ct.get_float('types.float_value'), float)
assert isinstance(ct.get_bool('types.bool_value'), bool)
assert ct.get('types.null_value') is None
assert ct.get('types.bool_value') is True
assert ct.get_bool('types.bool_value') is True


ct.put('dev.user_id', 'oren')  # adds to ConfigTree

from pprint import pprint
pprint(ct)
# ConfigTree([('application', 'myapp'),
#             ('dev',
#              ConfigTree([('host', 'dev.com'),
#                          ('port', 8080),
#                          ('user_id', 'oren')])),
#             ('test', ConfigTree([('host', 'test.com'), ('port', 8080)])),
#             ('role',
#              ConfigTree([('id', 24), ('name', "'admin'"), ('active', False)])),
#             ('all', ConfigTree([('roles', ['admin', 'sales', 'support'])])),
#             ('devprofile', ConfigTree([('hostname', 'dev')])),
#             ('devpath', 'dev:8080'),
#             ('types',
#              ConfigTree([('config_tree_value', ConfigTree([('key', 'value')])),
#                          ('list_value', [1, 2, 3]),
#                          ('string_value', "'test   '"),
#                          ('int_value', 42),
#                          ('float_value', 3.14),
#                          ('bool_value', True),
#                          ('null_value', None)]))])

hocon_string2 = """application=myapp1
                   application2=myapp2"""

ct2 = ConfigFactory.parse_string(hocon_string2) 
ct.update(ct2)   # will update in-place the key-values of ct with entries in ct2, replacing values with those in ct2 where there are conflicts.  c.f. dict1.update(dict2)
assert ct2.get('application') == 'myapp1'
assert ct2.get('application2') == 'myapp2'

# ct.as_plain_ordered_dict()          #  returns ordered dictionary
# ct.put(key, value)                  #  sets key value pair
# ct.get()                            #  returns value
# ct.get_bool()                       #  returns value, raising exception if incorrect type
# ct.get_config()                     #  returns value, raising exception if incorrect type
# ct.get_float()                      #  returns value, raising exception if incorrect type
# ct.get_int()                        #  returns value, raising exception if incorrect type
# ct.get_list()                       #  returns value, raising exception if incorrect type
# ct.get_string()                     #  returns value, raising exception if incorrect type
# ct.history

# ct.clear()                          # c.f. with dict
# ct.copy()                           # c.f. with dict
# ct.fromkeys(['key1', 'key2'], 4)    # c.f. with dict
# ct.keys()                           # c.f. with dict
# ct.values()                         # c.f. with dict
# ct.items()                          # c.f. with dict
# ct.pop()                            # c.f. with dict
# ct.popitem()                        # c.f. with dict
# ct.setdefault()                     # c.f. with dict
# ct.update()                         # c.f. with dict


# ct.merge_configs(a, b)              # merge ConfigTree 'b' into ConfigTree 'a'
# ct.move_to_end                      #
# ct.parse_key                        #
# ct.resolve                          #
# ct.root                             #
# ct.with_fallback                    #

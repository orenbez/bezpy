# TRY THIS: https://towardsdatascience.com/working-with-json-in-python-a53c3b88cc0
# TRY THIS: https://towardsdatascience.com/single-line-of-code-to-interchange-between-python-objects-and-json-b0f23fbaaa65
# READ ME: https://towardsdatascience.com/you-must-know-python-json-dumps-but-maybe-not-all-aspects-fa8d98a76aa0
# ======================================================================================================================
#   STORING DATA WITH JSON - JavaScript Object Notation  (PREFERRED OVER XML)
# ======================================================================================================================
#   JSON vs XML Comparison
#   XML is document-oriented, and is more secure.
#   JSON is data-oriented, faster and generally preferred as the structure is simpler and resembles a python dictionary
# ======================================================================================================================
#   Use Notepad++->Plugins->Json Viewer->'Format Json' & 'Show Json Viewer'
#   https://jsoncrack.com/ to visualize the data
#   https://www.jsonlint.com/ to validate the data
# ======================================================================================================================
#   loads(json_string):         LOAD STRING:    json_string -> python_dict  (deserialize a JSON string to a Python object)
#   load(json_file):            LOAD FILE:      json_file -> python_dict    (deserialize a JSON file to a Python object)
#   dumps(json_dict):           DUMP TO STRING: json_dict -> json_string (serializing python object to json string)
#   dump(json_dict,json_file):  DUMP TO FILE:   json_dict -> json_file   (serializing python object to json file)
# ======================================================================================================================

import numpy
import json
from datetime import datetime, date
import re

# these are the json basic types
# =========================
# Python      |  JSON     #
# =========================
# dict	      |  object   #
# list/tuple  |	 array    #
# str	      |  string   #
# int/float	  |  number   #
# True	      |  true     #
# False	      |  false    #
# None	      |  null     #
# ==========================

# ======================================================================================================================
#   loads(s): converts Json String -> Python object.
#             WARNING: All KEYS in JSON must be strings with DOUBLE QUOTES e.g  "name", "age", "city"  "0", "1"
# ======================================================================================================================
# 's' represents string, 'd' represents dictionary
# WARNING: MUST USE DOUBLE QUOTES FOR STRINGS ******************************************
json.loads('null')         # JSON null   -> Python NoneType  None
json.loads('"string"')     # JSON string -> Python str       'string'
json.loads('"true"')       # JSON string -> Python str       'true'
# json.loads('string')  ->  json.decoder.JSONDecodeError
json.loads('234.1')        # JSON number -> Python float     234.1
json.loads('234')          # JSON number -> Python int       234
json.loads('true')         # JSON bool   -> Python bool      True
json.loads("true")         # JSON bool   -> Python bool      True
json.loads('''true''')     # JSON bool   -> Python bool      True
json.loads('[1,2,3]')      # JSON array  -> Python list      [1, 2, 3]
# json.loads('(1,2,3)')  ->  json.decoder.JSONDecodeError
s1 = '{"name":"John", "age":30, "city":"New York"}'                     # json object
s2 = '''[{"name":"John","age":30}, {"name":"Fred","age":20}]'''         # using triple quotes ''' for clarity that this is a json string
s3 = '''{"0":{"name":"John","age":30},"1":{"name":"Fred","age":20}}'''  # Requires double quotes for "0" & "1"
d1 = json.loads(s1)  # JSON 'object'          -> Python Dict
d2 = json.loads(s2)  # JSON array of objects  -> Python List of Dicts
d3 = json.loads(s3)  # JSON nested objects    -> Python nested Dicts

d1['age']           # returns 30
d2[0]['age']        # returns 30
d3['0']['age']      # returns 30


# Using the object_hook field to handle exceptions loading  JSON -> Python
# we want a datetime isoformated string to convert to a date object
def parse_isodates(dct):
    """recursively parses dictionary to replace isoformat dates with python dates"""
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    for k, v in dct.items():
        if isinstance(v, dict):
            parse_isodates(v)
        elif isinstance(v, str) and re.match(regex, v):
            dct[k] = datetime.fromisoformat(v)
    return dct

json_obj = '{"node1": "2021-12-30T08:36:19", "node2": {"date": "2021-12-30T08:36:19"}}'
dct = json.loads(json_obj, object_hook=parse_isodates)
print(dct)    # {'node1': datetime.datetime(2021, 12, 30, 8, 36, 19), 'node2': {'date': datetime.datetime(2021, 12, 30, 8, 36, 19)}}

# ======================================================================================================================
# dumps(d): converts Python Variable -> Json String.
# ======================================================================================================================
# json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
# Parameters:
#   obj:            Serialize obj as a JSON formatted stream
#   skipkeys:       If skipkeys is True (default: False), then dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of raising a TypeError.
#   ensure_ascii:   If ensure_ascii is True (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is False, these characters will be output as-is.
#   check_circular: If check_circular is False (default: True), then the circular reference check for container types will be skipped and a circular reference will result in an OverflowError (or worse).
#   allow_nan:      If allow_nan is False (default: True), then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification. If allow_nan is True, their JavaScript equivalents (NaN, Infinity, -Infinity) will be used.
#   indent:         If indent is a non-negative integer or string, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0, negative, or “” will only insert newlines. None (the default) selects the most compact representation. Using a positive integer indent indents that many spaces per level. If indent is a string (such as “\t”), that string is used to indent each level.
#   separators:     If specified, separators should be an (item_separator, key_separator) tuple. The default is (‘, ‘, ‘: ‘) if indent is None and (‘, ‘, ‘: ‘) otherwise. To get the most compact JSON representation, you should specify (‘, ‘, ‘:’) to eliminate whitespace.
#   default:        If specified, default should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.
#   sort_keys:      If sort_keys is True (default: False), then the output of dictionaries will be sorted by key.
#
#   Note: If you use a Numeric value as the key of a python dict it will be converted to a string in the json string.
#         python strings do NOT need to be in double quotes, they will be converted to json strings with double quotes
# ======================================================================================================================
d = {"name": "John", "age":30, "city": "New York"}   # Python Dictionary
s = json.dumps(d) # Converts to Json String '{"name": "John", "age": 30, "city": "New York"}'


# all of the below will also be converted to json strings
json.dumps("hello")                   # = '"hello"'                    str   -> Json string
json.dumps('hello')                   # = '"hello"'                    str   -> Json string
json.dumps(42)                        # = '42'                         int   -> Json number
json.dumps(31.76)                     # = '31.76'                      float -> Json number
json.dumps(True)                      # = 'true'                       bool  -> Json bool
json.dumps(False)                     # = 'false'                      bool  -> Json bool
json.dumps(None)                      # = 'null'                       None  -> Json null
json.dumps(['apple', 'bananas'])      # = '["apple", "bananas"]'       list  -> Json array
json.dumps(('apple', 'bananas'))      # = '["apple", "bananas"]'       tuple -> Json array
json.dumps({1: 'one', 2: 'two'})      # = '{"1": "one", "2": "two"}'   dict  -> Json object
json.dumps({'1': 'one', '2': 'two'})  # = '{"1": "one", "2": "two"}'   dict  -> Json object
json.dumps(float('nan'))              # 'NaN'
json.dumps(numpy.nan)                 # 'NaN'


# dict -> Json object
json.dumps({"json_object": {'one': 1}, "json_array":[1,2,3], "json_string": "abc", "json_number": 123.4, "json_bool": True, "json_null": None})
# returns '{"json_object": {"one": 1}, "json_array": [1, 2, 3], "json_string": "abc", "json_number": 123.4, "json_bool": true, "json_null": null}'


# TypeError: Object of type set is not JSON serializable
non_serializable = ({1, 2, 3}, numpy.int64(3), datetime(2000, 1, 1, 23, 59, 59), date(2020, 1, 1), 3 + 2j, b'hello')
for i in non_serializable:
    try:
        json.dumps(i)
    except TypeError:        
        print(f'{type(i)} is non-serializable')

# <class 'set'> is non-serializable
# <class 'numpy.int64'> is non-serializable      
# <class 'datetime.datetime'> is non-serializable
# <class 'datetime.date'> is non-serializable
# <class 'complex'> is non-serializable
# <class 'bytes'> is non-serializable

# keys of a dictionary that you are converting to JSON can only be str, int, float, bool or None, not tuple. otherwise you will get a TypeError
# Use skipkeys to ignore error ... TypeError: keys must be str, int, float, bool or None, not tuple
json.dumps( {1: 'one', (1, 2): 'will be skipped'}, skipkeys=True)  # '{"1": "one"}'

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}],
  "_comment1": "add a comment like this",
  "__comment__": "or add a comment like this"
  }

# prints the whole json object as string and can format the string
print(json.dumps(x,
                 indent=4,  # indents string output
                 separators=("**", " -> "), # changes default seperators  from ','  to '**' (end of value)  and from  ':' to ' -> ' (end of key)
                 sort_keys=True, # orders keys in JSON
                 ))

# ======================================================================================================================
# Using json.dump() to Store some json data in a .json text file 
# json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,  allow_nan=True,
#           cls=None, indent=None, separators=None, default=None,  sort_keys=False, **kw)
# ensure_ascii=False will not limit text to ascii
# default=json_encoder  you can write your own encoder to handle serialization of any object to JSON (see below)
# cls=
# ======================================================================================================================
# METHOD 1: serializing an object to JSON using an Encoder Function
# ======================================================================================================================
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

def json_encoder(p : Person):
    if isinstance(p, Person):
        return {'name' : p.name, 'age': p.age}
    return TypeError(f'{p} is not of type Person')

p = Person('Fred', 12)

# json.dumps(p)  # TypeError: Object of type Person is not JSON serializable
json.dumps(p, default=json_encoder) # Serialized to JSON  '{"name": "Fred", "age": 12}'


# ======================================================================================================================
# METHOD 2: serializing an object to JSON using an Encoder Class
# ======================================================================================================================
class PersonEncoder(json.JSONEncoder):
    # overridew the 'default' function
    def default(self, p: Person):
        if isinstance(p, Person):
            return {'name' : p.name, 'age': p.age}
        return super().default(p)  # raises type error

json.dumps(p, cls=PersonEncoder) # Serialized to JSON  '{"name": "Fred", "age": 12}'


# ======================================================================================================================
# json.dump()
# ======================================================================================================================
# if keys are not strings, they will be converted to strings in the .json file
data ={101: {"class": "X", "Name": "Rohit",  "Roll_no": 7},
       102: {"class": "Y", "Name": "David",  "Roll_no": 8},
       103: {"class": "Z", "Name": "Müller", "Roll_no": 12}}

fp = '.\myfiles\data.json'  # file path
with open(fp, 'w') as f_obj:
    json.dump(data, f_obj) # Dumps Dict->JSON File Returns None

# {"101": {"class": "X", "Name": "Rohit", "Roll_no": 7}, "102": {"class": "Y", "Name": "David", "Roll_no": 8}, "103": {"class": "Z", "Name": "M\u00fcller", "Roll_no": 12}}

# ======================================================================================================================
# Using json.load() to read data - Load some previously stored numbers
# json.load(fp, cls=None, object_hook=None, parse_float=None,parse_int=None,
#           parse_constant=None, object_pairs_hook=None, **kw)
# ======================================================================================================================
try:
    with open(fp, 'r') as f_obj:
        json_dict2 = json.load(f_obj) # loads json file -> python dict
except FileNotFoundError:
    print("Can’t find " + fp)
else:
    print(json_dict2['103']['Name']) # Returns Müller

from pprint import pprint, PrettyPrinter # built-in-module 'pretty print'



d = {1: {'name': 'John', 'age': '27', 'sex': 'Male', 'scores': [78, 88, 99, 59]},
     2: {'name': 'Marie', 'age': '22', 'sex': 'Female', 'scores': [44, 88, 65, 59]},
     3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'scores': [71, 82, 99, 59]},
     4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'scores': [98, 33, 99, 59]}}


print(d)
# {1: {'name': 'John', 'age': '27', 'sex': 'Male', 'scores': [78, 88, 99, 59]}, 2: {'name': 'Marie', 'age': '22', 'sex': 'Female', 'scores': [44, 88, 65, 59]}, 3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'scores': [71, 82, 99, 59]}, 4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'scores': [98, 33, 99, 59]}}

pprint(d)   # prints dictionary to screen in staggered format if exceeds line length


# {1: {'age': '27', 'name': 'John', 'scores': [78, 88, 99, 59], 'sex': 'Male'},
#  2: {'age': '22', 'name': 'Marie', 'scores': [44, 88, 65, 59], 'sex': 'Female'},
#  3: {'age': '24', 'name': 'Luna', 'scores': [71, 82, 99, 59], 'sex': 'Female'},
#  4: {'age': '29', 'name': 'Peter', 'scores': [98, 33, 99, 59], 'sex': 'Male'}}

pp = PrettyPrinter(indent=2,                    # (default 1) specifies the amount of indentation added for each nesting level.
                   width=50,                    # (default 80) specifies the desired maximum number of characters per line
                   depth=3,                     # controls the number of nesting levels which may be printed, if exceeds 'depth' replaces with ...
                   stream=None,                 # (default is sys.stdout) can provide file-like object to which the output will be written by calling its write() method.
                   compact=True,                # 3.4: Added the compact parameter. If compact is true, as many items of list/set/tuple as will fit within the width will be formatted on each output line
                   # sort_dicts=True,           # 3.8: Added the sort_dicts parameter. formatted with their keys sorted
                   # underscore_numbers=False   # 3.10: Added the underscore_numbers parameter. _ character for a thousands separator
                   )

pp.pprint(d)

# { 1: { 'age': '27',
#        'name': 'John',
#        'scores': [78, 88, 99, 59],
#        'sex': 'Male'},
#   2: { 'age': '22',
#        'name': 'Marie',
#        'scores': [44, 88, 65, 59],
#        'sex': 'Female'},
#   3: { 'age': '24',
#        'name': 'Luna',
#        'scores': [71, 82, 99, 59],
#        'sex': 'Female'},
#   4: { 'age': '29',
#        'name': 'Peter',
#        'scores': [98, 33, 99, 59],
#        'sex': 'Male'}}


# OR SIMPLY ...
pprint(d, indent=2, width=50, depth=3, stream=None, compact=True)
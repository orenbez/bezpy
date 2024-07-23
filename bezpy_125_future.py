# ======================================================================================================================
# the __future__ module is a built-in module in Python that MUST occur at the begining of the file
# Is used to inherit new features that will be available in the new Python versions as mandatory but optional now
# https://www.geeksforgeeks.org/__future__-module-in-python/
# ======================================================================================================================
# For Example  ...
# print_function was optional in 2.6 and mandatory in 3.0
# generator_stop fuction was optional in 3.5 and mandatory in 3.7
# annotations features which are optional in 3.7 mandatory in 3.11

from __future__ import print_function
from __future__ import division 
from __future__ import annotations

import __future__
__future__.all_feature_names

# >>> ['nested_scopes', 
#      'generators', 
#      'division', 
#      'absolute_import', 
#      'with_statement', 
#      'print_function', 
#      'unicode_literals', 
#      'barry_as_FLUFL', 
#      'generator_stop', 
#      'annotations']


print("Hello world", end=" ")  # In python 2.7 you could do this with the import print_function

print(7 / 5)  # In python 2.2 you could upgrade the behavior of division operator '/' to return floats with import division 

class A:
    def f(self) -> A:   # NameError: name 'A' is not defined (unless you import annotations)
        pass


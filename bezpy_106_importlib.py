# ======================================================================================================================
# Documentation: https://docs.python.org/3/library/importlib.html
# importlib is part of the standard library  
# It provides the implementation to Python's import statement ... see importlib.__import__()
# Note the 'imp' module was deprecated in 3.4
# IN addition the importlib library can do the following
# ======================================================================================================================
# see also bezpy_156_pkgutil.py,  Standard Library module provides utilities for the import system, package support.
# see also bezpy_114_inspect.py,  Standard Library module provides utilities to inspect objects
# ======================================================================================================================

import importlib
    
if __name__ == '__main__':
    
    # you can dynamically import a module as a STRING using .import_module()
    # below we import the math module but math is expressed as a string
    # below is equivalent to ...  import math as math_module  
    math_module = importlib.import_module('math')  # returns module object <module 'math' (built-in)> 

    math_module.__doc__   # returns Docsting: 'This module provides access to the mathematical functions\ndefined by the C standard.'
    math_module.__name__  # 'math'
    math_module.__spec__  # ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')
    math_module.sqrt(9)   # 3.0

    # imports your module 'mymath'
    mm = importlib.import_module('mylib.mymath')    # <module 'mylib.mymath' from 'c:\\bezpy\\bezpy\\mylib\\mymath.py'>
    mm.triple_me(3)  # returns 9
 
    # You can try/except ModuleNotFoundError: or you can check to see if you can import the module without acutally importing it with find_spec()
    mod_spec = importlib.util.find_spec('mylib.mymath')   # returns ModuleSpec object  equivalent to mylib.mymath.__spec__
    if mod_spec:
        module = importlib.util.module_from_spec(mod_spec)  # returns module <module 'mylib.mymath' from 'c:\\bezpy\\bezpy\\mylib\\mymath.py'>
        mod_spec.loader.exec_module(module)   # loads module, this step doesn't seem to be required for 'built-in' modules
        module.triple_me(3)   # returns 9

    module1 = importlib.import_module('package.module1')                    # compare with 'from package import module1'
    obj3 = importlib.import_module(name='package.module1', package='obj3')  # compare with 'from package.module1 import obj3'
    # ==================================================================================================================
    # methods like 'getattr' 'callable', 'isclass', 'issubclass' can be now used on the modules/objects
    # ==================================================================================================================
# ======================================================================================================================
# Any Python file is a module, its name being the file's base name without the .py extension.
# A package is a collection of Python modules: while a module is a single Python file, a package is a directory of
# Python modules containing an additional __init__.py file, to distinguish a package from a directory that just happens
# to contain a bunch of Python scripts. Packages can be nested to any depth, provided that the corresponding directories
# contain their own __init__.py file.
# ======================================================================================================================
# after version 3.3.  the __init__.py is not required for the 'import' to work.  It is still required if you wish to
# use an initialization script when importing a package (placed in __init__.py) but not strictly necessary.
# The __init__.py is still required in order to recognize a directory as a 'package' or 'subpackage'
# also see bezpy_156_pkgutil.py
# ======================================================================================================================
# CIRCULAR IMPORTS
# ======================================================================================================================
# 'Circular Imports' are where two modules import each other.  You will need to refactor the code.
# e.g
#       module_a.py:  import module b
#       module_b.py:  import module a
# You can also place an import inside a method or function to avoid the circular imports

from package.module1 import obj1, obj2, obj3

import package.module2 as mod2  # also works,  access with mod2.obj1
from package.module2 import obj1 as another_obj1  # same objects as above
from package.module3 import ret_obj1
from package.subpackage.module1 import obj1 as o1, obj2 as o2, obj3 as o3
from package.subpackage.module2 import test


# from package/module1
print(obj1)          # 1
print(obj2())        # 2
print(obj3().value)  # 3

# from package/module2
print(mod2.obj1)       # 4, does not conflict with module1.obj1
print(another_obj1)    # 4, same object as above

# from package/subpackage/module2
print(o1)  # 5
print(o2())  # 6
print(o3().value)  # 7
test()  # 7383 7383
print(ret_obj1())

# Initializing package
# IMPORTED: __name__=package.module1, __file__=C:\Users\obezalely\OneDrive\PYTHON\package\module1.py
# IMPORTED: __name__=package.module2, __file__=C:\Users\obezalely\OneDrive\PYTHON\package\module2.py
# Initializing subpackage
# IMPORTED: __name__=package.subpackage.module1, __file__=C:\Users\obezalely\OneDrive\PYTHON\package\subpackage\module1.py
# IMPORTED: __name__=package.module3, __file__=C:\Users\obezalely\OneDrive\PYTHON\package\module3.py
# IMPORTED: __name__=package.subpackage.module2, __file__=C:\Users\obezalely\OneDrive\PYTHON\package\subpackage\module2.py
# 1
# 2
# 3
# 4
# 4
# 5
# 6
# 7
# 7383
# 7383
# 4
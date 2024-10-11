# from module1 import obj3   # if I use this import then from bezpy_68_packages.py I just need to 'import packages'
                             # otherwise I need to import from bezpy_68_packages.py using the full path 'from package.module1 import obj3'
print('Initializing package')
__all__ = ['module1', 'module2']   # __all__ affects the from <module> import * behavior only, determines what modules to include

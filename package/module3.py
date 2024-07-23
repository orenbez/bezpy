print(f'IMPORTED: __name__={__name__}, __file__={__file__}')
obj1 = 7383

def ret_obj1():
    from package.module2 import obj1   # <----- "from module2 import obj1" will fail since you are importing ret_obj1 into bezpy_68_packages.py, needs full path
    return obj1

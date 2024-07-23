print(f'IMPORTED: __name__={__name__}, __file__={__file__}')

# RUN THIS FROM CURRENT MODULE



import module1                       # From Current directory
from package import module3          # From package directory


print(module1.obj1)  # 5
print(module3.obj1)  # 7383





# current_directory = os.path.join(os.path.dirname(__file__)
# 1 directory up .. = os.pardir


import sys
import os


PROJ_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))  # TWO DIRECTORIES UP
PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))          # ONE DIRECTORY UP

sys.path.append(PROJ_ROOT)  # appends the project directory to sys.path if required.
# alternatively use env variable 'PYTHONPATH',  but that CANNOT be set during runtime


from mylib.bezpy_customer import Customer
x = Customer('Jeff Knupp',"Bronze",1000.0, 85000)



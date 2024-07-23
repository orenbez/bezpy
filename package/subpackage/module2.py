print(f'IMPORTED: __name__={__name__}, __file__={__file__}')
#  All of these imports give an error if you run from this file because __name__='__main__' which is needed to figure out the paths
#  BUT if you run from bezpy_68_packages.py as your main they will work


from . import module1  as modx_relative                 # Current directory relative path
from package.subpackage import module1 as modx_aboslute # Current directory absolute path

from .. import module3 as mody_relative       # From directory above relative path
from package import module3 as mody_absolute  # From directory above absolute path


obj1 = 5

def obj2():
    return 6

class obj3:
    value = 7


def test():
    print(mody_relative.obj1)
    print(mody_absolute.obj1)

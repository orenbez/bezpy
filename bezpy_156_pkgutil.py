# ======================================================================================================================
# Standard Library module
# https://docs.python.org/3/library/pkgutil.html
# ======================================================================================================================
import pkgutil   # built-in library pkgutil provides utilities for the import system, in particular package support.
import zipimport #  built-in library provides support for importing Python modules from Zip archives
import importlib

# 'x' stores contents of sample.hocon as a string.  All lines below work the same
x = pkgutil.get_data('package', '/subpackage/sample.hocon').decode()   # 'package' requires an __init__.py file,
x = pkgutil.get_data('package', 'subpackage/sample.hocon').decode()    # 'package' requires an __init__.py file
x = pkgutil.get_data('package.subpackage', '/sample.hocon').decode()   # 'subpackage' also requires an __init__.py file
x = pkgutil.get_data('package.subpackage', 'sample.hocon').decode()    # 'subpackage' also requires an __init__.py file

x = pkgutil.get_data('mylib', 'mymock.py').decode()  # stores .py file as a string
'class MyClass3' in x # True

list(pkgutil.walk_packages(['package']))
# [ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='module1', ispkg=False),
#  ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='module2', ispkg=False),
#  ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='module3', ispkg=False),
#  ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='subpackage', ispkg=True)]

for path, name, ispkg in pkgutil.walk_packages(['package']):
    print(path, name, ispkg)
# FileFinder('C:\\github\\package') module1 False
# FileFinder('C:\\github\\package') module2 False
# FileFinder('C:\\github\\package') module3 False
# FileFinder('C:\\github\\package') subpackage True


list(pkgutil.iter_modules(['package']))
# [ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='module1', ispkg=False),
#  ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='module2', ispkg=False),
#  ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='module3', ispkg=False),
#  ModuleInfo(module_finder=FileFinder('C:\\github\\package'), name='subpackage', ispkg=True)]

for path, name, ispkg in pkgutil.iter_modules(['package']):
    if not ispkg:
        module = importlib.import_module(f'package.{name}')
        print(name, [x for x in dir(module) if not x.startswith('_')])
# module1 ['obj1', 'obj2', 'obj3']
# module2 ['obj1']
# module3 ['obj1', 'ret_obj1']

# pkgutil.extend_path
# pkgutil.find_loader
# pkgutil.get_data(package, resource)  # reads file into variable
# pkgutil.get_importer(path_item)
# pkgutil.get_loader(module_or_name)
# pkgutil._get_spec(finder, name)
# pkgutil.iter_importer_modules
# pkgutil.iter_importers
# pkgutil.iter_modules()     # iterator of all built-in modules (see Python Notes)
# pkgutil.iter_modules(list_of_paths)  # returns iterator of all subpackages and modules
# pkgutil.walk_packages(list_of_paths)  # returns iterator of all subpackages and modules  (seems to be same as above)
# pkgutil.iter_zipimport_modules
# pkgutil.namedtuple
# pkgutil.read_code
# pkgutil.simplegeneric
# pkgutil.zipimporter

# ======================================================================================================================
# List of built-in modules ...

sorted([m.name for m in list(pkgutil.iter_modules()) if not m.name.startswith('_')])
# ['abc', 'aifc', 'antigravity', 'argparse', 'ast', 'asynchat', 'asyncio', 'asyncore', 'base64', 'bdb', 'binhex',
# 'bisect', 'bz2', 'cProfile', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmd', 'code', 'codecs', 'codeop', 'collections',
# 'colorsys', 'compileall', 'concurrent', 'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt',
# 'csv', 'ctypes', 'curses', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils', 'doctest',
# 'email', 'encodings', 'ensurepip', 'enum', 'face', 'filecmp', 'fileinput', 'fnmatch', 'fractions', 'ftplib',
# 'functools', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib', 'gzip', 'hashlib', 'heapq', 'hmac',
# 'html', 'http', 'idlelib', 'imaplib', 'imghdr', 'imp', 'importlib', 'inspect', 'io', 'ipaddress', 'json', 'keyword',
# 'lib2to3', 'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'mimetypes', 'modulefinder', 'msilib',
# 'multiprocessing', 'netrc', 'nntplib', 'ntpath', 'nturl2path', 'numbers', 'opcode', 'operator', 'optparse', 'os',
# 'pathlib', 'pdb', 'pickle', 'pickletools', 'pip', 'pipes', 'pkg_resources', 'pkgutil', 'platform', 'plistlib',
# 'poplib', 'posixpath', 'pprint', 'profile', 'pstats', 'pty', 'py_compile', 'pyclbr', 'pydoc', 'pydoc_data',
# 'pyexpat', 'queue', 'quopri', 'random', 're', 'reprlib', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select',
# 'selectors', 'setuptools', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket',
# 'socketserver', 'sqlite3', 'sre_compile', 'sre_constants', 'sre_parse', 'ssl', 'stat', 'statistics', 'string',
# 'stringprep', 'struct', 'subprocess', 'sunau', 'symtable', 'sysconfig', 'tabnanny', 'tarfile', 'telnetlib',
# 'tempfile', 'test', 'textwrap', 'this', 'threading', 'timeit', 'tkinter', 'token', 'tokenize', 'trace', 'traceback',
# 'tracemalloc', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'unicodedata', 'unittest', 'urllib', 'uu', 'uuid',
# 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'winsound', 'wsgiref', 'xdrlib', 'xml', 'xmlrpc', 'zipapp',
# 'zipfile', 'zipimport', 'zoneinfo']


sorted([(m.name, m.ispkg, m.module_finder) for m in pkgutil.iter_modules() if not m.name.startswith('_') and not m.name.startswith('bezpy')])
# ('abc', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('aifc', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('airshow', False, FileFinder('C:\\github'))
# ('antigravity', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('argparse', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ast', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('asyncio', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('base64', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('bdb', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('bisect', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('bofa_convert', False, FileFinder('C:\\github'))
# ('bz2', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('cProfile', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('calendar', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('cgi', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('cgitb', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('chunk', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('cmd', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('code', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('codecs', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('codeop', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('collections', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('colorsys', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('compileall', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('concurrent', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('configparser', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('contextlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('contextvars', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('copy', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('copyreg', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('crypt', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('csv', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ctypes', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('curses', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('dataclasses', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('datetime', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('dbm', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('decimal', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('difflib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('dis', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('doctest', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('email', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('encodings', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ensurepip', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('enum', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('filecmp', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('fileinput', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('fnmatch', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('fractions', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ftplib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('functools', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('genericpath', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('getopt', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('getpass', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('gettext', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('glob', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('graphlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('gzip', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('hashlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('heapq', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('hmac', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('html', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('http', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('idlelib', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('imaplib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('imghdr', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('importlib', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('inspect', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('interpreterInfo', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('io', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ipaddress', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('json', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('keyword', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('leet_code', False, FileFinder('C:\\github'))
# ('lib2to3', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('linecache', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('locale', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('logging', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('lzma', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('mailbox', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('mailcap', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('mimetypes', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('modulefinder', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('msilib', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('multiprocessing', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('netrc', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('nntplib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ntpath', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('nturl2path', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('numbers', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('opcode', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('operator', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('optparse', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('os', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pathlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pdb', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pickle', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pickletools', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pip', True, FileFinder('C:\\github\\venv\\Lib\\site-packages'))
# ('pipes', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pkgutil', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('platform', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('plistlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('poplib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('posixpath', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pprint', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('profile', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pstats', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pty', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('py_compile', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pyclbr', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pycompletionserver', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydev_app_engine_debug_startup', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydev_console', True, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydev_coverage', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydev_ipython', True, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydev_pysrc', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevconsole', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevd', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevd_concurrency_analyser', True, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevd_file_utils', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevd_plugins', True, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevd_pycharm', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydevd_tracing', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('pydoc', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pydoc_data', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('pyexpat', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\DLLs'))
# ('queue', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('quopri', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('random', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('re', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('reprlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('rlcompleter', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('runfiles', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('runpy', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sched', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('secrets', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('select', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\DLLs'))
# ('selectors', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('setup_cython', False, FileFinder('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\plugins\\python-ce\\helpers\\pydev'))
# ('shelve', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('shlex', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('shutil', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('signal', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('site', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('smtplib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sndhdr', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('socket', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('socketserver', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sqlite3', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sre_compile', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sre_constants', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sre_parse', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('ssl', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('stat', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('statistics', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('string', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('stringprep', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('struct', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('subprocess', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sunau', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('symtable', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('sysconfig', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tabnanny', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tarfile', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('telnetlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('temp', False, FileFinder('C:\\github'))
# ('tempfile', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('test', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('textwrap', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('this', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('threading', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('timeit', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tkinter', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('token', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tokenize', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tomllib', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('trace', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('traceback', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tracemalloc', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('tty', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('turtle', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('turtledemo', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('types', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('typing', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('unicodedata', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\DLLs'))
# ('unittest', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('urllib', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('uu', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('uuid', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('venv', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('warnings', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('wave', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('weakref', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('webbrowser', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('winsound', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\DLLs'))
# ('wsgiref', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('xdrlib', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('xml', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('xmlrpc', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('zipapp', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('zipfile', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('zipimport', False, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))
# ('zoneinfo', True, FileFinder('C:\\users\\orenb\\AppData\\Local\\Programs\\Python\\Python312\\Lib'))

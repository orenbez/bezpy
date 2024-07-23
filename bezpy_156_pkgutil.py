# ======================================================================================================================
# Standard Library module provides utilities for the import system, in particular package support.
# https://docs.python.org/3/library/pkgutil.html
# ======================================================================================================================
import pkgutil  # built-in library pkgutil
x = pkgutil.get_data('package', '/subpackage/sample.hocon').decode()    # 'package' seems to require an __init__.py file
x = pkgutil.get_data('package', 'subpackage/sample.hocon').decode()     # works as above
x = pkgutil.get_data('package.subpackage', '/sample.hocon').decode()    # works as above
x = pkgutil.get_data('package.subpackage', 'sample.hocon').decode()     # works as above


# pkgutil.extend_path
# pkgutil.find_loader
# pkgutil.get_data                # reads file into variable
# pkgutil.get_importer
# pkgutil.get_loader
# pkgutil.importlib
# pkgutil.iter_importer_modules
# pkgutil.iter_importers
# pkgutil.iter_modules           # iterator of all built-in modules (see Python Notes)
# pkgutil.iter_zipimport_modules
# pkgutil.namedtuple
# pkgutil.os
# pkgutil.read_code
# pkgutil.simplegeneric
# pkgutil.sys
# pkgutil.walk_packages
# pkgutil.warnings
# pkgutil.zipimport
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

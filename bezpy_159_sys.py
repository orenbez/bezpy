# sys is part of the standard library
import sys

sys.version        #  '3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]'
sys.version_info   # sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)
sys.api_version    # 1013


sys.stdin
sys.stderr
sys.stdout

sys.argv   # returns command line arguments

sys.builtin_module_names   # Built-in Modules which are (compiled-in)
sys.stdlib_module_names    # stdlib Modules which are (compiled-in)
sys.modules                # returns a dictionary of all the modules that have been imported by the current Python interpreter.
                           # The dictionary keys are the module names, and the dictionary values are the module objects.

sys.path   # returns the list of directories that the interpreter will search for the required module

a = 'Geeks'
sys.getrefcount(a)         # number of times it is referenced by other objects. An object is garbage collected when its reference count reaches 0, meaning that it is no longer referenced by any other objects
sys.setrecursionlimit()	   # method is used to set the maximum depth of the Python interpreter stack to the required limit.
sys.getrecursionlimit()    # method is used to find the current recursion limit of the interpreter or to find the maximum depth of the Python interpreter stack.
sys.settrace()             # used for implementing debuggers, profilers and coverage tools. This is thread-specific and must register the trace using threading.settrace(). On a higher level, sys.settrace() registers the traceback to the Python interpreter
sys.setswitchinterval()    # used to set the interpreter’s thread switch interval (in seconds).
sys.maxsize                # fetches the largest value a variable of data type Py_ssize_t can store.
sys.getdefaultencoding()   # method is used to get the current default string encoding used by the Unicode implementation.

sys.exit(4)                # exit with value 4
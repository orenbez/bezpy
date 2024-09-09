# https://realpython.com/python-logging/
# https://docs.python.org/3/library/logging.html

# ======================================================================================================================
# 5 severity levels:    (note you can add more levels if you want)
# ======================================================================================================================
# logging.DEBUG = 10
# logging.INFO = 20
# logging.WARNING = 30
# logging.ERROR = 40
# logging.CRITICAL = 50
# logging.FATAL = 50 (same as above)

# ======================================================================================================================
# Formatting
# ======================================================================================================================
#  %(name)s            Name of the logger (logging channel)
#  %(levelno)s         Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#  %(levelname)s       Text logging level for the message ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
#  %(pathname)s        Full pathname of the source file where the logging call was issued (if available)
#  %(filename)s        Filename portion of pathname
#  %(module)s          Module (name portion of filename)
#  %(lineno)d          Source line number where the logging call was issued (if available)
#  %(funcName)s        Function name
#  %(created)f         Time when the LogRecord was created (time.time() return value)
#  %(asctime)s         Textual time when the LogRecord was created
#  %(msecs)d           Millisecond portion of the creation time
#  %(relativeCreated)d Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded (typically at application startup time)
#  %(thread)d          Thread ID (if available)
#  %(threadName)s      Thread name (if available)
#  %(process)d         Process ID (if available)
#  %(message)s         The result of record.getMessage(), computed just as the record is emitted
# [%(lineno)10.5d]     Right justify 10 spaces, use 5 digits for the number  e.g lineno=146 =>  [     00146]
# [%(message)20.15s]   Right justify 20 spaces, use 15 chars for the message  e.g message='new log in the new format' => [     new log in the ]

import sys
import logging
from mylib.mylog import test

file1 = r'.\myfiles\test1.log'
file2 = r'.\myfiles\test2.log'
file3 = r'.\myfiles\test3.log'
file4 = r'.\myfiles\file.conf'
file5 = r'.\myfiles\test5.log'

# ======================================================================================================================
# by default logging is set to ...
# logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
# logging.debug('Debug message')         # This would be ignored as level is set to logging.WARNING
# logging.info('Info message')           # This would be ignored as level is set to logging.WARNING
# logging.warning('Warning message')     # WARNING:root:Warning message - Displayed in Red with format <Logging-level>:<logger-name>:<message>
# logging.error('Error message')         # ERROR:root:Error message - Displayed in Red with format <Logging-level>:<logger-name>:<message>
# logging.critical('Critical message')   # CRITICAL:root:Critical message - Displayed in Red with format <Logging-level>:<logger-name>:<message>

# ======================================================================================================================
# To set up the root logger and create log file ...
#
logging.basicConfig(filename=file1,      # this field redirects from console (stream=sys.stdout)  to log file
                    filemode='w',        # or 'a' = append
                    level=logging.INFO,  # Sets logging for INFO and above (i.e. logging.debug is ignored)
                    format='%(asctime)s|%(threadName)s|%(levelname)s|%(name)s|%(lineno)d|%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
# • logging.basicConfig:  CAN ONLY BE EXECUTED ONCE, and MUST be before the first logging.<level>.('message')
#      else will default to logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
# • Swap (asctime)s for  %(asctime)s.%(msecs)03d   for micro seconds with datefmt UNCHANGED

# Full list of 'format' attributes: https://docs.python.org/3.8/library/logging.html#logrecord-attributes
# logging.basicConfig(stream=sys.stdout)  # will set logging for stdout instead of file. NOTE: can not have both file output and stdout initialized with basicConfig, will give ValueError
# logging.basicConfig(stream=sys.stderr)  # will set logging for stderr instead of file. NOTE: can not have both file output and stderr initialized with basicConfig, will give ValueError

# Alternatively can set logging parameters with a config file or dictionary by using
# logging.config.fileConfig() ... or
# logging.config.dictConfig() ... see below

# To add a log to the ROOT logger
logging.debug('Debug message')  # This is ignored as level is set to loggin.INFO
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

# Generates ...
# 2024-02-16 07:56:49|MainThread|INFO|root|62|Info message
# 2024-02-16 07:56:50|MainThread|WARNING|root|63|Warning message
# 2024-02-16 07:56:50|MainThread|ERROR|root|64|Error message
# 2024-02-16 07:56:51|MainThread|CRITICAL|root|65|Critical message

# The below are equivalent. Using % String evaluation is lazy and preferred to f-strings for logging.
logging.info("Name: %s, Age: %d, Weight: %.2f kg" % ('Zara', 21, 33.3))
logging.info("Name: %s, Age: %d, Weight: %.2f kg", 'Zara', 21, 33.3)

# Generates ...
# 2024-07-23 16:39:03|MainThread|INFO|root|1|Name: Zara, Age: 21, Weight: 33.30 kg
# 2024-07-23 16:39:15|MainThread|INFO|root|1|Name: Zara, Age: 21, Weight: 33.30 kg

# Capturing Stack Traces with exc_info and print to your logger
try:
    c = 3 / 0
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
  # logging.exception("Exception occurred")  # Equivalent to the above line

# 2024-09-09 14:03:54|MainThread|ERROR|root|100|Exception occurred
# Traceback (most recent call last):
#   File "C:/Oren/06 Computing/06 25 Python/bezpy_28_logging.py", line 51, in <module>
#     c = 3 / 0
# ZeroDivisionError: division by zero

# NOTE:  if a module is imported you do not need to do another logging.basicConfig() in that module too.
test()  # This is an external function (from mylib.mylog) call but still logs to file1

# Use this to modify the ROOT logger at runtime
logger = logging.getLogger()     # access the 'root' logger
logger.name                      # returns 'root'
handler = logger.handlers[0]     # Returns 1st root handler object: <FileHandler C:\github\myfiles\test1.log (NOTSET)>
handler.flush()                  # Flushes the stream.  (Doesn't seem to be necessary)
handler.baseFilename             # returns root logger file path: 'C:\\github\\myfiles\\test1.log'
logger.getEffectiveLevel()       # Returns 20 = logging.INFO level

logger.setLevel(logging.DEBUG)  # This modifies logging level for root logger dynamically to 10 - All child loggers will also be set to 10 if they exist
logging.debug('Debug message')  # This log will now appear, logging & logger point to the 'root' logger
logger.debug('Debug message')   # This is the SAME as the above line

# ADD stderr for 'root' logger in addition to the file output logger (could not be done with basicConfig)
stream_handler = logging.StreamHandler()   # Defaults to logging.StreamHandler(sys.stderr)
logger.addHandler(stream_handler)          # Adds logs to stderr.  
logger.handlers   # root logger now has two handlers: [<FileHandler C:\github\myfiles\test1.log (NOTSET)>, <StreamHandler <stderr> (NOTSET)>]

logger2 = logging.getLogger("another")   # creates new logger called 'another', or retrieves logger 'another' if it exists
logger2.name                             # returns 'another'
logger2.getEffectiveLevel()              # returns 10,  level has been set as the parent (root) logger

assert logger.getChild('another') is logger2   # True, since 'another' is the child of the root logger.  It would also find a grandchild logger if it had that name
assert logger2.parent is logger                # True, since parent of 'another' is the root logger

# Add stdout & Change log format for root logger2
log_format = logging.Formatter("[%(asctime)s] [%(threadName)-12s] [%(levelname)-5.5s] [%(name)s] [%(funcName)s] [%(lineno)10.5d]  [%(message)20.15s]")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_format)
file_handler = logging.FileHandler(file2)
file_handler.setLevel(logging.WARNING)   # sets this only for file handler, not for all of logger 2
logger2.addHandler(stream_handler)       # Adds stream handler to logger2
logger2.addHandler(file_handler)         # Adds file handler to logger2
logger2.handlers                         # logger2 now has two handlers: [<StreamHandler <stdout> (NOTSET)>, <FileHandler C:\github\myfiles\test2.log (WARNING)>]

# Add log file & Change log format for logger2
log_format = logging.Formatter("%(asctime)s: %(message)s", "%Y-%m-%d %H:%M:%S")   # sets date format also,  default date format = '2010-07-10 10:46:28,811' with micro secs
file_handler = logging.FileHandler(file3)
file_handler.setFormatter(log_format)
logger2.addHandler(file_handler)              # additional file handler added to logger2
logger2.handlers                              # now has 3 handlers: [<StreamHandler <stdout> (NOTSET)>, <FileHandler C:\github\myfiles\test2.log (WARNING)>, <FileHandler C:\github\myfiles\test3.log (NOTSET)>]
logger2.info('new log in the new format')     # this now posts to all handlers of logger2 except the File Handler 'file2'
logger2.warning('new log in the new format')  # posts to all handlers of logger2

# ====================================================================================================================
# standard syntax to retrieve from multiple files set to the module name, e.g. logger = logging.getLogger(__name__)
# see explanation below
# ====================================================================================================================
l0 = logging.getLogger()            # sets l0 as the existing root logger  (defined above)
l1 = logging.getLogger('xxx')       # sets child logger
l2 = logging.getLogger('xxx.yyy')   # sets grand-child logger

l0  # <RootLogger root (DEBUG)>
l1  # <Logger xxx (DEBUG)>
l2  # <Logger xxx.yyy (DEBUG)>

assert l0 is l1.parent                 # True
assert l1 is l2.parent                 # True
assert l1 is l0.getChild('xxx')        # True
assert l2 is l0.getChild('xxx.yyy')    # True
assert l2 is l1.getChild('yyy')        # True

l1.addHandler(logging.FileHandler(file5))
l0.warning('this is from l0')   # writes to all root log streams (l0 only)
l1.warning('this is from l1')   # writes to l0/l1 streams
l2.warning('this is from l2')   # writes to l0/l1/l2 streams

l0.addHandler(logging.StreamHandler(sys.stdout))  # adds stdtout to root stream handler in addition to stderr
l0.handlers   # [<FileHandler C:\github\myfiles\test1.log (NOTSET)>, <StreamHandler <stderr> (NOTSET)>, <StreamHandler <stdout> (NOTSET)>]
l1.handlers   # [<FileHandler C:\github\myfiles\test5.log (NOTSET)>]
l2.handlers   # []  - no handlers added

l0.warning('test')            # prints to stdout and stderr
logging.warning('test')       # same as above
logger = logging.getLogger(__name__)   # since __name__ will be == 'dir1.dir2.filename' you can inherit all handlers from 'dir1' with this trick

# Note: there is no close function logger.close()


# ======================================================================================================================
# dir(logging.getLogger()
# ======================================================================================================================
# addFilter
# addHandler()  - add file or stream handler to the logger
# callHandlers
# critical(msg) - critical message
# debug(msg) - debug message
# disabled
# error(msg) - error message
# exception(msg) - error message + stack trace
# fatal(msg) - fatal message
# filter
# filters
# findCaller
# getChild('child-name') - returns child logger of the name 'child-name' (or grandchild)
# getEffectiveLevel() - returns logger level
# handle
# handlers
# hasHandlers     - returns boolean if handlers are present
# info(msg) - info message
# isEnabledFor
# level - logger.level stores integer value of severity level 10-50
# log  - logger.log(logging.DEBUG, msg) is same as logger.debug(msg)
# makeRecord
# manager
# name - returns name of logger
# parent
# propagate
# removeFilter
# removeHandler()  - to remove a logger handler (file or stdout or stderr)
# root - 'logger' is the samge object as logger.root
# setLevel() - change logging level
# warn(msg) - DEPRECATED, DO NOT USE
# warning(msg) - warning message

# ======================================================================================================================
# Sample Logging dictionary setup
# ======================================================================================================================
LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'default': {
           'format': '%(asctime)s|%(threadName)s|%(levelname)s|%(name)s|%(lineno)d|%(message)s'
        },
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
           'format': '%(message)s'
        },
        'full': {
           'format': '%(asctime)s.%(msecs)03d|%(threadName)s|%(levelname)s|%(name)s.%(funcName)s|%(lineno)d|%(message)s'
        }
    },
    'handlers': { 
        'default': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'logfile': {
           'level': 'ERROR',
           'formatter': 'default',
           'class': 'logging.handlers.RotatingFileHandler',
           'filename': 'error_file.log',
           'backupCount': 2
        }
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['default'],
            'level': 'WARNING',
            'propagate': False
        },
        'my.packg': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}

import logging.config

logging.config.fileConfig(file4)            # loggers set by file.conf
logging.config.dictConfig(LOGGING_CONFIG)   # loggers reset by LOGGING_CONFIG dictionary
assert logging.getLogger('__main__').getEffectiveLevel() == logging.DEBUG  # 10
assert logging.getLogger('my.packg').getEffectiveLevel() == logging.INFO   # 20

# ======================================================================================================================
# Sample User-Defined logging class
# ======================================================================================================================
class BezLog:

    def __init__(self):

        logging.basicConfig(filename="event.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S', level=logging.DEBUG)
        self.logger = logging.getLogger()

    def init_config(self):
        self.logger.info('Reading Configuration file')

    def read_files(self):
        self.logger.info('Reading files from the source directory')

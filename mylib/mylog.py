# this module is imported by bezpy_28_logging.py despite
# If test() is called in this file then test() will do nothing as no log file is defined
# If test() is imported it will add logging to whatever log file was defined in the main program


import logging
def test():
    logging.info('Hello from mylog.py')


if __name__ == '__main__':
    test()

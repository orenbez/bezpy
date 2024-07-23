# built-in library signal: This module provides support for handling signals. e.g. signal.CTRL_C_EVENT
# When the operating system receives certain events, it can pass that to programs in the form of signals

# https://pavolkutaj.medium.com/explaining-signal-module-in-python-854734318aea


import signal
[x for x in dir(signal) if not x.startswith('_')]

# ['CTRL_BREAK_EVENT',
#  'CTRL_C_EVENT',
#  'Handlers',
#  'NSIG',
#  'SIGABRT',
#  'SIGBREAK',
#  'SIGFPE',
#  'SIGILL',
#  'SIGINT',
#  'SIGSEGV',
#  'SIGTERM',
#  'SIG_DFL',
#  'SIG_IGN',
#  'Signals',
#  'default_int_handler',
#  'getsignal',
#  'raise_signal',
#  'set_wakeup_fd',
#  'signal',
#  'strsignal',
#  'valid_signals']


signal.valid_signals()      #   dictionary of valid signals in your OS
# {<Signals.SIGINT: 2>,     #  SIGNAL INTERUPT
#  <Signals.SIGILL: 4>,
#  <Signals.SIGFPE: 8>,
#  <Signals.SIGSEGV: 11>,
#  <Signals.SIGTERM: 15>,
#  <Signals.SIGBREAK: 21>,
#  <Signals.SIGABRT: 22>}


# https://www.askpython.com/python-modules/python-signal
# A Signal Handler is a user defined function, where Python signals can be handled.
# after we run our program, when we press Ctrl + C, the program will go to the signal_handler() function, since we have registered the handler with SIGINT (Ctrl + C).
import signal
import time

# Our signal handler
def signal_handler(signum, frame):
    print("Signal Number:", signum, " Frame: ", frame)


def exit_handler(signum, frame):
    print('Exiting....')
    exit(0)


signal.signal(signal.SIGINT, signal_handler) # Register our signal handler with `SIGINT`(CTRL + C)
signal.signal(signal.SIGTSTP, exit_handler) # Register the exit handler with `SIGTSTP` (Ctrl + Z)

# While Loop
while 1:
    print("Press Ctrl + C")
    time.sleep(3)




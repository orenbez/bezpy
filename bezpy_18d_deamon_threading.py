# I haven't fully understood how this works to be honest

# Deamonic Threads
# setting threads as daemon threads,
# you can let them run and forget about them, and when your program quits, any daemon threads are killed automatically.

from threading import Thread, currentThread # appears to be the same as current_thread
import time
import sys


def a():
    print('Starting of thread :', currentThread().name)
    time.sleep(10)
    print('Finishing of thread :', currentThread().name)


def b():
    print('Starting of thread :', currentThread().name)
    time.sleep(5)
    print('Finishing of thread :', currentThread().name)

def c():
    print('Starting of thread :', currentThread().name)
    print('Finishing of thread :', currentThread().name)


a = Thread(target=a, name='Thread-a', daemon=True)
b = Thread(target=b, name='Thread-b')
c = Thread(target=c, name='Thread-c')

a.start()
b.start()
c.start()

sys.exit()

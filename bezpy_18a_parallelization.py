# TRY THIS https://towardsdatascience.com/how-to-speed-up-your-python-code-d31927691012
# TRY THIS https://betterprogramming.pub/speed-up-your-data-collection-efforts-with-multithreading-in-python-61f3b3cc06df
# TRY THIS https://towardsdatascience.com/a-hands-on-guide-to-multiprocessing-in-python-48b59bfcc89e?source=bookmarks---------68----------------------------
# TRY : https://medium.com/better-programming/python-memory-and-multiprocessing-ed517b8db8fd?source=bookmarks---------7----------------------------
# https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612
# https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/
# http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html

# also see joblib library https://measurespace.medium.com/use-joblib-to-run-your-python-code-in-parallel-ad82abb26954


# Both processes and threads are independent sequences of execution.

# Threading:
# - Threads are executed with CONCURRENCY
# - A new thread is spawned within the existing process
# - Starting a thread is faster than starting a process
# - Memory is shared between all threads
# - Mutexes often necessary to control access to shared data
# - In cpython, One GIL (Global Interpreter Lock) for all threads, allows only one thread to hold the control of the interpreter
# - Used for programs involving network operations or I/O or user interaction.

# Multiprocessing:
# - Processes can be executed in PARALLEL (with multiple CPUS)
# - A new process is started independent from the first process
# - Starting a process is slower than starting a thread
# - Memory is not shared between processes
# - Mutexes not necessary (unless threading in the new process)
# - In cpython, One GIL (Global Interpreter Lock) for each process
# - Used for CPU bound, computation-intensive programs.

from threading import Thread, current_thread          # BUILT-IN LIBRARY
from multiprocessing import Process, current_process  # BUILT-IN LIBRARY
from random import sample
import urllib.request
from functools import reduce
from time import sleep, time
import os, sys


def disp():
    print(f'Process ID: {os.getpid()}, Process Name: {current_process().name}, Thread Name: {current_thread().name}')

def job(n):
    disp()
    random_list = sample(range(1000000), n)  # Generates Random list of 'n' elements
    return reduce(lambda x, y: x * y, random_list)  # multiplies elements of a list

def sleepy():
    """ Do nothing, wait for a timer to expire """
    disp()
    sleep(1)
    return 1

def crunch():
    """ Do some computations """
    disp()
    x = 0
    while x < 10000000:
        x += 1

def return_after_5_secs(message):
    disp()
    sleep(5)
    return message

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.yahoo.com/',
        'http://www.google.com/',]


# Retrieve a single page and report the url and contents
def load_url(url):
    disp()
    with urllib.request.urlopen(url, timeout=60) as conn:
        return conn.read()

# ======================================================================================================================
#  __name__ == '__main__':
# ======================================================================================================================
if __name__ == '__main__':

    # ==================================================================================================================
    # There are two built-in parallelization libraries 'multiprocessing' and 'threading'
    # ==================================================================================================================
    num_of_cores = os.cpu_count()   # or can use multiprocessing.cpu_count()

    test = 4

    if test == 1:   # Serial Wins
        threads = [Thread(target=job, args=(50000,)) for _ in range(num_of_cores)]
        processes = [Process(target=job, args=(50000,)) for _ in range(num_of_cores)]

    elif test == 2:  # Thread Wins
        threads = [Thread(target=sleepy) for _ in range(num_of_cores)]
        processes = [Process(target=sleepy) for _ in range(num_of_cores)]

    elif test == 3:   # Parallel Wins
        threads = [Thread(target=crunch) for _ in range(num_of_cores)]
        processes = [Process(target=crunch) for _ in range(num_of_cores+1)]

    elif test == 4:   # Thread Wins
        threads = [Thread(target=load_url, args=([URLS[i]])) for i in range(num_of_cores)]
        processes = [Process(target=load_url, args=([URLS[i]])) for i in range(num_of_cores)]

    # Run tasks serially
    start_time = time()
    for i in range(num_of_cores):
        if test == 1:
            job(50000)
        elif test == 2:
            sleepy()
        elif test == 3:
            crunch()
        elif test == 4:
            load_url(URLS[i])
    end_time = time()
    duration = end_time - start_time
    print(f'Serial time={duration:.3f}\n')

    # Run tasks using threads
    start_time = time()

    # Start all Threads
    for thread in threads:
        thread.start()

    # Wait for all thread to finish
    for thread in threads:
        thread.join()

    end_time = time()
    duration = end_time - start_time
    print(f'Threads time={duration:.3f}\n')


    # Run tasks using processes
    start_time = time()

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to join
    for process in processes:
        process.join()
    end_time = time()
    duration = end_time - start_time
    print(f'Parallel time={duration:.3f}\n')


# ======================================================================================================================

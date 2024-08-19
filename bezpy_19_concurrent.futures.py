# ======================================================================================================================
# concurrent.futures From the standard library
# ======================================================================================================================
# https://docs.python.org/3/library/concurrent.futures.html
# ProcessPoolExecutor: CPU-Intensive tasks
# ThreadPoolExecutor: I/O bound tasks
# READ ME: https://towardsdatascience.com/concurrency-in-python-how-to-speed-up-your-code-with-threads-bb89d67c1bc9
# http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed, wait
from math import factorial
from functools import reduce
import os
import random
import sys
from time import sleep, time
import urllib.request


def task(n):
    print(f'task {n} starting')
    sleep(2)
    print(f'\ntask {n} finished')
    return n


def disp():
    print(f'PID: {os.getpid()}')


def job(n):
    disp()
    random_list = random.sample(range(100000), n)     # Generates Random list of 'n' elements
    return reduce(lambda x, y: x * y, random_list)    # multiplies elements of a list


def sleepy():
    """ Do nothing, wait for a timer to expire """
    disp()
    sleep(1)
    return 1


def crunch():
    """ Do some computations """
    disp()
    x = 0
    while x < 1000000:
        x += 1


def return_after_1_sec(message):
    disp()
    sleep(1)
    return message


URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    disp()
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


if __name__ == '__main__':
    # executor.submit
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        for future in as_completed(futures):
            print(f'result={future.result()}')

    # executor.map
    numbers = [2, 3, 7, 9]
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(factorial, numbers))
        for number, result in zip(numbers, results):
            print(f'factorial of {number} is {result}')
    sys.exit(0)

    # ==================================================================================================================
    pool = ThreadPoolExecutor(max_workers=4)
    thread = pool.submit(return_after_1_sec, ("hello"))
    print(thread.running())
    sleep(3)
    print(thread.done())
    print(thread.result())

    # ==================================================================================================================
    pool = ProcessPoolExecutor(max_workers=4)
    process = pool.submit(return_after_1_sec, ("hello"))
    print(process.running())  # Is the job running?
    sleep(3)
    print(process.done())  # Has job been completed?
    print(process.result())

    # ==================================================================================================================
    process1 = pool.submit(sleepy)
    process2 = pool.submit(sleepy)
    fs = [process1, process2]  # futures

    # default = ALL_COMPLETED, other values FIRST_COMPLETED, FIRST_EXCEPTION
    print(wait(fs, return_when='ALL_COMPLETED'))

    # ==================================================================================================================
    start_time = time()
    for _ in range(4):
        job(50000)
    end_time = time()
    print("Serial time=", end_time - start_time, '\n')

    # We can use a with statement to ensure threads are cleaned up promptly
    start_time = time()
    with ProcessPoolExecutor() as executor:
        executor.map(job, [50000, 50000, 50000, 50000])  # map() example
    end_time = time()
    print("Parallel time=", end_time - start_time, '\n')

    # ==================================================================================================================
    start_time = time()
    for _ in range(4):
        crunch()
    end_time = time()
    print("Serial time=", end_time - start_time, '\n')

    # ==================================================================================================================
    # as_complete() example
    # ==================================================================================================================
    start_time = time()
    pool = ProcessPoolExecutor(4)
    fs = [pool.submit(crunch) for _ in range(4)]  # List of processes called 'futures'
    for x in as_completed(fs):
        print(x.result())
    end_time = time()
    print("Parallel time=", end_time - start_time, '\n')

    # ==================================================================================================================
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL in a dictionary
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))

# Python GIL can be disabled in python 3.13
import sys
import sysconfig
from math import factorial
from threading import Thread
import time
from multiprocessing import Process
numlist = [1000, 2000, 3000, 4000]


def single_threaded_compute():
    for num in numlist:
        factorial(num)
    print('End single_threaded_compute')


def multi_threaded_compute():
    threads = [Thread(target=factorial, args=(num,)) for num in numlist]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print('End multi_threaded_compute')


def multi_process_compute():
    processes = [Process(target=factorial, args=(num,)) for num in numlist]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print('End multi_process_compute')


def main():
    print(f'Python version = {sys.version}')
    status = sysconfig.get_config_var('Py_GIL_DISABLED')

    match status:
        case 0:
            print('GIL ACTIVE')
        case 1:
            print('GIL DISABLED')
        case None:
            print('GIL can not be DISABLED')
        case _:
            print('oops - something went wrong here')

    # Single Threaded Execution
    start = time.perf_counter()
    single_threaded_compute()
    end = time.perf_counter() - start
    print(f'Single Threaded Time = {end:.2f} secs')

    # Multi Threaded Execution (quickest if GIL disabled)
    start = time.perf_counter()
    multi_threaded_compute()
    end = time.perf_counter() - start
    print(f'Single Threaded Time = {end:.2f} secs')

    # Multi-Process Execution  (quickest if GIL enabled)
    start = time.perf_counter()
    multi_process_compute()
    end = time.perf_counter() - start
    print(f'Single Threaded Time = {end:.2f} secs')

if __name__ == '__main__':
    main()
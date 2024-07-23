# read https://medium.com/python-features/pythons-gil-a-hurdle-to-multithreaded-program-d04ad9c1a63
# Using Classes and Inheritance


from time import time, sleep
from threading import Thread, current_thread
from multiprocessing import Process, current_process

def sleepme(number):
    sleep(number)


class SleepThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
    def run(self):
        print(current_thread().name)
        sleepme(self.number)
        self.message = f'You slept for {self.number} s'


class SleepProcess(Process):
    def __init__(self, number):
        super().__init__()
        self.number = number
    def run(self):
        print(current_process().name)
        sleepme(self.number)
        self.message = f'You slept for {self.number} s'   # For some reason this process attribute is deleted when process ends

if __name__ == '__main__':
    numbers = [1, 2, 2, 1]

    # SERIES
    start = time()
    for number in numbers:
        sleepme(number)
    end = time()
    print (f'Series took {end-start:.3f} seconds')

    # THREADS
    start = time()
    threads = []
    for number in numbers:
        thread = SleepThread(number)
        thread.start() # this calls run()
        threads.append(thread)
    # wait for all thread to finish
    for thread in threads:
        thread.join()
    end = time()
    print(f'Threads took {end - start:.3f} seconds')


    # PROCESS
    start = time()
    processes = []
    for number in numbers:
        process = SleepProcess(number)
        process.start() # this calls run()
        processes.append(process)
    # wait for all thread to finish
    for process in processes:
        process.join()
    end = time()
    print(f'Processes took {end - start:.3f} seconds')

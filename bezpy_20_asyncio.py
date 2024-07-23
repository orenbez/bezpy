# Asynchronous programming - Does not require sequential instructions. Code can be executed independent of the main
# program flow, while waiting for something. A unit of work runs separately from the main application thread and
# notifies the calling thread of its completion/failure/progress.

# Setting up coroutines with asyncio is an alternative to threading
# threads - OS decides on context switching, locks determine when you can't switch to another thread
# coroutines - you decide on the switch, 'await' determines when you can switch to another coroutine

# the word coroutine is used in contrast to a normal subroutine which is evaluated synchronously

# New to python 3.10 functions aiter(), anext()  asynchronous counterparts to iter() and next()
# anext() raises an StopAsyncIteration exception when iteration has ended

# New to python 3.11 support of Nested Async Comprehensions, and TaskGroup feature
# The TaskGroup functions as a context manager, holding your group of tasks that will wait for all of them upon exit

# Blocking Call : waits till finished to return a value
# Non-Blocking Call: will resume code while call is processing

# Callbacks
# Callbacks are a type of API that is frequently used in network programming where rather than launching the thread
# yourself, the language takes care of running the request in the background. Callbacks provide a place to wait for
# multiple options to return, all in a single thread.

import asyncio  # BUILT-IN LIBRARY from Python 3.4
import time

# ======================================================================================================================
# Example 0: asyncio.gather, asyncio.create_task
# ======================================================================================================================
# asyncio.create_task(f())    will spawn a task and then forget about it
# asyncio.gather(f(), g())    This is like a join statement in threads
# ======================================================================================================================


# coroutine 1: returns a coroutine object
async def brew():  # async keyword allows method to be used as a coroutine
    print('Start Brew')
    await asyncio.sleep(3)   # await => safe to pause and yield to other coroutines
    print('Stop Brew')
    return 'brewed'

# Note 'await' can only go before commands that are awaitable
# e.g. time.sleep() is not awaitable but asyncio.sleep() is awaitable


# coroutine 2: returns a coroutine object
async def toast():   # async keyword allows method to be used as a coroutine
    print('Start toast')
    await asyncio.sleep(3)  # await => safe to pause and yield to other coroutines
    print('Stop toast')
    return 'toasted'


async def main1():  # since we used the 'await' keyword below we must use 'async' here treating 'main' as a coroutine
    start = time.perf_counter()
    batch = asyncio.gather(brew(), toast())   # gather groups coroutines for concurrent execution
    result_brew, result_toast = await batch   # executes both tasks - need to 'await' for the return values of the coroutines in same order as listed in 'gather'
    elapsed_time = time.perf_counter() - start
    print(result_brew, result_toast, elapsed_time)


async def main2():  # alternative to main1() which used 'gather'.  You can list the tasks individually. Exact same behavior as main1()
    start = time.time()
    brew_task = asyncio.create_task(brew())
    toast_task = asyncio.create_task(toast())

    result_brew = await brew_task    # executes task
    result_toast = await toast_task  # executes task

    elapsed_time = time.time() - start
    print(result_brew, result_toast, elapsed_time)


asyncio.run(main1())  # this is how we call the 'main1' coroutine
asyncio.run(main2())  # this is how we call the 'main2' coroutine

# Output for main1
# Start Brew
# Start toast
# Stop Brew
# Stop toast
# brewed toasted 3.0149359703063965

# Output for main2
# Start Brew
# Start toast
# Stop Brew
# Stop toast
# brewed toasted 3.007777452468872

# ======================================================================================================================
# Example 1:
# ======================================================================================================================
async def print_something_twice():  # python keyword 'async'
    print('Hello World')
    await asyncio.sleep(1)   # python keyword 'await' => safe to switch to coroutine. Usually you would be waiting for a server response
    print('Hello to you three')


async def print_something():
    print('Hello to you two')   # Note: doesn't have await command


async def print_main():
    await asyncio.gather(print_something_twice(), print_something())

asyncio.run(print_main())

# Hello World
# Hello to you two
# Hello to you three

# ----------------------------------------------------------------------------------------------------------------------
# asyncio.get_event_loop, asyncio.run_until_complete deprecated in 3.10,
# asyncio.wait deprecated in 3.8
# asyncio.ensure_future deprecated in 3.4
# ----------------------------------------------------------------------------------------------------------------------
# loop = asyncio.get_event_loop()

# tasks = [asyncio.ensure_future(print_something_twice()), asyncio.ensure_future(print_something())] ... OR
# tasks = [loop.create_task(print_something_twice()), loop.create_task(print_something())]

# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# ======================================================================================================================
# Example 2:
# ======================================================================================================================
counter = 0


async def f():
    global counter
    while True:
        counter += 2
        print(counter)
        if counter > 10:
            break
        await asyncio.sleep(0)


async def g():
    global counter
    while True:
        counter -= 1
        print(counter)
        if counter < -10:
            break
        await asyncio.sleep(0)


async def f_g_main():
    await asyncio.gather(f(), g())

asyncio.run(f_g_main())


# ======================================================================================================================
# Example 3
# ======================================================================================================================
async def foo():
    print('foo started')
    await asyncio.sleep(3)
    print('foo ended')


# When this is called it returns a coroutine which can be executed with an await command
async def main():
    print('main start')
    task = asyncio.create_task(foo())
    print('after foo')
    await task   # executes


asyncio.run(main())  # This creates an Event Loop

# main start
# after foo
# foo started
# foo ended


# ======================================================================================================================
# Example 4
# ======================================================================================================================

async def count2():
    await asyncio.sleep(1)
    print(1)
    await asyncio.sleep(2)
    print(2)
    await asyncio.sleep(3)
    print(3)


async def main3():
    await asyncio.gather(count2(), count2(), count2())


t1 = time.perf_counter()
asyncio.run(main3())  # asynchronous
t2 = time.perf_counter()
print(f'Elapsed time = {t2-t1:.2f} secs')


# ======================================================================================================================
# Example 5 - Using aiter(), anext()  from version 3.10
# ======================================================================================================================
class AsyncIter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __aiter__(self):
        self.cur = self.start
        return self

    async def __anext__(self):     # <---- next value returned by the async for loop
        await asyncio.sleep(1)
        if self.cur > self.stop:
            raise StopAsyncIteration
        self.cur += 1
        return self.cur - 1


async def example():
    cust_obj = AsyncIter(1, 3)
    obj_iter = aiter(cust_obj)
    print(obj_iter)
    print(await anext(obj_iter), 'Explicit anext call')
    print(await anext(obj_iter), 'Explicit anext call')
    print(await anext(obj_iter), 'Explicit anext call')
    async for num in obj_iter:
        print(num, 'Implicit anext call')

asyncio.run(example())

# <__main__.AsyncIter object at 0x000001F14C254220>
# 1 Explicit anext call
# 2 Explicit anext call
# 3 Explicit anext call
# 1 Implicit anext call
# 2 Implicit anext call
# 3 Implicit anext call

# ======================================================================================================================
# 'asyncore' module from the standard library  — Asynchronous socket handler - to be replaced by asyncio. 3.13
# ======================================================================================================================
# https://docs.python.org/3/library/asyncore.html
# provides a framework for developing asynchronous network applications.


# ======================================================================================================================
# 'asynchat' module from the standard library - - to be replaced by asyncio. 3.13
# ======================================================================================================================
# https://docs.python.org/3/library/asynchat.html
# provides a framework for handling asynchronous chat

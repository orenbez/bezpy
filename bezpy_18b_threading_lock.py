# RACE CONDITION.
# occur when two computer program processes, or threads, attempt to access the same resource at the same time
# could be seperate instances of your program runnning at the same time trying to access the same database column 

# the threads are protected by GIL but if you have multiple threads accessing the same data
# and modifying the data you will need locks to protect a block
# Choosing the right locking granularity is hard,  risk of deadlocking

from threading import Lock  # BUILT-IN LIBRARY
# RLock is an alternative lock


# Use the with 'context' statement
with Lock():
    # do your operations here
    pass

# Without the with statement
lock = Lock()
lock.acquire()
try:
    # do your operations here
    pass
except Exception:
    # handle exceptions
    pass
finally:
    lock.release()

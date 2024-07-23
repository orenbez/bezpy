# https://medium.com/python-features/understanding-memory-usage-and-leaks-in-our-python-code-beginners-c9dc211887af

# ============================================================================================================
# MEMORY MANAGEMENT IN PYTHON
# ============================================================================================================
# 1) DMA (Dynamic Memory Access) provides memory on-the-fly as apposed to Static Memory Allocation which
# for which systems prepare memory to be used, allocating at complie time

# 2) PHS (Private Heap Space) all the objects and data structures are stored in the private heap space. 
# Python has inbuilt garbage collector, which recycles unused memory and frees it, making it available 
# to the heap space User has no control over it.

# 3) GCS (Garbage Collection System):
# Python uses a method called reference counting to decide when an object needs to be collected in the memory.
# ============================================================================================================


import sys

list_1 = list(range(1,100))
tuple_1 = tuple(range(1,100))

print(sys.getsizeof(list_1))   # 848 bytes
print(sys.getsizeof(tuple_1))  # tuples use less memory - 832 bytes


# Have not understood this yet  3/23/2021

import gc   # Built-In Module Garbage Collection
# https://docs.python.org/3/library/gc.html

found_objects = gc.get_objects()
print(f'{len(found_objects)} objects before')
ref = 'Sarah ' * 512000
found_objects = gc.get_objects()
print(f'{len(found_objects)} objects after')
for obj in found_objects[:3]:
    print(repr(obj)[:100])


gc.enable()
gc.collect()   # returns the number of unreachable objects found and cleaned within the namespace. In simple terms, the function releases the memory slot of unused objects



import tracemalloc  # Built-In Module
tracemalloc.start(5)  # save upto 5 stack frames
time1 = tracemalloc.take_snapshot()
ref = 'Sarah ' * 51200
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)



# >>> punk=2077
# >>> id(punk)
# 4319088080 is the memory location of punk

# >>> import _ctypes
# >>> print(_ctypes.PyObj_FromPtr(4319088080))
# 2077 is the value stored in the memory location
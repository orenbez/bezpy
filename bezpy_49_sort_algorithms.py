# see python library 'bisect'  https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
# for list.sort() and sorted() python uses O(n Log n) Tim Sort Algorithm https://www.geeksforgeeks.org/timsort/
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def bubble_sort(list_a):
    indexing_length = len(list_a) - 1 #SCan not apply comparison starting with last item of list (No item to right)
    is_sorted = False #Create variable of sorted and set it equal to false

    while not is_sorted:  #Repeat until sorted = True
        is_sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i] > list_a[i+1]: #if value in list is greater than value directly to the right of it,
                is_sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a # Return our list "unsorted_list" which is not sorted.


def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

            if min_value != i:
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a


# Searches for a value in a sorted list by divide and conquer
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None


def merge_sort(sequence):
    if len(sequence) > 1:
        mid = len(sequence) // 2
        left = sequence[:mid]
        right = sequence[mid:]
        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sequence[k] = left[i] # The value from the left half has been used
                i += 1 # Move the iterator forward
            else:
                sequence[k] = right[j]
                j += 1
            k += 1 # Move to the next slot
        # For all the remaining values
        while i < len(left):
            sequence[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            sequence[k] = right[j]
            j += 1
            k += 1
    return sequence


# O(1) => Fixed time irrespective of list size (not necessarily instant, rather independent of data size)
# O(log(n))) =>  this is log base 2 of n, if you double the data list you only add '1' to the order
# O(n) => if you double the list you will double the order
# O(n^2) => complexity increases quadratically with data-size
# O(n*log(n))) =>  n x log base 2 of n
# O(2^n) => complexity increases exponentially with data-size

# O(1) > O(log(n)) > O(n) > O(n*log(n)) > O(n^2) > O(2^n) > O(n!)   https://www.bigocheatsheet.com/
print(f'binary_search={binary_search([2,4,5,6,7,8,9,10,12,13,14], 10)}')   # Θ(log(n)) average, O(n) at worst
print(f'insertion_sort{insertion_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0])}')    # O(n^2)
print(f'selection_sort={selection_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0])}')   # O(n^2)
print(f'buble_sort={bubble_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0])}')          # O(n^2)
print(f'merge_sort={merge_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0])}')           # O(n^2)
print(f'quick_sort={quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0])}')           # O(n*log(n)))   fastest sort is n x log base 2 of n
# Fibonacci recursive function to calculate the nth term                   # O(2^n)


# Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into
#   simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal
#   solution to its subproblems.


# Complexity Functions
# A function f(n) = O(g(n)) if there exists a positive real number c such that |f(n)| ≤ c|g(n)| for sufficiently large n.
# More informally, we say that f(n) = O(g(n)) if f(n) grows no faster than g(n) does with increasing n. 
# Writing f(n) ≺ g(n) indicates that g(n) has greater order than f(n) and hence grows more quickly. 
# The hierarchy of common functions is ...  1 ≺ log(n) ≺ n ≺ n^k ≺ c^n ≺ n! ≺ n^n  where c,k > 1.
import graphlib  # Standard library as of Python 3.9
# used for sorting data which is in a graph-like structure
# for complex graph structures , with multiple nodes and edges, the python 'sorted' function is not enough

from graphlib import TopologicalSorter

graph = {
    'band': {'manager'},
    'manager': set(),
    'concert': {'band', 'venue'},
    'venue': set(),
}
sorter = TopologicalSorter(graph)
ordered = tuple(sorter.static_order())
print(ordered) # ('manager', 'venue', 'band', 'concert')
"""
Binary search implementation
"""

def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.
    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

list = ['alberto' , 'beto', 'carmen', 'daniel', 'fernando', 'pablo', 'ramon', 'samuel', 'wilson']

print(f"Find carmen: {binary_search(list,'carmen')}")
print(f"Find carmen: {binary_search(list,'wilson')}")
print(f"Find carmen: {binary_search(list,'pablo')}")
print(f"Find carmen: {binary_search(list,'asss')}")
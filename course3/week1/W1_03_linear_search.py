
"""
If you're curious about how linear and binary search look in code,
here are a couple of implementations in Python:
"""

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


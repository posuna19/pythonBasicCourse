import memory_profiler
import random
import string
import sys

@profile
def doSometing():
    print(f"Size of a List: {sys.getsizeof([])}")
    print(f"Size of a Set: {sys.getsizeof(set())}")
    print(f"Size of a Dict: {sys.getsizeof({})}")

    num_dic = {}
    for i in range(0,1000):
        #print(f"This is the counter {i+1}")
        num_dic[i] = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

doSometing()


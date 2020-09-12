import numpy as np
import string
import time
from collections import deque

size = 200000
max_str_length = 100
ascii_letters = string.ascii_letters

arr = []
narr = np.empty((size, 1), dtype=object)
fix_size_array = np.empty((size, 1), dtype=np.dtype('U20000'))
d = deque(maxlen=size)
for i in range(size):
    random_size = np.random.randint(20000)
    char = ascii_letters[i % len(ascii_letters)]
    s = char * random_size
    arr.append(s)
    # narr[i] = s
    # fix_size_array[i] = s
    d.append(s)

print("*** Test Loop Execution ***")

def builtin():
    start_time = time.time()
    print("Start test built-in: %s" % (start_time))
    for item in arr:
        tmp = len(item)
    print("--- %s seconds ---" % (time.time() - start_time))


def object_array():
    start_time = time.time()
    print("Start test object numpy array: %s" % (start_time))
    for item in narr:
        tmp = len(item)
    print("--- %s seconds ---" % (time.time() - start_time))

def fix_length_numpy_array():
    start_time = time.time()
    print("Start test fix length numpy array: %s" % (start_time))
    for item in fix_size_array:
        tmp = len(item)
    print("--- %s seconds ---" % (time.time() - start_time))

def deque_array():
    start_time = time.time()
    print("Start test fix length numpy array: %s" % (start_time))
    while len(d) != 0:
        tmp = len(d.pop())
    print("--- %s seconds ---" % (time.time() - start_time))

builtin()
deque_array()

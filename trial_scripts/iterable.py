#!/usr/bin/env python

def iterable():
    for i in range(3):
        yield i


class iterator():
    def __iter__(self):
        for i in range(3):
            yield i


test = iterator()

for i in test:
    print(i)

for i in test:
    print(i)

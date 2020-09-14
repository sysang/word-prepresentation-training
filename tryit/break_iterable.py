def iterable():
    for i in range(5):
        yield(i)


def iterable_break():
    for i in range(5):
        if i > 3:
            break
        yield(i)


def iterable_return():
    for i in range(5):
        if i > 3:
            return None
        yield(i)


for i in iterable_return():
    print(i)

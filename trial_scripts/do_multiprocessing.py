from multiprocessing import Process
from multiprocessing.sharedctypes import RawValue
import ctypes


def f(n):
    n.value = 'hello!!'


if __name__ == '__main__':
    num = RawValue(ctypes.c_wchar_p, 'abc')

    p = Process(target=f, args=(num,))
    p.start()
    p.join()

    print(num.value)


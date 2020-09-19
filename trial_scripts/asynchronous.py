import time
import tarfile
import re

import asyncio
import concurrent.futures
import _thread

regex_fname = re.compile(r'aclImdb/(train|test)/(pos|neg|unsup)/\d+_\d+.txt$')


def blocking_io(thread_name):
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with tarfile.open('aclImdb_v1.tar.gz', mode='r:gz') as tar:
        for member in tar.getmembers():
            if regex_fname.match(member.name):
                member_bytes = tar.extractfile(member).read()
                member_text = member_bytes.decode('utf-8', errors='replace')
                time.sleep(1)
                print(member_text)


_thread.start_new_thread(blocking_io, ("Thread-1",))


for i in range(100):
    time.sleep(1)
    print('No one stops me.')

while True:
    pass


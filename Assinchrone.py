from hashlib import md5
from random import choice
import time
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

j=0
start_time = time.time()
with PoolExecutor(max_workers=100) as executor:
    while j<3:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            j+=1
print(time.time() - start_time)
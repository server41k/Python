from random import *
import time
start_time = time.time()
a = 0
while True:
    a += randrange(-1, 2)
    print(a)
print("--- %s seconds ---" % (time.time() - start_time))

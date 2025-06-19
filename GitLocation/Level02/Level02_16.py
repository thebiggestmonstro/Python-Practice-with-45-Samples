import time
import numpy

def sleepBy(start, end):
    for i in numpy.arange(start + 0.5, end + 0.5, 0.5):
        print(f'Delayed for {i} seconds')
        time.sleep(i)

sleepBy(0, 3)


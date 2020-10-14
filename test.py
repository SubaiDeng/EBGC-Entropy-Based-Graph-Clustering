import numpy as np
from queue import Queue
from EBGC import EBGC

print('hello world')
a = [0, 2, 4]
b = np.array((range(10)))

t = EBGC()

l = [3, 4, 5]
q = Queue()
[q.put(x) for x in l]
q.put(1)
q.put(2)
q.put(3)
t_1 = q.get()
t_2 = q.get()
print(t_1)
print(t_2)
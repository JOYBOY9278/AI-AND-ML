import numpy as np
import timeit

# Vectorized sum
print(np.sum(np.arange(15)))
print("time taken by vectorized sum:", end="")
print(timeit.timeit(lambda: (np.arange(15))))

# Iterative sum
total = 0
for item in range(0,15):
    total += item
a = total
print("\n" + str(a))
print("time taken by iterative sum:", end="")
print(timeit.timeit(lambda:np.sum (a)))

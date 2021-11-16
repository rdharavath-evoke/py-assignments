import statistics
import math
import random

A = [5,10,6,21,5,17,14,8,3,9]
mean = statistics.mean(A)
print('The mean of A is ', mean)


B = [1,7,13,24,35,37,42,44,53,55]
median = statistics.median(B)
print('Median of B is:', median)


B = [1,7,13,24,35,37,42,44,53,55]
low_median = statistics.median_low(B)
print('Low Median of B is:', low_median)

B = [1,7,13,24,35,37,42,44,53,55]
high_median = statistics.median_high(B)
print('High Median of B is:', high_median)



x = 81
print('The square root of', x, 'is', math.sqrt(x))

x = 5.6
print('The ceil of', x, 'is', math.ceil(x))


result = random.randint(1, 11)
print('The random integer number in range [1,11] is:', result)


import fibo
fibo.fib(1000)
from fibo import fib, fib2
fib(500)

from fibo import *
fib2(500)


import mymodule
mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)


import mymodule as mx

a = mx.person1["age"]
print(a)


import platform

x = platform.system()
print(x)

# x = dir(platform)
# print(x)
import math
a = 1
b = 2
c = 3
fib = [1, 2]
even = []
i = 1
while (c < 4000000):
    fib.append(c)
    a,b = b,c
    c = a + b
while (3 + i) <= (len(fib)+2):
    even.append(fib[i])
    i = i + 3
print sum(even)
raw_input()

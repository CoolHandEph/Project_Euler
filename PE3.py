import math
a = int(raw_input("Enter the number you wish to factor: "))
f = 2
factors = []
while f < (a + 1):
        if a % f == 0:
                factors.append(f)
                a = a / f
        elif a % f != 0:
                f = f + 1
print factors
print "The largest prime factor is", factors[-1]
raw_input()

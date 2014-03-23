import math
n = range(1,1001)
value = 0
for i in n:
	if int(i % 15) == 3 or int(i % 15) == 5 or int(i % 15) == 6 or int(i % 15) == 9 or int(i % 15) == 10 or int(i % 15) == 12 or int(i % 15) == 0:
		value = value + i
print value

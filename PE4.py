import math
product =[]
for a in range(100, 999): #and b in range(100, 900):
    for b in range(100, 999):
        a = float(a)
        b = float(b)
        p = math.trunc((a * b) / 1000)
        c = str(p)
        if len(c) == 3:
            d = format(((a*b)/1000) - p, '.3f')
            s = str(d)
            if int(float(''.join(s[::-1]))) == int(float(c)):
                if a*b not in product:
                    product.append(a*b)
print product
print max(product)
print "There are", len(product), "palindromes."

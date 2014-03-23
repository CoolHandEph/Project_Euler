import math
import copy
primes = []
#def findprimes():
#    while a > 0:
max_number = int(raw_input("Max number: "))
counter = 1
#for a in range(20, 2):
#    for b in range(20, a):
#        if 
unique_factors = {}
count_factors = {}

for ceiling in range(2, max_number + 1):
        unique_factors[ceiling] = []
        current_ceiling = copy.deepcopy(ceiling)
        count_factors_pre = {}
        for factor_test in range(2, int(math.ceil(math.sqrt(ceiling) + 1))):
                while current_ceiling % factor_test == 0:
                        unique_factors[ceiling].append(factor_test)
                        if factor_test not in count_factors_pre.keys():
                                count_factors_pre[factor_test] = 0
                        count_factors_pre[factor_test] += 1
                        current_ceiling  = current_ceiling / factor_test
                        if current_ceiling == 1:
                                break
        if current_ceiling != 1:
                unique_factors[ceiling].append(current_ceiling)
                count_factors_pre[current_ceiling] = 1

        print count_factors_pre

        for prime, times_divide in count_factors_pre.iteritems():
                if prime not in count_factors.keys():
                        count_factors[prime] = times_divide
                else:
                        count_factors[prime] = max(times_divide, count_factors[prime])


             
                # elif ceiling % factor_test != 0 and ceiling != 2:
                #         factor_test += 1
                #         primes.append(counter)
                # elif ceiling == 2:
                #         factor_test = 2
                #         ceiling = max_number - counter
                #         counter += 1
#print primes
print unique_factors
print count_factors

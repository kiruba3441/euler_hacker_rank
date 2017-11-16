import math
from collections import OrderedDict


def get_prime_factors(n):
    nval = n
    prime=set()
    prime_counter={}
    while n & 1 == 0:
        n = n//2
        prime.add(2)

    while n % 3 == 0:
        n = n//3
        prime.add(3)

    while n % 5 == 0:
        n = n//5
        prime.add(5)

    while n % 7 == 0:
        n = n//7
        prime.add(7)

    end = math.ceil(n**0.5)
    i = 7
    while i <= end:
        count = 0
        if n % i == 0:
            while n % i == 0:
                n = n // i
            prime.add(i)
            end = math.ceil(n ** 0.5)
            i = 7
        else:
            i += 2
    prime.add(n)
    total_factors = 1
    for p in prime:
        num = nval
        pow = 0
        while num%p == 0 and p>1:
            num = num//p
            pow+=1
        total_factors*= (pow+1)

    return total_factors

sum = 0
index = 0
max_factors=0
factor_num = OrderedDict()
while max_factors<1000:
    index+=1
    sum += index
    temp_factor = get_prime_factors(sum)
    if sum == 76576500:
        print("for sum {}  factors are {} ".format(sum,temp_factor))
    if not factor_num.get(temp_factor):
        factor_num[temp_factor] = sum
        max_factors = max(temp_factor,max_factors)


#print(factor_num)
n=500
for k in (factor_num.keys()):
    if k > n :
        print(factor_num[k])
        break


print(factor_num[576])

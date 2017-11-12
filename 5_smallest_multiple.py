import math


def get_prime_factors(n):
    prime=set()
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
        if n % i == 0:
            while n % i == 0:
                n = n // i
            prime.add(i)
            end = math.ceil(n ** 0.5)
            i = 7
        else:
            i += 2
    prime.add(n)
    prime.remove(1)
    return prime


#takes way too much time
def lcm_approach(n):
    a = 2
    lcm = 1
    for i in range(3,n+1):
        b = i
        lcm = (a*b)//gcd(a,b)
        a = lcm
    return lcm

def gcd(a,b):
    while(a!=b):
        if a>b:
            a = a-b
        elif a<b:
            b = b-a
    return a

def smallest_multiple(n):
    primes = set([2,3,5,7,11,13,17,19,23,29,31,37])
    result = 1
    prime_counter = {}
    for i in primes:
        if i <= n:
            result *= i
            prime_counter[i]=1

    for i in range(2, n+1):
        if result % i != 0:
            prime_factors = get_prime_factors(i)
            for pf in prime_factors:
                division_possible = pf**prime_counter[pf]
                if division_possible%i != 0:
                    pending = i//division_possible
                    prime_counter[pf] = prime_counter[pf]+int(math.log(pending, pf))

    fin_result = 1
    for key, value in prime_counter.items():
        fin_result = fin_result*(key**value)
    return fin_result


print(smallest_multiple(40))
print(lcm_approach(40))

#2->8
#3->4
#5->2
#7->1

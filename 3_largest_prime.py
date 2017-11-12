import math

def prime_factors(a,b,primes):
    print("{}/{}".format(b,a))
    if a > b**(0.5):
        primes.add(b)
        return primes
    else:
        while b & 1 == 0:
            b = b//2
            primes.add(2)
        if b % a == 0:
            while b % a == 0:
                b = b // a
            primes.add(a)
            return prime_factors(3,b,primes)
        else:
            a = a + 2
            return prime_factors(a, b, primes)



def get_max_prime_factor(n):
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
    while(i <= end):
        if (n % i == 0):
            while n % i == 0:
                n = n // i
            prime.add(i)
            end = math.ceil(n ** 0.5)
            i = 7
        else:
            i += 2
    prime.add(n)
    return max(prime)

#print(prime_factors(3,6789631,set()))
#6789631
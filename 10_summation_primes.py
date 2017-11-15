import math


def sieves_memoize():
    n=1000001
    sieve = [False] * (n+1)
    prime_sum_memoized = [0]*(n+1)
    if n<=1:
        return 0
    if n<3:
        return 2
    prime_sum=2
    end = math.ceil(n**0.5)
    for i in range(3,end,2):
        if not sieve[i]:
            prime_sum+= i
            for j in range(2*i,n+1,i):
                sieve[j] = True

    prime_sum_memoized[0]=0
    prime_sum_memoized[1] = 0
    prime_sum_memoized[2] = 2
    prime_sum_memoized[3] = 5
    for i in range(5,n+1,2):
        prime_sum_memoized[i]= prime_sum_memoized[i-2]
        prime_sum_memoized[i-1]= prime_sum_memoized[i-2]
        if not sieve[i]:
            prime_sum_memoized[i]+=i
    #print(primes)
    return prime_sum_memoized

#37550402023
memozied_primes = (sieves_memoize())
print(memozied_primes[5])
print(memozied_primes[100])
print(memozied_primes[1000000])

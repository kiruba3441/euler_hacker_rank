import math

def all_possible_3_digit_nums(n):
    num_combos = []
    num_to_prime_factors = {}
    for i in range(999,100,-1):
        num = int(str(i)+((str(i)[::-1])))
        if(num<n):
          for i in range(100,1000):
              if num%i == 0:
                  result = num // i
                  if 99 < result < 1000:
                      return num
    return None


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
    return prime



n = 800000
n = 101110
n = 101110
n = 1000000
print(all_possible_3_digit_nums(1000000))

print(get_prime_factors(906609))

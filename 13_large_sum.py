import sys


big_sum = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    big_sum+=n
print(str(big_sum)[0:10]) 
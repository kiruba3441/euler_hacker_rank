
n = int(input().strip())

for i in range(0,n):
    print(sum([int(i) for i in str(2**(int(input().strip())))]))
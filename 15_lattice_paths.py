from math import factorial


def compute_paths(x,y,result):
    if x == len(result)-1 and y == len(result[0])-1:
        return 1
    elif x > len(result)-1 or (y >len(result[0])-1):
        return 0
    else:
        if not result[x][y]:
            result[x][y] = compute_paths(x,y+1,result)+compute_paths(x+1,y,result)
        return result[x][y]%(10**9+7)



row,col=2,3
result = ((factorial(row + col) // (factorial(row) * factorial(col))) % 1000000007)
print(result)

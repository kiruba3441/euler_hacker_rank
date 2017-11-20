

def compute_max_sum(level,index,input,result):
    if level == len(input)-1 :
        result[level][index] = input[level][index]
    else:
        if not result.get(level).get(index):
            left =  compute_max_sum(level+1,index,input,result)
            right = compute_max_sum(level+1,index+1,input,result)
            result[level][index] = max(left,right)+input[level][index]
    return result[level][index]



'''
rows = 4
input = [[]]*rows
input[0] = [3]
input[1] = [7,4]
input[2] = [2,4,6]
input[3] = [8,5,9,3]
result={}
result[0] = {}
result[1] = {}
result[2] = {}
result[3] = {}
print(compute_max_sum(0,0,input,result))

print(result)

1
4
3
7 4
2 4 6
8 5 9 3
'''

t = int(input().strip())
for i in range(0,t):
    rows = int(input().strip())
    print(rows)
    elements = []*rows
    result = {}
    for j in range(0,rows):
         elements.append([int(el) for el in input().strip().split(' ')])
         result[j] = {}
    print(compute_max_sum(0, 0, elements, result))



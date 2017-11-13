

def sum_square_diff(num):
    sum = 0
    #(a+b)^2 -a^2-b^2 = 2(ab)
    #(a+b+c)^2 -a^2-b^2-c^2 = 2(ab+ac+cb)
    for i in range(1,num):
        n = num-i
        '''
          (1.2+1.3+1.4+1.5..1.10)
          1*(2+3+4...10)
          1*(1+1,1+2,1+3...1+9)
          1*(9.1 + (1+2+3+...9))
          1*(9.1 + (9*(9+1)/2)) 
        '''
        sum += i*((n*i)+(n*(n+1))//2)
    return sum*2


def sum_square_diff_formula(n):
    return ((((n**2))*((n+1)**2))//4)-((n*(n+1)*(2*n+1))//6)

n=3
print(sum_square_diff_formula(n))
print(sum_square_diff(n))
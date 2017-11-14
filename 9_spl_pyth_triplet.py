import math


def get_max_pyth_triplet(n):
    max_product = -1
    e = n//2
    print(e)
    for i in range(e,1,-1):
        test_b_remainder = ((n*(n-(2*i)))%(2*(n-i)))
        if test_b_remainder == 0 :
            b = ((n*(n-(2*i)))//(2*(n-i)))
            c = i*b*(n-i-b)
            print("{} X {} X {}".format(i,b,(n-i-b)))
            max_product = c if c > max_product else max_product
    return -1 if max_product==0 else max_product


print(get_max_pyth_triplet(60))

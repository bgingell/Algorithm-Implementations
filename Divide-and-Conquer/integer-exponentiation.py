def int_to_exp(a, b):
    if(b == 1):
        return a
    else:
        if(b % 2 == 0):
            c = int_to_exp(a, b//2)
            return c * c
        else:
            c = int_to_exp(a, (b-1)//2)
            return a * c * c



print(int_to_exp(3, 21))

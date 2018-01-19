# implementation of mergesort
# probably could be more concise and could certainly
# use less space

def merge(a, b):
    if(len(a) == 0):
        return b
    elif (len(b) == 0):
        return a
    else:
        answ = []
        k = 0
        i = 0
        while(i < len(a) and k < len(b)):
            if(a[i] <= b[k]):
                answ.append(a[i])
                i += 1
            else:
                answ.append(b[k])
                k += 1
        if(i < len(a)):
            answ += a[i:]
        elif (k < len(b)):
            answ += b[k:]
        return answ

def mergesort(a):
    if(len(a) == 1):
        return a
    else:
        one = mergesort(a[:(len(a)//2)])
        two = mergesort(a[len(a)//2:])
        return merge(one, two)


a = [10, 9, 8, 6, 7, 5, 4, 3, 1]
print(mergesort(a))

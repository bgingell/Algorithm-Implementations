def merge_and_count(a, b):
    if(len(a) == 0):
        return b
    elif (len(b) == 0):
        return a
    else:
        answ = []
        k = 0
        i = 0
        inversions = 0
        while(i < len(a) and k < len(b)):
            if(a[i] <= b[k]):
                answ.append(a[i])
                i += 1
            else:
                answ.append(b[k])
                inversions += len(a[i:])
                k += 1
        if(i < len(a)):
            answ += a[i:]
        elif (k < len(b)):
            answ += b[k:]
        return inversions, answ

def sort_and_count(a):
    if(len(a) == 1):
        return 0, a
    ra, one = sort_and_count(a[:len(a)//2])
    rb, two = sort_and_count(a[len(a)//2:])
    r, l = merge_and_count(one, two)
    return ra+rb+r, l

a = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
print(sort_and_count(a))

# precondition that a is sorted
def binarysearch(a, target):
    if(a[len(a)//2] == target):
        return len(a)//2
    elif (target < a[len(a)//2]):
        return binarysearch(a[:len(a)//2], target)
    else:
        return len(a)//2 + binarysearch(a[len(a)//2:], target)
    return

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarysearch(a, 8))

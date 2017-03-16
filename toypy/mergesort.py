def mergesort(a):
    if not a:
        raise ValueError("a must not be empty")
    if (len(a) == 1):
        return
    mid = int(len(a) / 2)
    left = a[:mid]
    right = a[mid:]
    mergesort(left)
    mergesort(right)
    merge(left, right, a)
    
def merge(left, right, a):
    if not a:
        raise ValueError("a must not be empty")
    if not left:
        raise ValueError("left must not be empty")
    if not right:
        raise ValueError("right must not be empty")
    i = 0
    j = 0
    k = 0
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while (i < len(left)):
        a[k] = left[i]
        i += 1
        k += 1
    while (j < len(right)):
        a[k] = right[j]
        j += 1
        k += 1

a = [5, -1, 2, 7, 6, 3]
mergesort(a)
print a
def quicksort(a):
    lo = 0
    hi = len(a) - 1
    quicksort_rec(a, lo, hi)

def quicksort_rec(a, lo, hi):
    if not a:
        raise ValueError("a must not be empty")
    if lo < 0:
        raise IndexError("lo must be greater than or equal to zero")
    if hi >= len(a):
        raise IndexError("hi must be less than or equal to the index of the last element")
    """
    Base case: array of len 1 is already sorted
    """
    if lo >= hi:
        return
    iPivot = partition(a, lo, hi)
    #print "lo [%d] hi [%d] iPivot [%d]" % (lo, hi, iPivot)
    quicksort_rec(a, lo, iPivot - 1)
    quicksort_rec(a, iPivot + 1, hi)
    
def partition(a, lo, hi):
    pivot = a[hi]
    iPivot = lo
    """
    Stop before hi 
    because a[hi] will be swapped with a[iPivot]
    """
    for i in xrange(lo, hi):
        if a[i] <= pivot:
            swap(a, i, iPivot)
            iPivot += 1
    swap(a, hi, iPivot)
    return iPivot
        
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    
a = [5, -1, 2, 7, 6, 3]
quicksort(a)
print a

a = [-1]
quicksort(a)
print a
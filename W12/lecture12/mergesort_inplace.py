import pdb
import doctest

#mergeSort: Recursive Divide-and-Conquer algorithm.

#This procedure assumes left and right are sorted lists in ascending order,
#and merges them to produce a sorted list in ascending order.
#This procedure modifies L to a list that is in sorted order.

def mergeSort(L, beg=-1, end=float("inf")):
    # Initial limits
    beg = max(beg, 0)
    end = min(end, len(L))
    
    # Base Case
    if end - beg < 2:
        return

    middle = (beg + end)//2
    mergeSort(L, beg, middle)
    mergeSort(L, middle, end)
    merge(L, beg, middle, end)


def merge(L, beg, middle, end):
    # Base Cases
    if end - beg < 2 or middle - beg < 1 or end - middle < 1:
        return
    
    # Initialization of Left and Right Pointers
    ptr_left, ptr_right = middle - 1, middle
    
    # Move pointers until left is less than right
    # Or until one of the pointers hits the boundary
    while ptr_left >= beg and ptr_right < end and L[ptr_left] > L[ptr_right]:
        ptr_left, ptr_right = ptr_left - 1, ptr_right + 1
    
    # Fix pointer overshoot
    ptr_left += 1
    ptr_right -= 1
    
    # If left pointer hits boundary
    # But left is still greater than right
    if ptr_left == beg:
        while ptr_right < end and L[ptr_left] > L[ptr_right]:
            ptr_right += 1
        # Fix pointer overshoot
        ptr_right -= 1
    
    # If right pointer hits boundary
    # But left is still greater than right
    elif ptr_right == end - 1:
        while ptr_left >= beg and L[ptr_left] > L[ptr_right]:
            ptr_left -= 1
        # Fix pointer overshoot
        ptr_left += 1

    # Rotate the two segments
    rotate(L, ptr_left, middle, ptr_right + 1)
    
    # Recursive merge
    merge(L, beg, ptr_left, middle)
    merge(L, middle, ptr_right + 1, end)


def rotateByOne(L, beg, end):
    """
    Rotation by one unit. Shifts the range [beg, end) forward
    and cycles the entry at end back to the beginning.
    >>> L = list(range(10))
    >>> beg, end = 3, 7
    >>> rotateByOne(L, beg, end)
    >>> L
    [0, 1, 2, 6, 3, 4, 5, 7, 8, 9]
    """
    temp = L[end-1]
    for i in range(beg, end):
        L[i], temp = temp, L[i]

def rotate(L, beg, middle, end):
    """
    Full Rotation. Shifts the range [beg, middle) forward
    and cycles the range [middle, end) back to the beginning.
    >>> L = list(range(10))
    >>> beg, middle, end = 2, 5, 7
    >>> rotate(L, beg, middle, end)
    >>> L
    [0, 1, 5, 6, 2, 3, 4, 7, 8, 9]
    """
    for _ in range(middle, end):
        rotateByOne(L, beg, end)


inp = [23, 3, 45, 7, 6, 11, 14, 12]


##if __name__ == '__main__':
##    doctest.testmod()
##    
##    import random
##
##    inp = [random.randint(0,1000000) for _ in range(1000)]
##    L = inp[:]
##    inp.sort()
##    mergeSort(L)
##    print('PASS' if L == inp else 'FAIL')



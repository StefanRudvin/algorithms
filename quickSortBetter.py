import random

def quickSort(l, low, high):
    if ((high - low) < 1): return []

    pivot = partition(l, low, high)
    quickSort(l, low, pivot)
    quickSort(l, pivot + 1, high)

def partition(l, left, right):
    print(l)
    smaller = left
    larger = right -1
    pivot = l[right -1]

    while (larger > smaller):
        if (l[larger - 1] > pivot):
            l[larger] = l[larger - 1]
            larger -= 1
        else:
            help = l[larger -1]
            l[larger -1] = l[smaller]
            l[smaller] = help
            smaller += 1
    l[larger] = pivot
    print(l)
    return larger


l = [95,5,3,8,9,7,7,7]
quickSort(l, 0, len(l))
print(l)
          l
[3, 1, 2, 1]
 s  h  l
[3, 1, 2, 2]
    s  l
[1, 3, 2, 2]

[1, 3, 2, 2]





[3, 1, 2, 2]

[3, 1, 2, 2]


#               x     x
# [95, 5, 3, 8, 7, 7, 7, 9]
#
# [95, 5, 3, 8, 7, 7, 7, 9]
#  x         x     x
# [95, 5, 3, 7, 7, 7, 8, 9]
#                  x
# [7, 5, 3, 7, 7, 95, 8, 9]
#
# instead
#
# [3, 5, 7, 7, 7, 95, 8, 9]

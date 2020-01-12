import random

def quickSort(l):

    if (len(l) == 0):
        return []

    pivotIndex = random.randint(0, len(l) - 1)
    pivotValue = l[pivotIndex]

    print(pivotIndex)
    print(pivotValue)

    low = []
    high = []

    for (i, num) in enumerate(l):
        if i != pivotIndex:
            if num <= pivotValue:
                low.append(num)
            else:
                high.append(num)
    return quickSort(low) + [pivotValue] + quickSort(high)

l = [5,3,2,5,6,7,8,2,9]

print(quickSort(l))

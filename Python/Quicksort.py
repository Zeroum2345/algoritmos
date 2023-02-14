listToSort = [3,5,1,6,8,2,1,8,1,6,9,0,6,7,4]

print('- List before quicksort:', listToSort)

# Quicksort
def quicksort(listToSort, start, end):
    if start < end:
        pivot_index = partition(listToSort, start, end)
        quicksort(listToSort, start, pivot_index-1)
        quicksort(listToSort, pivot_index+1, end)

def partition(listToSort, start, end):
    pivot = listToSort[end]
    i = start

    for j in range(start, end):
        if listToSort[j] <= pivot:
            listToSort[j], listToSort[i] = listToSort[i], listToSort[j]
            i += 1

    listToSort[i], listToSort[end] = listToSort[end], listToSort[i]

    return i

quicksort(listToSort, 0, len(listToSort)-1)

print('- List after quicksort:', listToSort)
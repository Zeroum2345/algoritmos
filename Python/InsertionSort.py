listToSort = [3,5,1,6,8,2,1,8,1,6,9,0,6,7,4]

print('- List before insertion sort:', listToSort)

# Insertion Sort 
for i in range(len(listToSort)):
    current = i
    # Compare current number with the one behind it and change if is lower
    while current > 0 and listToSort[current] < listToSort[current-1]:
        listToSort[current], listToSort[current-1] = listToSort[current-1], listToSort[current]
        current -= 1

print('- List after insertion sort:', listToSort)
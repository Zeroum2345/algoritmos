listToSort = [3,5,1,6,8,2,1,8,1,6,9,0,6,7,4]

print('- List before bubble sort:', listToSort)

# Bubble Sort
for i in range(len(listToSort)):
    # Do this to test all the list
    for j in range(len(listToSort)):
        if j != 0 and listToSort[j] < listToSort[j-1]:
            listToSort[j], listToSort[j-1] = listToSort[j-1], listToSort[j]

print('- List after bubble sort:', listToSort)
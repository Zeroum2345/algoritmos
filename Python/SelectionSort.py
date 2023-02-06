listToSort = [3,5,1,6,8,2,1,8,1,6,9,0,6,7,4]

print('- List before selection sort:', listToSort)

#Selection sort
for i in range(len(listToSort)):
    lowerNumberIndex = i

    #Find the lower value after i
    for j in range(i, len(listToSort)):
        lowerNumber = listToSort[lowerNumberIndex]
        
        if(listToSort[j] < lowerNumber):
            lowerNumberIndex = j

    # Change values in the list
    listToSort[i], listToSort[lowerNumberIndex] = listToSort[lowerNumberIndex], listToSort[i]

print('- List after selection sort:', listToSort)
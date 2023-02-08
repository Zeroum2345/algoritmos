listToSort = [3,5,1,6,8,2,1,8,1,6,9,0,6,7,4]

print('- List before merge sort:', listToSort)

# Merge sort

def merge_sort(listToSort, start, end):
    if (end - start) > 1:
        center = (start + end) // 2
        merge_sort(listToSort, start, center)
        merge_sort(listToSort, center, end)
        merge(listToSort, start, center, end)

def merge(listToSort, start, center, end):
    left_list = listToSort[start:center]
    right_list = listToSort[center:end]
    right_index, left_index = 0, 0

    for i in range(start, end):
        if left_index >= len(left_list):
            listToSort[i] = right_list[right_index]
            right_index += 1   

        elif right_index >= len(right_list):
            listToSort[i] = left_list[left_index]
            left_index += 1

        elif left_list[left_index] < right_list[right_index]:
            listToSort[i] = left_list[left_index]
            left_index += 1

        else:
            listToSort[i] = right_list[right_index]
            right_index += 1

# --------------------------------------------------------------

merge_sort(listToSort, 0, len(listToSort))

print('- List after merge sort:', listToSort)

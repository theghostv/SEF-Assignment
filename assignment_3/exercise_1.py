"""
Always comment your work it makes it easy to you
and to the person reading the code  
"""
# the list must be sorted in the binary search 
#in worst case we make a sorting function 
def selectionSort(list1):
    for index_unsorted in range(0,len(list1)):
    # the smallest index of the unsorted list will be contained in minIndex  
        minIndex = index_unsorted
# now we search for the min 
        for i in range(index_unsorted, len(list1)):
            if list1[i]<list1[minIndex]:
                minIndex = i
# now we swap them
        list1[minIndex],list1[index_unsorted]=list1[index_unsorted],list1[minIndex]
    return list1

def binarySearch(list1, key, start=0, end=None):
    # sort the list using selection sort
    sorted_list =selectionSort(list1) 
    if end is None:
        end = len(sorted_list)-1 
# base case: if start surpasses end
    if start > end:
        return False
# now we calculate the mid of the list
    mid = (start + end) // 2
# checking if the middle index is the key
    if sorted_list[mid] == key:
        return True
# if the key is smaller it goes in the left side
    if sorted_list[mid] > key:
        return binarySearch(sorted_list, key, start, mid -1)
# if the key is bigger, it goes on the right side
    if sorted_list[mid] < key:
        return binarySearch(sorted_list, key, mid +1, end)


example=[12,99,73,-21,1,2,3,31,15]    

print(binarySearch(example, 99))
print(binarySearch(example,101))
print(binarySearch(example, -21))
print(binarySearch(example, 3))


def insertionSort(list1):
    
    for sorted_index in range(0,len(list1)-1):
        unsorted_element_index=sorted_index+1       
        
        while unsorted_element_index > 0 and list1[unsorted_element_index] < list1[unsorted_element_index-1]:
            
            temp=list1[unsorted_element_index]
            list1[unsorted_element_index]=list1[unsorted_element_index-1]
            list1[unsorted_element_index-1]=temp
            unsorted_element_index=unsorted_element_index-1
    print(list1)    
example=[1,34,56,78,89]
# we ask an input from the user
val=int(input("Enter value: "))
example.append(val)
insertionSort(example)


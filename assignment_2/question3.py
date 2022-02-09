def selectionSort(arr, size):
    i = 0
    for i in range(0, size-1): ## for int i in range 0, till size-1
        unsortedMin = i ## the min value of the list is i
        j = i + 1 # j, another variable is i + 1
        while (j < size): # while  j is less than size
            if arr[j] < arr[unsortedMin]: # and if arr[j] is smaller than arr at min
                unsortedMin = j # min is now equal to j
            j = j + 1 # add one to j
        temp = arr[i] # temporary variable is equal to arr at i
        arr[i] = arr[unsortedMin] ## arr at i is equal to arr at unsortedMin
        arr[unsortedMin] = temp ## arr at unsorted min is equal to temp
listArr = [0, 68, 41, 88, 16, 40, 65, 97, 85] # unsorted list
print(listArr) # print the old list
sizeOfList = len(listArr) # assign the size of the list to sizeOfList
selectionSort(listArr, sizeOfList) # perform the sort
print(listArr) # print the sorted array

# [This program will sort a list of random numbers by quicksort implementation.]
# Author: @matheusphalves



itens = input("").split() #Insert here your list spaced by ' ' 
itens = [int(x) for x in itens]

def partition(array, left, right, pivot):
    i = left
    while i <= right:      #if i > right, all of elements are greater than the pivot
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[right] = array[right], array[i]
            right -= 1
        else:
            i += 1
           
    return left, right      # range between pivot's repeated elements

def quickSort(array, left, right):  
    if left >= right:
        return
    else:
        pivot = array[left]# pivot changed: left elements are smaller and right are taller
        kLeft, kRight = partition(array, left, right, pivot)
        quickSort(array, left, kLeft-1)#'centers' are send to sorting
        quickSort(array, kRight+1, right) 
    return array
    

#START PROGRAM
listFinal = quickSort(itens, 0, len(itens)-1)
for x in listFinal:
        print(x, end=' ')
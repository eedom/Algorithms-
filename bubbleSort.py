
# runs in O(n^2) time | O(1) space

def bubbleSort(array):
    '''Check is it is sorted '''

    #check if it is sorted
    isSorted = False
    counter = 0
   
    while not isSorted:
        isSorted = True
        for i in range(len(array) -1 - counter):  
            if array[i] > array[i+1]:
                swap(i, i +1, array)
                #we assume the array is not sorted
                isSorted = False
        counter+=1
    return array

def swap(i, j, array):
    array[i], array[i+1] = array[j], array[i]

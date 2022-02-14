# Recursive implementation of the binary search algorithm
# Runs in O(log n) time | O(log(n)) space time
def binary_Search(a_list, target):

    #A helper function that takes left and right pointer and only returns the result of that helper method
    return binary_SearchHelper(a_list, target, 0, len(a_list)- 1)


def binary_SearchHelper(a_list, target,left,right):

    #check if we are at the base case
    if left > right:
        return -1
    middle_num = (left + right) // 2
    potentialMatch = array[middle_num]

    if target == potentialMatch:
        return middle_num
    elif target < potentialMatch:
     
        return binary_SearchHelper(a_list, target, left,  middle_num -1)
    else:
        return binary_SearchHelper(a_list, target,  middle_num +1, right )
      

      
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print( binary_Search(array, target))

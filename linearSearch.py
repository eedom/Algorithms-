
def linearSearch(array, target):
  '''Ths function does LinearSearch'''
  number_comarisons = 0
  item_found = False
  index= 0
  while num_comparisons < len(array) and not item_found:
      num_comparisons = num_comparisons + 1
      if array[index] == target:
        item_found = True
      index =+ 1
  return(item_found, num_comparisons)

array = [8, 5, 2, 9, 4, 6, 3]
target = 6
print(linearSearch(array,target))      

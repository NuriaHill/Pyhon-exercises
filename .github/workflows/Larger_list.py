#this funtion return the last element of the list that contain more elements. 
def larger_list(lst1,lst2):
  if len(lst1)>=len(lst2):
    return lst1[-1]
  else: 
    return lst2[-1]
#testing the function:
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10,6]))
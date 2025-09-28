#Every command related to lists:
#Always remember that index 0 is the first place in a list
# append,
# copy, 
# count, 
# extend, 
# index, 
# insert, 
# pop, 
# remove, 
# reverse, 
# sort
# clear, 

ListEx = [5, 7, 3, 2, 6, 10, 1, 8, 4, 9]
print('normal list:', ListEx)

#append:(puts a value at the end of the list)
ListEx.append(2)
print("list.append(2) =", ListEx)

#copy:(returns a copy of the list)
ListCopy = ListEx.copy()
print("(copies the list)list.copy() =", ListCopy)

#count:(returns the number of times a value appears in the list)
print("list.count(3) =", ListEx.count(3))

#extend:(add the elements of a list to the end of the current list)
ListEx.extend([11,12,13,14,15])
print("list.extend([11,12,13,14,15]) =", ListEx)

#index:(returns the index of the first occurrence of a value in the list)
print("list.index(2) =", ListEx.index(2))

#insert:(inserts an element at a specified position in the list)
ListEx.insert(0, 0)
print("list.insert(0, 0) =", ListEx)

#pop:(removes and returns the element at the specified position in the list)
ListEx.pop(3)
print("list.pop(3) =", ListEx)

#remove:(removes the first occurrence of a value in the list)
ListEx.remove(8)
print("list.remove(8) =", ListEx)

#reverse:(reverses the order of the elements in the list)
ListEx.reverse()
print("list.reverse() =", ListEx)

#sort:(sorts the elements of the list in ascending order)
ListEx.sort()   
print("list.sort() =", ListEx)

#clear:(removes all elements from the list)
ListEx.clear()
print("list.clear() =", ListEx)

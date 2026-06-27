#	Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.
listnums = [3,1,4,1,5]
print(listnums[0])
print(listnums[-1])
#Findthe length of the list colors = ['red', 'blue', 'green'].
colorlist = ['red', 'blue', 'green']
print(len(colorlist))
#3.	Append 'yellow' to the list colors = ['red', 'blue'].
colorlist = ['red','blue']
colorlist.append('yellow')
print(colorlist)
#	Insert 'orange' at index 1 in fruits = ['apple', 'banana'].
fruitlist = ['apple','banana']
fruitlist.insert(1,'orange')
print(fruitlist)
#5.	Remove 'banana' from fruits = ['apple', 'banana', 'grapes'].
fruitlist =  ['apple', 'banana', 'grapes']
fruitlist.remove('banana')
print(fruitlist)
#6.	Pop the last element from items = [10, 20, 30] and print the popped value.
itemslist = [10,20,30]
itemslist . pop()
print(itemslist)
#7.	Check if 3 is in the list nums = [1, 2, 3, 4].
listnums = [1, 2, 3, 4]
print(listnums[2])
#8.	Print the slice [2, 3] from the list [0, 1, 2, 3, 4].
listnums = [0,1,2,3,4]
print(listnums[2:3])
#9.	Replace the element at index 1 in a = [5, 10, 15] with 12.
elementnums = [5,10,15]
elementnums[1] = 12
print(elementnums)
#Count how many times 2 appears in [1, 2, 2, 3, 2]:
listnums = [1,2,2,3,2]
print(listnums.count(2))
#1.	Create a tuple t = (10, 20, 30) and print the second element.
tuple = (10,20,30)
print(tuple[1])
#2.	Find the length of tuple ('a', 'b', 'c').
tuple = ('a','b','c')
print(len (tuple))

#3.	Unpack the tuple (4, 5) into variables x and y.
X, Y = (4,5)
print(X)
print(Y)
#4.	Check if 'b' is in the tuple ('a', 'b', 'c').
tuple = ('a','b','c')
print('b'in tuple)
#5.	Create an empty tuple and print its type.
tuple = ()
print(type(tuple))
#6.	Concatenate (1, 2) and (3, 4) into a new tuple.
tuple1 = (1,2)
tuple2 = (3,4)
new_tuple = tuple1 + tuple2
print(new_tuple)
#7.	Repeat (7,) three times.
tuple = (7,)
print(tuple*3)
#8.	Find the index of 2 in (1, 2, 3, 2).
tuple = (1,2,3,2)
print(tuple.index(2))
#9.	Count how many times 2 appears in (1, 2, 3, 2).
tuple = (1,2,3,2)
print(tuple.count(2))
#10.	Create a single‑element tuple containing the value 5.
tuple = (5,)
print(tuple)
#1.	Create a set from [1, 2, 2, 3] and print it.
set = {1,2,2,3}
print(set) #set mn same value repeat nhi hoti
#2.	Add element 4 to the set {1, 2, 3}.
set = {1,2,3}
set.add(4)
print(set)
#3.	Remove element 2 from the set {1, 2, 3}.
set = {1,2,3}
set.remove(2)
print(set)
#5.	Check if 5 is in the set {1, 3, 5}.
set = {1,3,5}
print(5 in set)
#6.	Find the length of set {10, 20, 30}.
set = {10,20,30}
print(len(set))
#7.	Clear all elements from the set {1, 2, 3}.
set = {1,2,3}
set.clear()
print(set)
#8.	Create a set {'a', 'b'} and add 'c' only if it’s missing.
set = {'a','b',}
set.add('c')
print(set)
#9.	Convert list ['a', 'a', 'b'] into a set to remove duplicates
set ={ 'a','a','c'}

print(set)
#10.	Create two sets and print their union.
set1 = {1,2}
set2 = {2,3}
new_set = set1.union (set2)
print(new_set)
# 1.	Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
dict = {'name': 'Ali', 'age': 25}
print(dict['name'])
#2.	Add key 'city': 'Lahore' to a dictionary.

dict['city'] = 'lahore'
print(dict)

# 3.	Change 'age' in {'name': 'Ali', 'age': 25} to 30.
dict =  {'name': 'Ali', 'age': 25} 
dict['age'] = 30
print(dict)
# 4.	Delete key 'age' from a dictionary.
dict = {'name': 'Ali', 'age': 25}
dict.pop('age')
print(dict)
#	Check if key 'salary' exists in a dictionary.
dict = {'name': 'Ali', 'age': 25} 
print('sallery' in dict)
#6.	Print all keys from {'a': 1, 'b': 2}.
dict = {'a': 1, 'b': 2}
print(dict.keys())
# 7.	Print all values from a dictionary.
dict = {'a': 1, 'b': 2}
print(dict.values())
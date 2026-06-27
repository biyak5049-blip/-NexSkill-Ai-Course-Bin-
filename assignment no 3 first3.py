#1.	Create a list comprehension that returns the squares of only the even numbers from 0–20.
list = [x**2 for x in range(21) if x % 2 == 0]
print(list)
#2.	Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
numbs = [3,1,4,1,5,9]
new_list = sorted (numbs)
print("orignal:", numbs)
print("sorted:", new_list)
#3.	Remove duplicates from a list while preserving the original order.
numbs = [3,1,4,1,5,9]
numbs.remove(1)
print(numbs)
#4.	Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension.
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist ]
print(flat)
#	Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore case.
names = ['alice', 'Bob', 'charlie', 'DAVID']
names.sort()
print(names)
#6.	Replace items from index 2–4 in a list with [100, 200] using slice assignment.
list = [2,3,4,5,6,5,8]
numbs[2:4] = [100,200]
print(numbs)
# Write a program to find all indices of a value in a list (e.g., all indices of 7).
list = ["a: "'20', "b:"'30', "c: ",'40']
print(list[0])
print(list[1])
#8.	Create a new list containing only elements that appear exactly once in the original list.
list = [1,6,3,6,5,6,7]
new_list = []
for item in list:
    if list.count(item) == 1:
       new_list.append(item)
print(new_list)
#9.	Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).
list = [1,3,2,4,5]
list = [list[-1]] + list[:-1]  #slice method
print(list)
#10.	Split a list into two lists: one with even numbers, one with odd numbers.
lst = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for item in lst:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)

print(even)
print(odd)
#1.	Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.

a,b,c,d = tuple([1,2,3,4])

print(a,b,c,d)

#2.	Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
#Tip: Use a comprehension: x[1].
t = (('a', 1), ('b', 2), ('c', 3))
second_elements = [x[1] for x in t]
print(second_elements)
#3.	Write a function that returns multiple values (sum, min, max) using a tuple.
#Tip: Return (..., ..., ...) and unpack later.
def values (x):
    return sum(x) , min(x), max(x)
a,b,c = values([10,20,30,40])
print(a,b,c)
#4.	Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
 #Tip: Use + to join them

t1 = (1, 2, 3)
t2 = (4, 5)
result = (t1 + t2)
print(result)
#5.	Given a tuple of numbers, find the element with the highest frequency.
#Tip: Loop through unique items using set(t)
t = (1, 2, 2, 3, 2, 4, 4)

result = max(set(t), key=t.count)

print(result)







6#.	Check if two tuples contain the same elements regardless of order.
#ip#: Compare sorted(tuple) values.
t1 = (1, 2, 3)
t2 = (3, 2, 1)

print(sorted(t1) == sorted(t2))






7.#	Extract the last three items from a tuple using slicing.
#Tip: Use negative indexing: t[-3:].


t = (10, 20, 30, 40, 50, 60)

print(t[-3:])



#8.	Concatenate a tuple with itself three times (repeat operation).
#Tip: Use tuple * 3.


t = (1, 2)

print(t * 3)



#9.	Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
#Tip: Use a comprehension inside tuple().


t = ((1, 2), (3, 4))

result = tuple(x for i in t for x in i)

print(result)


#10.	Store coordinates in tuples and calculate the Manhattan distance.
#Tip: Use absolute difference formula: abs(x1-x2) + abs(y1-y2).

p1 = (2, 3)
p2 = (5, 7)

distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

print(distance)
#1.	Given two sets, find elements that are in the first set but not the second.
#Tip: Use the - operator.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

print(set1 - set2)



#2.	Find common items between three sets using intersection.
#Tip: Use set1 & set2 & set3.
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
set3 = {3, 2, 6}

print(set1 & set2 & set3)



#.	Given a sentence, return all unique words in lowercase.
#: Split the string → lowercase → convert to set.
sentence = "Hello World Hello Python"

print(set(sentence.lower().split()))



#	Convert a list with duplicates into a set, then back to a sorted list.
#Use sorted(set(list)).

lst = [4, 2, 1, 2, 3, 4]

print(sorted(set(lst)))



#Check if one set is a strict subset of another.
#: Use < operator.

set1 = {1, 2}
set2 = {1, 2, 3}

print(set1 < set2)



#	Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.
# Write {x*x for x in ... if x % 3 == 0}.



result = {x*x for x in range(1, 16) if x % 3 == 0}

print(result)

#	Count how many duplicate values exist in a list using sets.
# Compare lengths: len(list) - len(set(list)).



lst = [1, 2, 2, 3, 4, 4, 5]

print(len(lst) - len(set(lst)))

#Write a program to remove all vowels from a string using a set.
#ip: Use a vowel set and filter characters.
vowels = {'a', 'e', 'i', 'o', 'u'}

text = "hello world"

result = "".join(ch for ch in text if ch.lower() not in vowels)

print(result)




#Find the symmetric difference between two sets.
#: Use the ^ operator.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 ^ set2)






#0.	Check if two strings are anagrams using set comparison (unique characters only).
#: Compare set(str1) with set(str2).


str1 = "listen"
str2 = "silent"

print(set(str1) == set(str2))

#1.	Count word frequencies in a sentence and store the results in a dictionary.
#Tip: Use d[word] = d.get(word, 0) + 1.
sentence = "apple banana apple orange banana apple"

d = {}

for word in sentence.split():
    d[word] = d.get(word, 0) + 1

print(d)








#Invert a dictionary where all values are unique.
#p: Swap key and value in a loop.
d = {"a": 1, "b": 2, "c": 3}

new_dict = {}

for key, value in d.items():
    new_dict[value] = key

print(new_dict)




#Merge two dictionaries where second dictionary overrides first.
# Use {**dict1, **dict2} or dict1 | dict2 (Python 3.9+).

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 10, "c": 3}

merged = {**dict1, **dict2}

print(merged)





#Group words by their first letter into a dictionary of lists.
# Use setdefault.


words = ["apple", "ant", "banana", "ball", "cat", "car"]

d = {}

for word in words:
    d.setdefault(word[0], []).append(word)

print(d)



#Filter a dictionary to keep only entries with values greater than 50.
# Use a dictionary comprehension.

d = {"A": 30, "B": 70, "C": 55, "D": 20}

new_dict = {k: v for k, v in d.items() if v > 50}

print(new_dict)







#Given a nested dictionary, safely access a deeply nested key.
# Chain .get() calls with default {}.
data = {
    "user": {
        "address": {
            "city": "Lahore"
        }
    }
}

city = data.get("user", {}).get("address", {}).get("city")

print(city)







#Write a dictionary comprehension that maps numbers 1–10 to their cubes.
# {x: x**3 for x in range(1,11)}.


cubes = {x: x**3 for x in range(1, 11)}

print(cubes)





#Find the key with the highest value in a dictionary.
#Use max(d, key=d.get).
d = {"Ali": 80, "Sara": 95, "Ahmed": 88}

highest = max(d, key=d.get)

print(highest)








#Combine two lists into a dictionary (keys from first list, values from second).
#: Use zip().


keys = ["name", "age", "city"]
values = ["Ali", 22, "Lahore"]

d = dict(zip(keys, values))

print(d)





#	Remove all keys from a dictionary whose values are None.
#: Check value before adding to new dict.

d = {
    "name": "Ali",
    "age": None,
    "city": "Lahore",
    "phone": None
}

new_dict = {k: v for k, v in d.items() if v is not None}

print(new_dict)













BookList = [22 , "think and grow rich",  25.6,  "Richard"]
print(BookList)

print(type(BookList))
print(len(BookList))

for X in BookList:
 print(X)
print(BookList[2])
print(BookList[3])
print(type(BookList[2]))
print(type(BookList[3]))
BookList.append("Richerd publisher")
print(BookList)
BookList.insert(1,1977)
print(BookList)
BookList.remove(22)
print(BookList)
BookList.pop(4)
print(BookList)

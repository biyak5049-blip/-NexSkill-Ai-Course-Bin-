BookSet = {22,"think and grow rich",25.5,"Richard"}
print(BookSet)
print(type(BookSet))
print(len(BookSet))

for X in BookSet:
    print(X)
BookSet.add(25.5)
print(BookSet)
BookSet.discard(25.5)
print(BookSet)
print("welcome to class 22 june 2026")
propertyId = 784
print(propertyId)
print(type(propertyId))
propertyprice = 50000.5
print(propertyprice)
print(type(propertyprice))
propertyarea = "gulberg"
print(propertyarea)
print(type(propertyarea))
propertyprice5 = (propertyprice*5)
print(propertyprice5)
print(type(propertyprice5))
propertycity = input("enter your city name")
print(propertycity)
print(type(propertycity))
propertyinfo = input("please enter property info")
print(propertyinfo)
print(len(propertyinfo))

for x in propertyinfo: 
    print(x)
    
st = propertyinfo
print(st[2:4:6])

number = int(input('enter a number:'))
if number > 0:
 print(f'{number}is a postive:')
 print('a statement outside the if statement:')
print('next run---')
print(int(input('enter a number')))

#python--if--else statement

if number > 0:
 print('postive number')

else:
  print('not a postive number')

  print('this statement is always executed')
  #python if--elif--else statement
  if number > 0:
    print('postive number')
elif number < 0:
print('negative number')

print('this statement is always executed')
print('run number---') 

  



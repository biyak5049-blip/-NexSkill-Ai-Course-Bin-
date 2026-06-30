MobileInfo =  input ( "Please enter your mobile info")
print (MobileInfo)
print(type(MobileInfo))
print(len(MobileInfo))
for i in MobileInfo:
    print(i)
first5  =  MobileInfo [ :5:1]
print(first5)

first5B  =  MobileInfo [ 0:5:1]
print(first5)

first10To115  =  MobileInfo [ 10:15:1]
print(first10To115)

firstTillEnd  =  MobileInfo [ 0::1]
print(first10To115)
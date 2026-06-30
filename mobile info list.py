MobileinfoList = [1,2,3,4]
print(MobileinfoList)
print(type(MobileinfoList))
print(len(MobileinfoList))
print(MobileinfoList[1])
for i in MobileinfoList:
    print(i)
MobileLength = float(input("Please enter your length"))
MobileinfoList.append(MobileLength)
print(MobileinfoList)


MobileinfoList.remove(2)
print(MobileinfoList)
MobileinfoList.insert(3 , 7)
print(MobileinfoList)
MobileinfoList.pop(2)
print(MobileinfoList)

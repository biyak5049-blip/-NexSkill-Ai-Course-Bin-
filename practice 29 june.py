print("welcome to practice 29 june 2026")
MobileName = input("please enter your mobile name") # enter name
print(MobileName)
print(type(MobileName))
print(len(MobileName))

for x in MobileName  :
    print(x)
    # my code ends here:
MobilePrice = float(input("please enter your MobilePrice"))
print(type(MobilePrice))

if MobilePrice > 5:
    print("Greater 5")
elif MobilePrice<3:
    print("less 3")
else:
    print("what ever.....") 
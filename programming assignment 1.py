#1.	Write a program to print "Hello, World!" and your name on two separate lines.
vars = "Hello, World!"
print(vars)
name = "shazia kareem"
print(name)
#2.	Ask the user for their favorite color using input() and print "Your favorite color is [color]".
#favoritecolor = input('black')
#print(favoritecolor)
#3.	Use a single print() statement to display three different words separated by a hyphen (-).
print("Apple-Banana-Mango")
#4.	Prompt the user for their birth year and print their age (assume the current year is 2026).
birthyear = 2004
age = 2026 - birthyear
print("your age is", age)

#5.	Print the result of $5 + 5$ such that the output is: The sum of 5 and 5 is 10.
result = ('$5 + $5')
print(('the sum of 5 and 5 is',5+5))
#6.	Use the end parameter in print() to join two separate print statements with a space.
print('hello',end ="")
print('world')
#7.	Write a program that takes two strings from the user and prints them joined together.
str1 = "hello"
str2 = "world"
print(str1+ ""+ str2)

#8.	Create a greeting that takes a user's name and prints "Welcome, [Name]!" in all uppercase.
#name = "shanzu"
#print("welcome, " +name+"!".upper())
#9.	Ask for a user's city and country, then print them in the format: "City, Country".
#cityname = input("lahore")
#countryname = input("pakistan")
#print("cityname" + "  " + "countryname")
#10.Experiment: What happens if you try to add a string and an integer in a print statement? Write a code snippet that fixes this using str().
age = 24
print("age:" + str(age))
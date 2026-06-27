#11.	Create an integer variable age and a float variable height. Print their types.
intage = 22
floatheight = 5.6
print(type(intage))
print(type(floatheight))

#12.	Store the value $3 + 4j$ in a variable. Print the variable and its type.
value = ('$3 + 4j$')
print(value)
print(type(value))
#13.	Create a boolean variable is_python_fun and set it to True.
is_python_fun = True
print(is_python_fun)



#14.	Method 1: Assign three different values to three variables in a single line.
a, b, c = 1,4,7
print(a,b,c)




#15.	Method 2: Assign the same value to three different variables in a single line.
a = b = c = 100
print(a,b,c)
#16.	Take a numeric input from a user and convert it to a float.
#num = float(input(25))
#print(num)

#17.	Take a string input "100" and convert it to an int.
str = "100"
print(str)
#18.	Create a variable with a complex number and print only its real part.

num = 4 + 5j
print(num.real)
#19.	Define a string variable containing a paragraph and print its length.
paragraph = "i am a shanzu khan and i am learning skills from arfa tower."
print(len(paragraph))
#20.	Swap the values of two variables a and b without using a third variable
a = 1
b = 5
a,b = b,a
print(a)
print(b)
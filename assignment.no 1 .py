#Question 1: 
#Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
#(Celsius * 9/5) + 32)
# Convert Celsius to Fahrenheit

celsius = float(input("enter temperature in celcius: "))

fahrenheit = (celsius * 9/5) + 32

#print("Temperature in Fahrenheit:", fahrenheit)
#Question 2: 
#Calculate Area of a Rectangle 
length = float(input("enter length: "))
width = float(input("enter width: "))
area = length * width
#print("area of rectangle:", area)

#Question 3: 
#Calculate Compound Interest 
#Use the formula: 
#CI = P * (1 + R/100)**T - P 
#Where P = principal, R = rate, T = time 
p = float(input("enter a principal: "))
R = float(input("enter a rate: "))
T = float(input("enter time: "))

CI = p * (1 + R/100)**T - p
print(CI)

#Question 4: 
#Perimeter of a Rectangle - Take length and width as input and calculate the perimeter. 
length = float(input("enter length"))
width = float(input("enter width"))
perimeter = 2 *(length + width)
print(perimeter)



#Question 5: 
#Average of Three Numbers - Input three numbers and print their average. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average:", average)




#Question 6: 
#Square and Cube of a Number - Ask the user for a number and display its square and cube. 
num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square:", square)
print("Cube:", cube)



#Question 7: 
#Distribute Items Equally - You have n candies and k students. 
n = int(input("Enter total candies: "))
k = int(input("Enter total students: "))

each = n // k
left = n % k

print("Each student gets:", each)
print("Candies left:", left)


#Write a program to find: 
#how many candies each student gets 
#how many are left 
#Question 8: 
#Calculate Profit or Loss 
#Input cost price and selling price. Display either: 
#Profit and amount, or 
#Loss and amount, or 
#No Profit No Loss 
cost = float(input("Enter cost price: "))
selling = float(input("Enter selling price: "))

if selling > cost:
    print("Profit:", selling - cost)
elif cost > selling:
    print("Loss:", cost - selling)
else:
    print("No Profit No Loss")




#Question 9: 
#Total Marks and Percentage 
#Input marks of 5 subjects. Print: 
# Total marks 
# Percentage 
# Average 
m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))
m4 = float(input("Enter marks 4: "))
m5 = float(input("Enter marks 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
average = total / 5

print("Total:", total)
print("Percentage:", percentage)
print("Average:", average)




#Question 10: 
#Salary Calculator 
#Input basic salary. Calculate: 
# HRA = 20% of basic 
# DA = 15% of basic 
# Total Salary = Basic + HRA + DA

basic = float(input("Enter basic salary: "))

HRA = basic * 20 / 100
DA = basic * 15 / 100
total_salary = basic + HRA + DA

print("HRA:", HRA)
print("DA:", DA)
print("Total Salary:", total_salary)
#Question 11: 
#Age in Months and Days 
#Input your age in years. Calculate and print age in: 
# Months 
# Days (approximate) 
age = int(input("Enter your age in years: "))

months = age * 12
days = age * 365

print("Age in months:", months)
print("Age in days:", days)










#Question 12: 
#Currency Converter (USD to PKR) 
#Input amount in USD. Convert using a fixed exchange rate. 
usd = float(input("Enter amount in USD: "))

rate = 285
pkr = usd * rate

print("Amount in PKR:", pkr)













#Question 13: 
#Sum of First N Natural Numbers 
#Input a number n, calculate sum of first n natural numbers. 
#Formula: sum = n * (n + 1) / 2
n = int(input("Enter a number: "))

sum = n * (n + 1) / 2

print("Sum of first", n, "natural numbers is:", sum)










#Question 14: 
#Percentage of Correct Answers 
#Input total questions and correct answers, and calculate the percentage score.
total = int(input("Enter total questions: "))
correct = int(input("Enter correct answers: "))

percentage = (correct / total) * 100

print("Percentage:", percentage)





#Question 15: 
#Speed, Distance, and Time 
#Input distance and time, and calculate speed. 
distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

speed = distance / time

print("Speed:", speed)




#Question 16: 
#Calculate Body Mass Index (BMI) 
3#Input weight (kg) and height (m), then calculate: 
#BMI = weight / (height ** 2) 
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

BMI = weight / (height ** 2)

print("BMI:", BMI)




#3Question 17: 
#3Convert Minutes to Hours and Minutes 
#Input number of minutes and convert to hours and remaining minutes. 
#Example: 130 minutes → 2 hours 10 minutes

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(hours, "hours", remaining_minutes, "minutes")
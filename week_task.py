# 1. Write a Python program to swap two variables without using a third variable.------------------------------------------
# a = 10
# b = 20

# print("a = ",a ,"b = ", b) 

# a,b = b,a
# print("a = ",a ,"b = ", b) 


# 2.Create a program that takes your name and age as input and prints them in a sentence.------------------------------------------

# name = input("Enter your Name :")
# age = int(input("Enter your age :"))

# print("Hello ",name, "you age",age) 

# 3.Write a program to calculate the area of a rectangle using user input for length and width.------------------------------------------

# length = int(input("Enter length :"))
# width = int(input("Enter length :"))

# rec = length * width 

# print("Area of Rectangle", rec)

# 4.Store your favorite movie name, release year, and rating in variables and print them in a formatted string.------------------------------------------

# movie_name = input("Enter Your Favorite movie Name :")
# release_year = int(input("Enter Your Favorite movie year :"))
# Rating = input("Enter rating of your Favorite movie :")

# print( "Your Favorite movie is ",movie_name,"in",release_year," it was reasised you rated it",Rating,)


# 5.Write a program to convert temperature from Celsius to Fahrenheit.------------------------------------------

# cal = int(input("enter cal"))
# far = cal * (9 / 5)
# print(cal)
# print(far)

# 6.Take input from the user and check its data type using type().------------------------------------------

# var = input("Enter string  value")
# print(type(var))
# var1 = int(input("Enter any int value"))
# print(type(var1))
# var2 = float(input("Enter any floate"))
# print(type(var2))
# var3 = bool(input("Enter any bool"))
# print(type(var3))

# 7.Write a program that accepts two integers and prints their sum, difference, product, and quotient.------------------------------------------

# num1= int(input("Enter a number one for Sum "))
# num2= int(input("Enter a number second for Sum "))

# sum1 = num1 + num2 # or print = (num1 + num2)
# print(sum1)

# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)


# 8.Create a program that checks whether a given number is even or odd.------------------------------------------

# num1 = int(input("Enter the number to find reather its even or odd :"))

# even = (num1 % 2) 
# even2 = (even == 0)

# print("False means it's 'odd' number and true if the given number is 'even'")
# print("your output is :",even2)

# 9.Write a program that accepts a string and prints its length.------------------------------------------

# val = str(input("print any string i willprint length for you :"))

# print(len(val))


# 10.Store a boolean value (True/False) in a variable and use it in a decision (if condition).------------------------------------------

# value = bool(input("Enter only true or false :"))

# if value == True :
#     print("true")
# else :
#     print("false")

# 11.Write a program to check whether a string is a palindrome or not.------------------------------------------

# 12Convert a float number to an integer and print both values.------------------------------------------

# num1 = 7.4
# print("Num before casting =",num1, type (num1))
# type_casting = int(num1)

# print("Num after type casting",type_casting,type(type_casting))


# 13.Take a string input and display the first and last character.------------------------------------------

# input = input(" Enter string i will print first and last later of string for you :")

# print( input [0])
# print( input [-1])


# 14.Write a program that checks whether the entered number is positive, negative, or zero.------------------------------------------

# num = int(input("Enter a number i will check it is positive nagitive or zero :"))

# if num > 0 :
#     print("positive")
# elif num < 0 :
#     print("negitive")
# else:
#     print("its Zero")


# 15.Concatenate two strings and print the result with proper formatting.------------------------------------------

# str1 = input("Enter your name :")
# str2 = input("Enter your last name :")

# total = str1 + str2

# print("Your full name ",total)


# 16.Write a program that calculates the square and cube of a given number using exponent operator **.------------------------------------------

# num1 = int(input("Enter number calculates the square and cube of a given number :"))

# square = num1*2
# cube = num1**2

# print("Square is :", square)
# print("cube is ",cube)


# 17.Demonstrate the use of // (floor division) and % (modulus) operators.------------------------------------------

# num2 = int(input("Enter the value for calculating division and '%' operator :"))
# num1 = int(input("Enter the smaller value to calculate devisoin :"))

# div = num2 // num1 
# modulus = num2 % num1 

# print("Division", div)
# print("modulus", modulus)


# *18.Write a program that takes three numbers and prints the largest one using comparison operators.------------------------------------------

# print("Entre three number I will print largest one using comparison :")
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# num3 = int(input("Enter third number "))

# largest = 

#* 19.Use logical operators (and, or, not) in a program to check eligibility for voting (age ≥ 18 and citizenship = True).------------------------------------------

# age = int(input("Enter your age :"))
# c_Status = bool(input("Enter trur if you are citizen and false if you dont have it :"))

# if (age > 18 and c_Status == True):
#     print("you are eligibility")
# else:
#     print("You may try again lator ")

#20.Write a program to check if a number is divisible by both 3 and 5.------------------------------------------

# num = 7

# three = num % 3 == 0  and num % 5 == 0 

# print(three)
# print("True if it will be devidibal false means can't" ,three)


# 21.Show the difference between == and is operators with examples.------------------------------------------

# num = 10
# print(num) 
# between = num == 10 
# print("It will print true if condition matchis or will show false :", between)

# num2 = 20
# print(num2)
# between2 = num == 15 
# print("It will print true if condition matchis or will show false :", between2)

# 22.Write a program to calculate simple interest (SI = PRT/100).------------------------------------------

amount = int(input("Enter a total number of amount :"))
roi = int(input("Enter the rate or intrust :"))
time = int(input("Enter number of months :"))

sum = (amount * roi * time) / 100

print("Hear is the intrust :",sum)

# 23.Demonstrate assignment operators (+=, -=, *=, /=, etc.) on a variable.------------------------------------------

# 24.Write a program to calculate BMI (Body Mass Index).------------------------------------------
# 25.Create a program to find the remainder when one number is divided by another.------------------------------------------
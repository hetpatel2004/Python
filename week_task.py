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

# amount = int(input("Enter a total number of amount :"))
# roi = int(input("Enter the rate or intrust :"))
# time = int(input("Enter number of months :"))

# sum = (amount * roi * time) / 100

# print("Hear is the intrust :",sum)

# 23.Demonstrate assignment operators (+=, -=, *=, /=, etc.) on a variable.------------------------------------------

# num1 = int(input("Enter a number :"))
# num1 += 10 # (num1 -= 10) (num1 *= 10) (num1 /= 10) (num1 += 10)
# print(num1)


# 24.Write a program to calculate BMI (Body Mass Index).------------------------------------------

# weight =  int(input("Enter your weight :"))
# height =  float(input("Enter your hight :"))
# sum = weight / (height**2)

# print("Sum of Body mass index :",sum)

# 25.Create a program to find the remainder when one number is divided by another.------------------------------------------

# num1 = int(input("Enter the first number for devision :"))
# num2 = int(input("Enter the second number for devision :"))

# div = num1 * num2
# print("sum of devision :",div)
# remainder = num1 % num2
# print("sum of devision :",remainder)

# 26.Write a program to check if a given year is a leap year. ------------------------------------------

# year = int(input("Enter the year to check it,s leep year or not :"))

# if (year%400 ==0) or (year%4==0 and year%100!=0):
#     print("Leap year")
# else:
#     print("Not leap year.")    


# 27.Take marks of a student and display the grade (A, B, C, D, Fail).------------------------------------------

# marks = int(input("Enter marks i will print grade :"))

# if marks >= 90 and marks < 100 :
#     print("You scored A grade",marks)
# elif marks >= 80 and marks < 90 :
#     print("You scored B grade",marks)
# elif marks >= 70 and marks < 80 :
#     print("You scored C grade",marks)
# elif marks >= 60 and marks < 70 :
#     print("You scored D grade",marks)
# else:
#     print("Try Again Next time :",marks) 

# 28.Write a program to check if a character is a vowel or consonant. ------------------------------------------

# cha = input("Enetr any character i will check the given char is vovel or not :")
# if cha == "a" or cha== "e" or cha== "i" or cha=="o" or cha== "u":
#     print("character is vowel")
# else:
#     print("Its not a vovel")

# 29.Create a login system that asks for username and password. If correct, print "Login successful".------------------------------------------

# name = input("Enter courect User-name @ is compulsory :")
# pas = input("Enetr 8 digit password :")

# if (name != "@" and pas.__len__ == 8) :
#     print("incourect user name or password :")
# else :
#     print("login Successfull")


#*30.Write a program to classify a person’s age group (Child, Teen, Adult, Senior).------------------------------------------

# age = int(input("Enetr your age :"))
# if age > 0 and age <= 150:
#     if age > 0 and age <= 13 :
#         print("Child")
#     elif age > 13 and age <=18 :
#         print("Teen")
#     elif age > 18  and age <= 30 :
#         print("Adult")
#     else:
#         print("senior") 
# else:
#  print("valid age between 1 to 150")


#*31.Check if a number is prime.------------------------------------------

# num = int(input("Enter the number :"))
# num1 = num
# sum = (num % num1) 
# if sum == 0:
#     print("Yes ",sum," is prime number :")
# else :
#     print("no ",sum," is not a prime number")


# 32.Write a program to find the smallest of three numbers.------------------------------------------

# num1 = int(input("Enter one number :"))
# num2 = int(input("Enter second number :"))
# num3 = int(input("Enter third number :"))

# if num1 > num2 and num1 > num3:
#  print(num1,"is largest")
# elif num2 > num1 and num2 > num3:
#  print(num2, "is largest")
# # elif num3 > num2 and num3 > num1:
# else:
#  print(num3," is largest ")


# 33.Create a simple calculator using if-elif-else (add, subtract, multiply, divide).------------------------------------------
num1 = int(input("Enter number first for calculation"))
num2 = int(input("Enter number  second calculation"))
num3 = int(input("Enter number third for calculation"))



# 34.Take two numbers and check if the first is a multiple of the second.------------------------------------------
# 35.Write a program to check if a number is a perfect square.------------------------------------------
# 36.Create a discount calculator: if purchase > 1000 give 10% discount else no discount.------------------------------------------
# 37.Write a program to check whether a given character is uppercase, lowercase, digit, or special symbol.------------------------------------------
# 38.Ask the user to enter their exam marks and print "Pass" if ≥ 40 else "Fail".------------------------------------------
# 39.Write a program to check whether the entered password length is strong (≥8) or weak.------------------------------------------
# 40.Write a program that checks whether a number ends with digit 0.------------------------------------------
# 41.Print all even numbers from 1 to 50.
# 42.Print multiplication table of a number entered by the user.
# 43.Write a program to find the factorial of a number using a loop.
# 44.Print Fibonacci sequence up to n terms.
# 45.Print the sum of digits of a number.
# 46.Write a program to reverse a number using loops.
# 47.Write a program to count the number of vowels in a given string.
# 48.Print a pattern:# .4
# 49.Write a program to check whether a number is an Armstrong number.
# 50.Write a program to print all prime numbers between 1 and 100.

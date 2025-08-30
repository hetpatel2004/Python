# 1.Write a program to calculate the area of a rectangle using user input for length and width.------------------------------------------

# length = int(input("Enter length :"))
# width = int(input("Enter Width :"))

# rec = length * width 

# print("Area of Rectangle", rec)


# 2.Take input from the user and check its data type using type().------------------------------------------

# var = input("Enter string  value")
# print(type(var))
# var1 = int(input("Enter any int value"))
# print(type(var1))
# var2 = float(input("Enter any floate"))
# print(type(var2))
# var3 = bool(input("Enter any bool"))
# print(type(var3))



# 3.Write a program that accepts two integers and prints their sum, difference, product, and quotient.------------------------------------------

# num1= int(input("Enter a number one for Sum "))
# num2= int(input("Enter a number second for Sum "))

# # sum1 = num1 + num2  #or print = (num1 + num2)
# # print(sum1)

# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)


# 4.Take a string input and display the first and last character.------------------------------------------

# input = input(" Enter string i will print first and last later of string for you :")

# print( input [0])
# print( input [1])
# print( input [2])

# print( input [-1])


# 5.Use logical operators (and, or, not) in a program to check eligibility for voting (age ≥ 18 and citizenship = True).------------------------------------------

# age = int(input("Enter your age :"))
# c_Status = bool(input("Enter trur if you are citizen and false if you dont have it :"))

# if (age > 18 and c_Status == True):
#     print("you are eligibility")
# else:
#     print("You may try again lator ")


# 6.Write a program to calculate BMI (Body Mass Index).------------------------------------------

# weight =  int(input("Enter your weight :"))
# height =  float(input("Enter your hight :"))
# sum = weight / (height ** 2)
# print("Sum of Body mass index :",sum)


# 7.Write a program to calculate simple interest (SI = PRT/100).------------------------------------------

# amount = int(input("Enter a total number of amount :"))
# roi = int(input("Enter the rate or intrust :"))
# time = int(input("Enter number of months :"))

# sum = (amount * roi * time) / 100

# print("Hear is the intrust :",sum)


# 8.Create a simple calculator using if-elif-else (add, subtract, multiply, divide).------------------------------------------
# num1 = int(input("Enter number first for calculation :"))
# num2 = int(input("Enter number  second calculation :"))
# operation = input("Enter any one opration which you like to parform but from this given option ( + - * / ) :")

# if (operation != "+", operation != "-" , operation != "*" , operation != "/"):
#     if operation == "+":
#         print( num1 + num2)
#     elif operation == "-":
#         print( num1 - num2)
#     elif operation == "*":
#         print( num1 * num2)
#     elif operation == "/":
#         print( num1 / num2)
#     else :
#         print("sorry wrong operator")
# else:
#     print("unvalid oprator")


# 9.Print a pattern:
# for i in range (1,5):
#         print("*" * i)


# 10.Print all even numbers from 1 to 50.

# for i in range(1,50):
#     if i % 2 == 0:
#         print(i)
integer_num = 10           # int
float_num = 3.14           # float
string_text = "Hello"      # str
boolean_val = True         # bool
list_data = [1, 2, 3]      # list
tuple_data = (4, 5, 6)     # tuple
set_data = {7, 8, 9}       # set
dict_data = {"name": "Aastha", "age": 19}  # dict

print("Data Types Examples:")
print("Integer:", integer_num, "| Type:", type(integer_num))
print("Float:", float_num, "| Type:", type(float_num))
print("String:", string_text, "| Type:", type(string_text))
print("Boolean:", boolean_val, "| Type:", type(boolean_val))
print("List:", list_data, "| Type:", type(list_data))
print("Tuple:", tuple_data, "| Type:", type(tuple_data))
print("Set:", set_data, "| Type:", type(set_data))
print("Dictionary:", dict_data, "| Type:", type(dict_data))
print("\n-------------------------------------\n")

number = int(input("Enter a number: "))

if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")
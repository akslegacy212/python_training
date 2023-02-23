# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# i = "May the force be with you"
# i = i.split(" ")
# p = []
# for a in i:
#     p.append((a.capitalize()))
#
# list2 = " ".join(p)
# reverse_list = list2[::-1]
# print(reverse_list)

# i = "Hello World"
# print(i[::2])

# i = input("please enter your name")
# print (i)

'''calculator'''
# def add(x, y):
#     return  x+y
#
# def subtract(x, y):
#     return x-y
#
# def multiply(x, y):
#     return x*y
#
# def divide(x, y):
#     return x/y
#
# print("Select operation.")
# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
#
# while True:
#     choice = input("Enter input: ")
#
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue
#
#         if choice == '1':
#             print(add(num1, num2))
#
#         elif choice == '2':
#             print(subtract(num1, num2))
#
#         elif choice == '3':
#             print(multiply(num1, num2))
#
#         elif choice == '4':
#             print(divide(num1, num2))

'''calculator'''

# def add(a,b):
#     print(f"{a} + {b} = ",a + b)
#
# def sub(a,b):
#     print(f"{a} - {b} = ",a - b)
#
# def mul(a,b):
#     print(f"{a} * {b} = ",a * b)
#
# def div(a,b):
#     print(f"{a} / {b} = ",a/b)
#
# def ask():
#     a = int(input("Enter first number "))
#     b = int(input("Enter second number "))
#     return a,b
#
# s = int(input("select a maths operation :"
#           " 1 : addition "
#           "2 : subtraction "
#           "3 : Multiplication "
#           "4 : Division : "))
# if s == 1 :
#     c = ask()
#     add(c[0], c[1])
# elif s == 2 :
#     c = ask()
#     sub(c[0], c[1])
# elif s == 3 :
#     c = ask()
#     mul(c[0], c[1])
# elif s == 4 :
#     c = ask()
#     div(c[0], c[1])


'''area and circumference for circle '''

# import math
#
# def Circle(d):
#     print("Radius = ",d/2 )
#     print("Circumference = ", 2*math.pi*d/2)
#     print("Area = ", math.pi*pow(d/2,2))
#
# dia =  int(input("Enter diameter = "))
# Circle(dia)

'''factorial using loops'''
# num = int(input("Enter a number: "))
#
# factorial = 1
#
# if num < 0:
#    print("Sorry, please enter valid number")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)
#

# user_input = int(input("Enter a number to calculate factorial "))
#
#
# def calculate_factorial(num):
#     if num > 1:
#         return num * calculate_factorial(num - 1)
#     else:
#         return 1
# print(calculate_factorial(user_input))

'''handsome numbers'''

# number = int(input("Enter the handsome number:"))
#
# last_digit = number % 10
#
# left_part = number // 10
#
# print(left_part)
#
# left_part_sum = 0
# while left_part:
#     left_part_sum += left_part % 10
#     left_part = left_part // 10
#
#
# if left_part_sum == last_digit:
#     print('%d is Handsome Number.' %(number))
# else:
#     print('%d is Not Handsome Number.' %(number))

'''addition of first and last digit of the number'''
#
# number = int(input("Enter the handsome number:"))
#
# last_digit = number % 10
#
#
# def test1():
#     print('jejerjerj')
#
# def test2():
#     print('test2')


'''sum of ascii values of characters in string'''

# def ascii_calculator():
#     string_input = input('input the string: ')
#
#     for char in string_input


'''perfect numbers'''

# input_number = int(input("enter the value: "))
#
# Sum = 0
# for i in range(1, input_number):
#     if (input_number % i == 0):
#         Sum = Sum + i
#     if (Sum == input_number):
#         print(" %d is a Perfect Number" % input_number)
#     else:
#         print(" %d is not a Perfect Number" % input_number)


# import math
# def calc(*args):
#     print("Perimeter ", sum(args))
#     print("Area", math.prod(args))
#
#     p = math.sqrt(((args[0] * args[2])+(args[1] * args[3]))*((args[0] * args[3])+(args[1] * args[2])) / ((args[0] * args[1])+(args[2] * args[3])))
#     q = math.sqrt(((args[0] * args[2])+(args[1] * args[3]))*((args[0] * args[1])+(args[2] * args[3])) / ((args[0] * args[3])+(args[1] * args[2])))
#     return [p, q]
#
# diagonals = calc(1,2,3,4)
# print(f"daigonal is {round(diagonals[0], 2)}, {round(diagonals[1], 2)}")


# from math import sqrt
# def per_sqr(x):
#     if x >= 0:
#         sr = int(sqrt(x))
#         return (sr * sr) == x
#         return Falseprint(per_sqr(10))


# num = 12
# num2 = 22
#
# num2 += num
#
# print(num)
# print(num2)

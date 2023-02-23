'''lambda function'''

# def my_function(a):
#     print(a)
#
# my_function(12)


'''create a calculator uing lambda function'''
#
# operations = {
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
#     "/": lambda x, y: x / y,
#     "*": lambda x, y: x * y
# }
#
#
# def calculate(expr):
#     numxChars = ""
#     operation = None
#     numyChars = ""
#     for char in expr:
#         if char.isdigit():
#             if operation is None:
#                 numxChars += char
#             else:
#                 numyChars += char
#         elif char in operations:
#             operation = char
#         elif char.isspace:
#             pass
#         else:
#             raise Exception("invalid charecter: " + char)
#     return operations[operation](int(numxChars), int(numyChars))
#
#     print calculate(raw_input("Input? "))


# n, m = input("enter").split()
# def calc(a):
#     return a
#     print(calc(lambda n,m: n + m)(int(n),int(m)))
#     print(calc(lambda n,m: n * m)(int(n),int(m)))
#     print(calc(lambda n,m: n - m)(int(n),int(m)))
#     print(calc(lambda n,m: n / m)(int(n),int(m)))


# a = int(input("Enter number: "))
# b = int(input("Enter Number: "))
#
# def calculator(a):
#     print(a)
# calculator((lambda a, b : a + b)(a, b))
# calculator((lambda a, b : a - b)(a, b))
# calculator((lambda a, b : a / b)(a, b))
# calculator((lambda a, b : a * b)(a, b))


'''QR code '''
#
# import qrcode
#
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
#
# qr.add_data('May the force be with you!!')
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save('test.png')

# img = qrcode.make('May the force be with you!!')
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")


'''generate a qr code for users input'''
# import qrcode
#
# user_input = input("enter a value for QR: \n")
#
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
#
# qr.add_data(user_input)
#
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save('test2.png')


'''oop'''
#
# class TripToNepal:
#     budget = 5000
#     modeOfTransport = "Car"
#     friends_list = []
#
#     def eat_smoething_new(self, cost):
#         self.budget = self.budget - cost
#
#     def change_mode_of_transport(self, newMode):
#         self.modeOfTransport = newMode
#
#     def look_at_current_situation(self):
#         print("remaining amount", self.budget)
#
# trip = TripToNepal()
# trip.eat_smoething_new(100)
# trip.eat_smoething_new(500)
# trip.change_mode_of_transport("bike")
# trip.look_at_current_situation()

'''calculator in oop'''
#
# class calculator:
#     first_input = int(input("Enter the first value: \n"))
#     second_input = int(input("Enter the second value: \n"))
#
#     def addition(self):
#         print(self.first_input + self.second_input)
#
#     def subtraction(self):
#         print(self.first_input - self.second_input)
#
#     def division(self):
#         print(self.first_input / self.second_input)
#
#     def multiplication(self):
#         print(self.first_input * self.second_input)
#
# result = calculator()
#
# result.addition()
# result.subtraction()
# result.multiplication()
# result.division()


'''classes, constructor'''

# class SampleClass:
#     def __init__(self, name, branch):
#         self.name = name
#         self.branch = branch
#
#     def get_name(self):
#         print(self.name)
#
# s1 = SampleClass("Akash", "CSE")
# s1.get_name()


# class Student:
#     def __init__(self,Name,USN,Branch):
#         self.Name = Name
#         self.USN = USN
#         self.Branch = Branch
#
#     def updateBranch(self,input):
#         self.Branch=input
#
#     def display_info(self):
#         print("StudentName : ", self.Name)
#         print("USN : ", self.USN)
#         print("Branch : ",self.Branch)
#
#     std = [Student("anish","007","magic"),Student("sujal","002","magic"),Student("anita","003","magic")]
#     std[0].updateBranch("fire")
#     print(std[0].Branch)
#     inputt= input("enter: ")
#     for i in std:
#             if i.Name == inputt:
#                 i.display_info()


'''create a class shapes '''
# from math import pi
#
# class Shape:
#     def __init__(self, *args):
#         if(len(args)==1):
#             print("The radius of the circle is: ", args[0])
#             print("Area:", (pi * (args[0]**2)))
#             print("circumference: ", (2 * pi * args[0]))
#         if(len(args)==2):
#             print("The size of your quadrilateral are:", args[0], args[1])
#             print("Area:", (args[0]*args[1]))
#             print("Perimeter:", 2*(args[0] + args[1]))
#
# circle = Shape(10)
# rect = Shape(10, 20)
#



'''api creation'''

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
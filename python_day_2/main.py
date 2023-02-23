#
# sample_string = "hey!! how are you?"
#
# print (sample_string.title())

'''1. input from user and calculate the index of the first and last number
'''
# number = input("Enter number:")
# sum = int(number[0]) + int(number[-1])
# print("The sum of digit = " + str(sum))


'''string operations'''

# i = "hey!! how are you?"
#
# print(i[1])
#
# print(i[4])
#
# print(i[1:3])
#
# print(i[3:8])

'''list operations'''




'''slice this strings to get o/p Harry Pan'''

# s1 = "HarryPotter"
# s2 = "PeterPan"
#
# j = s1[0:5] + s2[5:8]
#
# k = s1[5:11] + s2[0:5]
#
# print(j)
# print(k)



'''take a string input and even position is Capital case and odd position lower case'''


# inp = input('enter statement:\n ');
#
# temp_str = ""
#
# for i in range (len(inp)):
#     if i % 2 == 0:
#         temp_str = temp_str + inp[i].upper()
#     else:
#         temp_str = temp_str + inp[i].lower()
#
# print(temp_str)

'''count number of the vowels '''

# inp = input('enter string:\n ');
#
# count = 0
#
# i = 0
#
# for i in range(len(inp)):
#     if (
#         (inp[i] == "a")
#         or (inp[i] == "e")
#         or (inp[i] == "i")
#         or (inp[i] == "o")
#         or (inp[i] == "u")
#     ):
#         count += 1
#
# print("Number of vowels in the given string is: ", count)

#
# inp = input('enter string:\n ');
#
# inp = inp.lower()
#
# total = 0
#
# total += inp.count('a')
# total += inp.count('e')
# total += inp.count('i')
# total += inp.count('o')
# total += inp.count('u')
#
# print(total)


'''code to find out triangular number'''

# num = int(input("please enter the number: \n"))
#
# sum = 0
#
# for i in range(num):
#     sum += i
#
#     if sum == num:
#         print("is a triangular number")
#     else:
#         print("is not a triangular number")

# def is_triangular(n):
#     if n == 0 or n == 1:
#         return True
#
#     triangular_sum = 0
#
#     for i in range(n):
#         triangular_sum += i
#
#         if triangular_sum == n:
#             return True
#
#         if i == n:
#             return False
#
#
# # Reading number
# number = int(input('Enter number: '))
#
# # Making decision
# if is_triangular(number):
#     print('%d is TRIANGULAR.' % (number))
# else:
#     print('%d is NOT TRIANGULAR.' % (number))

'''pattern triangle'''

# n = int(input("Enter number: "))
#
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print((j+1)%2, end="")
#     print()


'''create a list which contains dictionaries and search a some word from dict if locates print the dict'''

dicts = [
{
    "name": "Akash Ghadge",
    "location": "Pune",
},
{
    "name": "Nikhil Batheja",
    "location": "Kolhapur",
},
{
    "name": "Aditya Shinde",
    "location": "Vita",
}
]


i =(input("Please eneter text: "))
listup=[]
for x in dicts:
    for z in x:
        if i.lower() in x[z].lower():
            listup.append(x)
print(listup)
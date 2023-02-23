'''list comprehension'''
import json

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)

'''filter out friends from nepal, filter out friends from india, filter out friends whose USN contains 1, 3s and multiple 3s,   filter out friends whose name contain ee '''
#
# student_1 = {
#     "name": "Cezane",
#     "USN":"006644",
#     "locaion": "Nepal"
# }
#
# student_2 = {
#     "name": "Junee",
#     "USN":"113322",
#     "locaion": "Nepal"
# }
#
# student_3 = {
#     "name": "Anish",
#     "USN": "1133222",
#     "locaion": "Nepal"
# }
#
# student_4 = {
#     "name": "Nisht",
#     "USN": "1133222",
#     "locaion": "India"
# }
#
# friend_list = [student_1, student_2, student_3, student_4]
#
# friend_nepal = [x for x in friend_list if x["locaion"] == "Nepal"]
# print(friend_nepal)
# friend_india =[x for x in friend_list if x["locaion"] == "India"]
# print(friend_india)
# list_three = [x for x in friend_list if "3" in x["USN"]]
# print(list_three)
# my_list = [x for x in friend_list if "ee" in x["name"]]
# print(my_list)


'''api'''

# import requests
#
# url = "https://jsonplaceholder.typicode.com/todos/1"
#
# resp = requests.get(url)
#
# print (resp.json())

'''use this url to filter out list from the url where words in title is less than or equal to 8 '''

# import requests
#
# url = "https://jsonplaceholder.typicode.com/posts"
#
# resp = requests.get(url)
#
# print (len(resp.json()))
#
# for data in resp.json():
#     if len(data.get("title").split()) <= 8:
#         print(data)


'''create a list of emails from url'''

# import requests
#
# url = 'https://jsonplaceholder.typicode.com/comments'
#
# resp = requests.get(url)
#
# lst = []
# for i in resp.json():
#     lst.append(i["email"])
# print(len(lst))


'''POST request'''

# import requests
#
# req_url = "https://jsonplaceholder.typicode.com/comments/posts"
#
# sample_entry = {
#     "title": "Voldemort",
#     "body": "bar",
#     "UserId": 1
# }
#
# string_sample_entry = json.dumps(sample_entry)
#
# response = requests.post(url=req_url, data=string_sample_entry, headers={
#     'content-type': 'application/json ; charset=UTF-8'
# })
#
# print(response)
# print(response.json())

#
# import requests
# res_url = "https://jsonplaceholder.typicode.com/posts"
# sample_entry ={    "title":'voldormort',    "body": 'bar',    "userId": 1}
# string_sample = json.dumps(sample_entry)
# res = requests.post(url=res_url, data=string_sample , headers={    'content-type': 'application/json ; charset=UTF-8'})
# print(res)
# print(res.json())

'''get a data from api'''

# import requests
#
# baseUrl = "https://api.publicapis.org/random"
# response = requests.get(baseUrl)
# fiveDict = []
# for i in range(0,5):
#     fiveDict.append(requests.get(baseUrl).json())
#     print(fiveDict)
#
#


'''dynamic input in url'''

import requests
# import json
#
# request_url = "https://jsonplaceholder.typicode.com/todos/1"
# user_input = input("please enter the postId:\n")
#
# print(user_input)



request_url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url=request_url,params={    "postId": input(""),})
va = (response.json())
print(va)
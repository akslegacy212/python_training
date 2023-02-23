import pandas as pd
import numpy as np

# temp = pd.read_csv('house_price.csv')
#
# print(temp.head(5))
#
# my_data_frame = pd.DataFrame(temp)
# print(my_data_frame.head(5))

'''create a pandas dataframe from multiple lists'''

# names = ['Harry', 'Ron', 'Tom', 'Dobby']
#
# ages = [23, 24, 57, 66]
#
# locations = ['London', 'Pune', 'Delhi', 'kolhapur']
#
# zipped_list = list(zip(names, ages, locations))
#
# df = pd.DataFrame(zipped_list, columns=['Name', 'Ages', 'Location'])

# print(df)



# Creating a 2 dimensional numpy array
# data = np.array([[5.8, 2.8], [6.0, 2.2]])
# print(data)
#
# # Creating pandas dataframe from numpy array
# dataset = pd.DataFrame({'Column1': data[:, 0], 'Column2': data[:, 1]})
# print(dataset)

'''print entire column with indexing'''
# temp = pd.read_csv('house_price.csv')
#
# print(temp.iloc[0:,2])


'''print name, hostname and availibility'''

# temp = pd.read_csv('house_price.csv')
# print(temp.loc[10:100,["name","host_name","availability_365"]])

''''''
house_price = pd.read_csv('house_price.csv')

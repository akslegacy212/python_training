# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd

iris_db = pd.read_csv('IRIS.csv')
iris_db

iris_db.info

iris_db.shape

my_df = pd.DataFrame([[10,20,30,40, "Avatar"]])
my_df

my_df_1 = pd.DataFrame([[10, 20, 30, 40, "Avatar World"]], columns=["sepal_length", "sepal_width","petal_length", "petal_width", "species"])
my_df_1

iris_db=iris_db.append(my_df_1, ignore_index=True)

iris_db.sort_index(inplace=True)

iris_db.tail()

iris_db['sepal_length'].sum()

iris_db[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']].sum()



sum_sepal_length = iris_db["sepal_length"].sum()
sum_sepal_width = iris_db["sepal_width"].sum()
sum_petal_length = iris_db["petal_length"].sum()
sum_petal_width = iris_db["petal_width"].sum()

my_df = pd.DataFrame([[sum_sepal_length, sum_sepal_width, sum_petal_length, sum_petal_width, "Avatar World"]], columns=["sepal_length", "sepal_width","petal_length", "petal_width", "species"])
iris_db.append(my_df)

iris_db.nunique()

iris_db['sepal_length'].unique()

iris_db_1 = iris_db.drop(axis=1, columns=['species'])
iris_db_1

iris_db_2 = iris_db_1
iris_db_2

iris_db_divide = iris_db_1 / iris_db_2
iris_db_divide

iris_db_divide.join(iris_db['species'])




# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import numpy as np

mock_data = pd.read_csv('MOCK_DATA.csv')

mock_data.head()

mock_data["usn"][mock_data["usn"] % 2 ==0]=np.NAN

mock_data.head()

drug_data = pd.read_csv('drug.csv')

drug_data.head()

drug_data_brazil = drug_data[drug_data["Country"]=="Brazil"]

drug_data_brazil.drop("Country",axis=1,inplace=True)

drug_data_brazil.reset_index(drop=True,inplace=True)

drug_data_brazil

drug_data_india = drug_data[drug_data["Country"]=="India"]

drug_data_india.drop("Country",axis=1,inplace=True)

drug_data_india.reset_index(drop=True,inplace=True)

drug_data_india

drug_data_nepal = drug_data[drug_data["Country"]=="Nepal"]

drug_data_nepal.drop("Country",axis=1,inplace=True)

drug_data_nepal.reset_index(drop=True,inplace=True)

drug_data_nepal

country_data = drug_data.groupby(["Country","Drug Name"],group_keys=True)

country_data.first()

unique_countries = drug_data["Country"].unique()
unique_countries

df_list = []
for x, i in enumerate(unique_countries):
    state = drug_data[drug_data["Country"]==i]
    df_list.append((state))
df_list[1]

drug_data_country = drug_data.groupby(['Country', 'Drug Name'])['Average Consumption '].max()

mock_data = mock_data.reset_index()

mock_data[mock_data['Average Consumption '] == mock_data['Average Consumption '].max()]

drug_list = []countries = (drug_df["Country"].unique())max_list = []


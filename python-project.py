# import numpy as np
import pandas as pd
import os

def read_csv_file(filename):
    current_directory = os.getcwd()
    dataframe = pd.read_csv(os.path.join(current_directory,filename+".csv"))
    return dataframe

# print(restaurants_df.head(10))
# print(restaurants_df.tail())
# print(restaurants_df.info())
# print(restaurants_df.shape)
# print(restaurants_df.describe())

# print(restaurants_menu_df.head(10))
# print(restaurants_menu_df.tail())
# print(restaurants_menu_df.info())
# print(restaurants_menu_df.shape)
# print(restaurants_menu_df.describe())


if __name__ == "__main__":
    filename = input("Enter File Name: ")
    df = read_csv_file(filename)
    # print(df.head(10))
    # print(df.tail())
    # print(df.info())
    # print(df.shape)
    print(df.describe())
    
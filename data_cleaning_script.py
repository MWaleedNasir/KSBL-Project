import pandas as pd
import numpy as np
from collections import defaultdict
import re

def data_cleaning_file (file_name1, file_name2):
    """ 
    ***DATA CLEANING OF RESTAURANTS-MENUS.CSV*** 
    Author: Fatima Dossani

    """
    # Loading the csv file
    # restaurant_menu_data = pd.read_csv('restaurant-menus.csv')
    restaurant_menu_data = file_name2 


    # Renaming columns of datasets
    restaurant_menu_data.rename(columns = {
            "category": "sub_category", 
            "name": "item_name"
            }, 
        inplace=True
    )

    # Explaing Datasets Properties
    # print("Columns of Dataset: ",restaurant_menu_data.columns)
    # print("Describe Dataset: ",restaurant_menu_data.describe())
    # print("Shape of Dataset: ",restaurant_menu_data.shape)
    # print("Datatypes of Dataset: ",restaurant_menu_data.dtypes)

    # print("---------------XXXXXXXXXXXXXX---------------XXXXXXXXXXXXXX---------------")

    # Define the clean_strings function to remove trailing ™ and ® characters

    def clean_strings(string):
        return string.rstrip("™®")

    def clean_menus_data(menus):
        # Remove any special characters from the menu item names
        restaurant_menu_data['item_name'] = restaurant_menu_data['item_name'].str.replace('[^A-Za-z0-9\s]+', '', regex=True)

        # Remove any trailing spaces from the menu item names
        restaurant_menu_data['item_name'] = restaurant_menu_data['item_name'].str.strip()

        # Replace '&amp;' with 'and'
        restaurant_menu_data['item_name'] = restaurant_menu_data['item_name'].str.replace('amp', 'and')

        return restaurant_menu_data

    restaurant_menu_data = clean_menus_data(restaurant_menu_data)
    restaurant_menu_data['sub_category'] = restaurant_menu_data['sub_category'].apply(clean_strings)


    restaurant_menu_data.drop(['description'], axis = 1, inplace=True)
    restaurant_menu_data['price'] = restaurant_menu_data['price'].apply(lambda x: '$' + x.split(' ')[0])

    return restaurants_data, restaurant_menu_data
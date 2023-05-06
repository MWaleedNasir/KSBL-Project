import pandas as pd
import numpy as np
from collections import defaultdict
import re

def data_cleaning_file (file_name1, file_name2):
    """ 
    ***DATA CLEANING OF RESTAURANTS.CSV*** 
    Author: Rabbiyah Sulman
    """
    
    # Loading the csv file
    # restaurants_data = pd.read_csv('restaurants.csv')

    restaurants_data = file_name1 

    # Since pandas displays a limited number of rows, we are setting this to 500 rows so that we can explore the dataset
    pd.set_option('display.max_rows', 300)

    # Renaming columns of datasets
    restaurants_data.rename(columns = {
            "id": "restaurant_id", 
            "position": "restaurant_position_in_search_result", 
            "name": "restaurant_name", 
            "category": "super_category", 
            "lng": "long"
            }, 
        inplace=True
    )

    # Explaing Datasets Properties
    # print("Columns of Dataset: ",restaurants_data.columns)
    # print("Describe Dataset: ",restaurants_data.describe())
    # print("Shape of Dataset: ",restaurants_data.shape)
    # print("Datatypes of Dataset: ",restaurants_data.dtypes)

    # print("---------------XXXXXXXXXXXXXX---------------XXXXXXXXXXXXXX---------------")

    """Cleaning of Restaurants Name & Spliting Address Into Seperate Column"""

    def clean_restaurant_name(data):
        # Remove parentheses and their contents using regular expressions
        data['restaurant_name'] = data['restaurant_name'].str.replace(r'\([^)]*\)', '')
        # Remove any special characters that are not letters or spaces using regular expressions
        data['restaurant_name'] = data['restaurant_name'].str.replace('[^a-zA-Z\s]+', '')
        # Replace '&amp;' with 'and'
        data['restaurant_name'] = data['restaurant_name'].str.replace('Amp', 'and')
        # Remove multiple spaces and replace with a single space using regular expressions
        data['restaurant_name'] = data['restaurant_name'].str.replace('\s+', ' ')
        # Strip any unwanted spaces from the beginning or end of the string using the strip method
        data['restaurant_name'] = data['restaurant_name'].str.strip()
        # Convert all letters to lowercase
        data['restaurant_name'] = data['restaurant_name'].str.lower()
        # Capitalize the first letter of each word using the title method
        data['restaurant_name'] = data['restaurant_name'].str.title()
        return data

    def count_restaurant_names(df):
        counts = df['restaurant_name'].value_counts()
        return pd.Series(counts.values, index=counts.index)

    def split_address(address):
        # split the address into block, street, city, state, and zip code using regex
        pattern = r'(\d+)\s+(.*?)\s*,\s*(.*?)\s*,\s*([A-Z]{2})\s*,\s*(\d+)'
        match = re.match(pattern, str(address))
        if match:
            block = match.group(1)
            street = match.group(2)
            city = match.group(3)
            state = match.group(4)
            zip_code = match.group(5)
        else:
            block = ''
            street = ''
            city = ''
            state = ''
            zip_code = ''
        
        return block, street, city, state, zip_code

    restaurants_data = clean_restaurant_name(restaurants_data)
    name_counts = count_restaurant_names(restaurants_data)

    #Add count of restaurants as a column
    restaurants_data['number_of_restaurants'] = restaurants_data['restaurant_name'].map(name_counts)

    # apply the split_address function to the 'full_address' column
    restaurants_data[['block', 'street', 'city', 'state', 'zip_code']] = restaurants_data['full_address'].apply(lambda x: pd.Series(split_address(x)))

    # print(restaurants_data.info())

    # restaurant_counts = restaurants_data.loc[:, ['restaurant_name', 'number_of_restaurants']].sort_values(by='number_of_restaurants', ascending=False)
    # print(restaurant_counts)

    # Dropping the column 'zip_code' column because we will be extracting zip_code from the full_address column Also dropping full_address, lat, long, block since no use of these columns
    restaurants_data.drop(['full_address','zip_code','lat', 'long', 'block', 'zip_code'], axis=1, inplace = True)

    # Dropping rows with Null Values in super category column
    restaurants_data.dropna(subset=['super_category'], inplace=True, how='any', axis=0)

    # print(restaurants_data.info())

    # print("---------------XXXXXXXXXXXXXX---------------XXXXXXXXXXXXXX---------------")

    """Cleaning of Score & Ratings Column"""
    # Checking for null values
    # print(restaurants_data.isnull().sum())

    # Fetch Unique Values from Score Column
    # print(restaurants_data['score'].unique())
    # print(restaurants_data['ratings'].unique())

    # Fetch Value Counts of each score
    # print(restaurants_data['score'].value_counts())
    # print(restaurants_data['ratings'].value_counts())

    # Fetch mean value of following columns
    # print(restaurants_data['score'].mean())
    # print(restaurants_data['ratings'].mean())

    # Fetch mode value of following columns
    # print(restaurants_data['score'].mode())
    # print(restaurants_data['ratings'].mode())

    # Filling null values with mean values in dataset 
    restaurants_data['score'].fillna(restaurants_data['score'].mean(), inplace=True)
    restaurants_data['ratings'].fillna(restaurants_data['ratings'].mean(), inplace=True)

    # Checking for null values again
    # print(restaurants_data.isnull().sum())

    # Using the round function to round the values in 'score' and 'ratings' columns to 2 decimal places
    restaurants_data['score'] = restaurants_data['score'].round(2)
    restaurants_data['ratings'] = restaurants_data['ratings'].round(2)

    # print("---------------XXXXXXXXXXXXXX---------------XXXXXXXXXXXXXX---------------")

    """Cleaning Price Range Column"""
    # print(restaurants_data['price_range'].unique())
    # print(restaurants_data['price_range'].value_counts())

    # Replacing the values for the price_range column
    restaurants_data['price_range'].replace({
        '$': 'Cheap', 
        '$$': 'Slighty Expensive', 
        '$$$': 'Expensive', 
        '$$$$': 'Very Expensive'
        }, inplace=True
    )

    # Fetch mode value of price range column
    # print(restaurants_data['price_range'].mode())

    # Filling null values with mode values in dataset 
    restaurants_data['price_range'].fillna(restaurants_data['price_range'].mode()[0], inplace=True)

    # print(restaurants_data.isnull().sum())

    # restaurants_data.replace(['', ' '], np.nan, inplace=True)
    # restaurants_data.dropna(subset=['restaurant_name','street', 'city', 'state'], inplace=True, how='all', axis=0)

    # Group the data by state and count the number of unique cities in each state
    state_city_counts = restaurants_data.groupby('state')['city'].nunique()

    # Create a new column 'Outlet Type' to indicate whether a restaurant is a chain outlet or a single outlet
    restaurants_data['outlet_type'] = restaurants_data.apply(lambda x: 'Chain Outlet' if state_city_counts[x['state']] > 1 else 'Single Outlet', axis=1)

    # Soring Values By Number Of Restaurants
    restaurants_data.sort_values(by = 'number_of_restaurants', ascending = False).head()

    # Checking for null values again
    # print(restaurants_data.columns)


    # print("---------------XXXXXXXXXXXXXX---------------XXXXXXXXXXXXXX---------------")
    # print("**************************************************************************")


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
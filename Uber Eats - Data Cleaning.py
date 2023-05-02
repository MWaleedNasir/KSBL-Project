#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the main libraries
import pandas as pd
import numpy as np


# In[2]:


# Loading the first csv file
main_data = pd.read_csv('restaurants.csv')
# Since pandas displays a limited number of rows, we are setting this to 500 rows so that we can explore the dataset
pd.set_option('display.max_rows', 300)


# In[3]:


# Fetching the first five rows
main_data.head()


# In[4]:


# Renaming the columns here which will help us to understand the data 
main_data.rename(columns={"id": "restaurant_id", "position": "restaurant_position_in_search_result", "name": "restaurant_name", "category": "super_category", "lng": "long"}, inplace=True)


# In[5]:


# Printing the output to check the new headers
main_data.head()


# ### Exploring the Dataset:

# In[6]:


main_data.info()


# In[7]:


main_data.describe()


# In[8]:


main_data.columns


# In[9]:


main_data.shape


# In[10]:


main_data.dtypes


# In[11]:


# Checking for null values
main_data.isnull().sum()


# ### Basic Insights:

# 1. There are missing values in the score, ratings, super_category, price_range, full_address, and zip code columns. We will probably be using the mean/mode value to fill the score and ratings column. However, we can drop the 23 rows where the super_category is not mentioned since it will not have a big impact on the data. Whereas for the full_address column, the only insight we can extract from here is the state and the city which would be helpful to have a holistic picture of the data segmenting it on the restaurant_name. Hence, for the missing values we can also drop these rows since they won't have sufficient damage on the dataset. 
# 
# 2. For the total number of restaurants, we can extract this information by checking the duplicates for restaurant_id, clean the data for the restaurant_name and check the value_counts. If there are multiple rows for the same restaurant_name, we can check for the state and city and distribute the data by creating a new column to check if a restaurant has multiple branches or not. 
# 
# 3. For the price_range column, we need to fix the values first and then use it to compare with the restaurants score and rating. From this, we can find the top and bottom restaurants. 
# 
# 4. The category column needs a lot of fixing. We need to clean the column and then convert it into a list to check the most famous categories on the basis of the restaurant name and score.

# #### Fixing the NULL values:

# In[12]:


main_data['score'].unique()


# In[13]:


main_data['score'].value_counts()


# In[14]:


main_data['score'].mean()


# In[15]:


main_data['score'].mode()


# In[16]:


main_data['score'].fillna(main_data['score'].mean(), inplace=True)


# In[17]:


main_data['score'].isnull().sum()


# In[18]:


main_data['ratings'].unique()


# In[19]:


main_data['ratings'].value_counts(ascending = False)


# In[20]:


main_data['ratings'].mean()


# In[21]:


main_data['ratings'].mode()


# In[22]:


main_data['ratings'].fillna(main_data['ratings'].mean(), inplace=True)


# In[23]:


main_data['ratings'].isnull().sum()


# In[24]:


main_data.dropna(subset=['super_category', 'full_address', 'zip_code'], inplace=True, how='any', axis=0)


# In[25]:


main_data.isnull().sum()


# In[26]:


# Using the round function to round the values in 'score' and 'ratings' columns to 2 decimal places
main_data['score'] = main_data['score'].round(2)
main_data['ratings'] = main_data['ratings'].round(2)


# In[27]:


main_data['price_range'].unique()


# In[28]:


main_data['price_range'].value_counts()


# In[29]:


# Replacing the values for the price_range column
main_data['price_range'].replace({'$': 'Cheap', '$$': 'Slighty Expensive', '$$$': 'Expensive', '$$$$': 'Very Expensive'}, inplace=True)


# In[30]:


main_data['price_range'].value_counts()


# In[31]:


main_data['price_range'].mode()


# In[32]:


main_data['price_range'].fillna(main_data['price_range'].mode()[0], inplace=True)


# In[33]:


main_data['price_range'].isnull().sum()


# In[34]:


# Checking the null values for all columns now
main_data.isnull().sum()


# #### Cleaning the restaurant_name column:

# In[35]:


main_data['restaurant_name']


# In[36]:


main_data['restaurant_name'].unique()


# In[37]:


main_data['restaurant_name'].value_counts()


# In[40]:


# Define the function to clean the restaurant name column
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

# Apply the function to the restaurant name column of the main_data dataframe
main_data = clean_restaurant_name(main_data)
print(main_data['restaurant_name'])


# In[41]:


main_data['restaurant_name'].head(50)


# #### Checking the count of restaurants:

# In[42]:


from collections import defaultdict

def count_restaurant_names(df):
    counts = defaultdict(int)
    for name in df['restaurant_name']:
        counts[name] += 1
    return counts

name_counts = count_restaurant_names(main_data)
for name, count in name_counts.items():
    if count > 1:
        print(f"{name}: {count} restaurants")


# In[43]:


def count_restaurant_names(df):
    counts = df['restaurant_name'].value_counts()
    return pd.Series(counts.values, index=counts.index)

name_counts = count_restaurant_names(main_data)
main_data['number_of_restaurants'] = main_data['restaurant_name'].map(name_counts)


# In[44]:


restaurant_counts = main_data.loc[:, ['restaurant_name', 'number_of_restaurants']].sort_values(by='number_of_restaurants', ascending=False)
print(restaurant_counts)


# In[45]:


main_data.head()


# In[46]:


# Dropping the column 'zip_code' column because we will be extracting zip_code from the full_address column
main_data.drop(['zip_code'], axis=1, inplace = True)


# #### Splitting the full_address column into block, street, city, state, and zip_code:

# In[47]:


main_data['full_address']


# In[48]:


import re

def split_address(address):
    # split the address into block, street, city, state, and zip code using regex
    pattern = r'(\d+)\s+(.*?)\s*,\s*(.*?)\s*,\s*([A-Z]{2})\s*,\s*(\d+)'
    match = re.match(pattern, address)
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

# apply the split_address function to the 'full_address' column
main_data[['block', 'street', 'city', 'state', 'zip_code']] = main_data['full_address'].apply(lambda x: pd.Series(split_address(x)))

# drop the original 'full_address' column
main_data.drop(['full_address'], axis=1, inplace=True)


# In[49]:


# Dropping the unnecessary columns
main_data.drop(['lat', 'long', 'block', 'zip_code'], axis=1, inplace = True)


# In[50]:


main_data.head()


# In[51]:


main_data['street'].unique()


# In[52]:


main_data['street'].value_counts()


# In[53]:


main_data.replace(['', ' '], np.nan, inplace=True)


# In[54]:


main_data.isnull().sum()


# In[55]:


# drop the columns with empty strings
main_data.dropna(subset=['street', 'city', 'state'], inplace=True, how='all', axis=0)


# In[56]:


main_data.isnull().sum()


# In[57]:


main_data[main_data['restaurant_name'].isnull()]


# In[58]:


main_data.head()


# In[59]:


main_data.dropna(subset=['restaurant_name'], inplace=True)


# In[60]:


main_data.isnull().sum()


# In[61]:


main_data.shape


# #### Checking what insights we can derive from the city column:

# In[62]:


main_data['city'].unique()


# In[63]:


main_data['city'].value_counts().head(10)


# #### Checking if a restaurant has multiple branches in a city:

# In[64]:


main_data[['restaurant_name', 'state', 'city', 'number_of_restaurants']].sort_values(by = 'number_of_restaurants', ascending = False)


# In[70]:


# Count the number of restaurants in each state
main_data['state'].value_counts()


# In[71]:


# Group the data by state and count the number of unique cities in each state
state_city_counts = main_data.groupby('state')['city'].nunique()

# Create a new column 'Outlet Type' to indicate whether a restaurant is a chain outlet or a single outlet
main_data['outlet_type'] = main_data.apply(lambda x: 'Chain Outlet' if state_city_counts[x['state']] > 1 else 'Single Outlet', axis=1)


# In[73]:


main_data.sort_values(by = 'number_of_restaurants', ascending = False).head()


# In[74]:


main_data['outlet_type'].unique()


# In[75]:


main_data['outlet_type'].value_counts()


# The code here isn't identfying the chain outlets properly. Will be picking this up tomorrow. 

# In[ ]:





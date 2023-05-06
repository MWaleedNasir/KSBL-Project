# KSBL PROJECT - UBER EATS ANALYSIS

This project has been selected in order to analyze how the restaurant industry in the US works and to gauge how different restaurants and chains have performed in different states in terms of ratings and their respective pricings.

## DATA SETS

- We have two datasets one is related to the details and data from the restaurants and the other is data 
that is specific to the menu of the restaurants and its details.

## DATA CLEANING
Data cleaning has been done in two phases in two different files:

1. #### Restaurants:



2. #### Restaurants Menu:

- At first we have renamed the necessary columns so that there is no duplication and things make sense  when we merge the two files.
- We then removed all the additional or irrelevant characters from the data so that we can perform calculations and there is no confusion. 
- We also removed all the trailing spaces in between the data
- Next we ensured that '&' is replaced with 'and'
- We then dropped the description column as it was irrelevant for our insights and calculations
- Finally in the price column we ensured the proper format of the pricing so that there is no confusion/error in the calculations.

## DATA MERGING

- The merging part has been automated with functions such that it can be used on different files. On running the code the system asks for either giving the list or exiting. If we input list the system gives us the file that are available and when we choose both the files it loads, merges, cleans and then saves all the files. If we input '0' the code ends with a 'Goodbye' response. 

## DATA ANALYSIS AND VISUALIZATION

- For the analysis part after cleaning and merging the two datasets we have analyzed the dataset on three KPIs: Price range, number of outlets and Cities.

![Top 10 restaurant Chains in US by price range] (https://github.com/MWaleedNasir/KSBL-Project/Data Visualization 1.jpg?raw=true)

![Top 10 restaurant Chains in US by # of outlets](https://github.com/MWaleedNasir/KSBL-Project/Data Visualization 2.jpg?raw=true)

![Top 10 restaurant Chains in US by Cities](https://github.com/MWaleedNasir/KSBL-Project/Data Visualization 3.jpg?raw=true)
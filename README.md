# KSBL PROJECT - UBER EATS ANALYSIS

This project has been selected in order to analyze how the restaurant industry in the US works and to gauge how different restaurants and chains have performed in different states in terms of ratings and their respective pricings.

## DATA SETS

- We have two datasets one is related to the details and data from the restaurants and the other is data 
that is specific to the menu of the restaurants and its details.

## DATA CLEANING
Data cleaning has been done in two phases in two different files:

1. #### Restaurants:

- We have renamed several columns so that they make sense and we can easily merge both the files without any confusion. Example category to super category since both files have columns name categories and have different data.
- The next step is related to how we figured out that there are null values in the dataset and their locations and then we removed those null values so that there is no discrepancy in the dataset and can be used easily for doing calculations and analysis.
- Performed extensive data cleaning on the restuarant_name and full_address for irrelevant characters and discrepancies.
- Created two new columns number_of_new_restaurants and outlet_type which can be used in doing analysis for different KPIs and insights.

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

- For the analysis part after cleaning and merging the two datasets we have analyzed the dataset on three KPIs: 


1. Price Range is Cheap and top 10 are based on count of Outlets
![Top 10 restaurant Chains in US by price range Cheap](https://github.com/MWaleedNasir/KSBL-Project/blob/main/Data_Visualization_1.png)

2. Top restaurants based on number of Outlets in the US
![Top 10 restaurant Chains in US by # of outlets](https://github.com/MWaleedNasir/KSBL-Project/blob/main/Data_Visualization_2.png)

3. Top restaurants in the cities of US based on count of Outlets
![Top 10 restaurant Chains in US by Cities](https://github.com/MWaleedNasir/KSBL-Project/blob/main/Data_Visualization_3.png)

- Through the analysis and the charts above you can see that the Ice Cream Shop is the largest chain in the cheap category of price range. Similarly, the Ice Cream shop has the greatest number of outlets (total of 161) in US in all the cities. Finally, we also found out that Washington has the greatest number of restaurant chains in the US and it is the biggest market for anyone who wants to open anywhere in the US.  
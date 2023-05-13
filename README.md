# UBER EATS ANALYSIS

This project has been selected in order to analyze 
- How the restaurant, that are patnered with UBER Eats, in the US works. 
- To gauge how these restaurants and chains have performed in different states in terms of ratings and their respective pricings.

Download CSV Files: https://www.kaggle.com/code/rajkumarpandey02/uber-eats-usa-data-analysis

## HOW TO RUN SCRIPT
Following are the steps to run scripts:
- Download the above gitub repository & extract files in a folder.
- Extract csv files from zip and place it in same folder where main.py belongs.
- Open any Python IDE with latest version python i.e 3x and open the downloaded repo folder along with CSV.
- Two separate scripts are in place: 
1. data_cleaning_script.py - Used for data cleaning of the respective CSV files.
2. main.py - Python script file where main part of the code is being executed.   
- Open Terminal Or Console in that IDE and run "main.py" & follow the commands of the script.

## DATA SETS

We have two datasets 
- Restaurants.csv - Details and data from the restaurants 
- Restaurant-menus.csv - Specific to the menu of the restaurants and its details

## DATA CLEANING
Data cleaning has been done in two phases in two different files:

1. #### Restaurants.csv:

- We have renamed several columns so that they make sense and we can easily merge both the files without any confusion. 
Example category to super category since both files have columns name categories and have different data.
- The next step is related to how we figured out that there are null values in the dataset and their locations and then we removed those null values so that there is no discrepancy in the dataset and can be used easily for doing calculations and analysis.
- Performed extensive data cleaning on the restuarant_name and full_address for irrelevant characters and discrepancies.
- Created two new columns number_of_new_restaurants and outlet_type which can be used in doing analysis for different KPIs and insights.

2. #### Restaurant-menus.csv:

- At first we have renamed the necessary columns so that there is no duplication and things make sense  when we merge the two files.
- We then removed all the additional or irrelevant characters from the data so that we can perform calculations and there is no confusion. 
- We also removed all the trailing spaces in between the data
- Next we ensured that '&' is replaced with 'and'
- We then dropped the description column as it was irrelevant for our insights and calculations
- Finally in the price column we ensured the proper format of the pricing so that there is no confusion/error in the calculations.

## DATA MERGING

- The merging part has been automated with functions such that it can be used on different files. 
- On running the code the system asks for either loading the respective CSV Files (Press 1) or Exit (Press 0) from the script. 
- On Selecting "0", the script will be ended with a 'Goodbye' response. 
- On Selecting "1", CSV files get loaded, cleaned, merged, saved on local directory. 

## DATA ANALYSIS AND VISUALIZATION

For the analysis part after cleaning and merging the two datasets we have analyzed the dataset on three KPIs: 

1. Price Range is Cheap and top 10 are based on count of Outlets
![Top 10 restaurant Chains in US by price range Cheap](https://github.com/MWaleedNasir/KSBL-Project/blob/main/Data_Visualization_1.png)

2. Top restaurants based on number of Outlets in the US
![Top 10 restaurant Chains in US by # of outlets](https://github.com/MWaleedNasir/KSBL-Project/blob/main/Data_Visualization_2.png)

3. Top restaurants in the cities of US based on count of Outlets
![Top 10 restaurant Chains in US by Cities](https://github.com/MWaleedNasir/KSBL-Project/blob/main/Data_Visualization_3.png)

Through the analysis and the charts following are the insights
- The Ice Cream Shop is the largest chain in the cheap category of price range. 
- The Ice Cream shop has the greatest number of outlets (total of 161) in US in all the cities. 
- Washington has the greatest number of restaurant chains in the US and it is the biggest market for anyone who wants to open anywhere in the US.  
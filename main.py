import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import random
import os
import time
from data_cleaning_script import data_cleaning_file
import sys

"""
Funtions To Read CSV file & Data Cleaning
Author: Waleed Nasir
"""   
def merge_file(filename1 , filename2, how, on):
    #Merging Both Files
    data_file = filename1.merge(filename2, how=how, on=on)
    return data_file

def read_csv_file(filename):
    current_directory = os.getcwd()
    dataframe = pd.read_csv(os.path.join(current_directory,filename+".csv"))
    return dataframe

"""Main Execution Part of Code"""

"""
Functions Data Visualization
Author: Muhammad Tariq Aijaz & Minhaaj Maqsood
"""

def horizontal_bar_plot_chart(df, xlabel, title):
    height = df.values
    bars = df.index
    y_pos = np.arange(len(bars))

    fig = plt.figure(figsize=[11,7], frameon=False)
    ax = fig.gca()
    ax.spines["top"].set_visible("#424242")
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#424242")
    ax.spines["bottom"].set_color("#424242")

    #colors = ["green","blue","magenta","cyan","gray","yellow","purple","violet","orange","red","maroon"]
    #random.shuffle(colors)
    colors = ["#f9cdac","#f2a49f","#ec7c92","#e65586","#bc438b","#933291","#692398","#551c7b","#41155e","#2d0f41"]
    plt.barh(y_pos, height, color=colors)
    
    plt.xticks(color="#424242")

    plt.yticks(y_pos, bars, color="#424242")
    plt.xlabel(xlabel)
    # plt.xlabel("Number of outlets in US")

    for i, v in enumerate(height):
        ax.text(v+3, i, str(v), color='#424242')

    plt.title(title)
    # plt.title("Top 10 Restaurant chain in US (by number of outlets)")

    return plt.show()

def vertical_bar_plot_chart(df, xlabel, title):
    height = df.values
    bars = df.index
    y_pos = np.arange(len(bars))

    fig = plt.figure(figsize=[11,7], frameon=False)
    ax = fig.gca()

    colors = ["green","blue","magenta","cyan","gray","yellow","purple","violet","orange","red","maroon"]
    random.shuffle(colors)
    colors = ["#f9cdac","#f2a49f","#ec7c92","#e65586","#bc438b","#933291","#692398","#551c7b","#41155e","#2d0f41"]

    plt.bar(bars, height, color=colors)

    plt.xlabel(xlabel)

    plt.title(title)

    plt.show()
    return plt.show()


"""Main Execution Part of Code"""

if __name__ == "__main__":
    running = True;
    while running:
        print("*************************************************")
        print("****UBER EATS ANALYSIS SIMULATOR****")
        print("*************************************************")
        print("Following are the commands to execute \n1) Upload CSV Files (Press 1) \n2) Exit (Press 0)\n")
        command_1 = input("Enter Command: ")
        
        if command_1 == '1':
            # print(os.listdir())
            # print("Enter csv file names from above list to load into data frames (Write only file names with space-seperated): ")
            # file_name1, file_name2 = input("").split()

            print("Loading CSV Files........")
            file_name1 = read_csv_file('restaurants')
            file_name2 = read_csv_file('restaurant-menus')
            time.sleep(1)

            print("Cleaning Data Files........")
            restaurants_data, restaurant_menu_data = data_cleaning_file(file_name1, file_name2)
            time.sleep(1)
            # print(restaurants_data)
            # print(restaurant_menu_data)

            print("Merging Data Files........")
            modified_data_file = merge_file(restaurants_data,restaurant_menu_data,'left','restaurant_id')
            modified_data_file.to_csv('modified_data_file.csv')
            time.sleep(1)

            print("File Saved in Local Directory.")

            print("Visualizing Data........")
            top10_chains = restaurants_data["restaurant_name"].value_counts()[:10].sort_values(ascending=False)
            horizontal_bar_plot_chart(top10_chains,'Number of outlets in US','Top 10 Restaurant chain in US (by number of outlets)')
            
            price_range_cheap = restaurants_data[restaurants_data["price_range"] == 'Cheap']
            top10_chains2 = price_range_cheap["restaurant_name"].value_counts()[:10].sort_values(ascending=False)
            horizontal_bar_plot_chart(top10_chains2,'Number of outlets in US','Top 10 Restaurant chain in US (by number of outlets & Price Range (Cheap))')

            price_range_list = ['Expensive','Very Expensive']
            price_range_expensive = restaurants_data[(restaurants_data['price_range'].isin(price_range_list)) & (restaurants_data['city'] != "")]
            top10_chains3 = price_range_expensive.groupby(['city'])['restaurant_id'].count().sort_values(ascending=False)[:10]
            vertical_bar_plot_chart(top10_chains2,'Number of outlets in US','Top 10 Restaurant chain in US By Cities')

            sys.exit()

        elif command_1 == '0':
            print("Good Bye!")
            sys.exit()    
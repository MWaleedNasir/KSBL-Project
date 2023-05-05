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

if __name__ == "__main__":
    running = True;
    while running:
        print("*************************************************")
        print("****WELCOME TO EXPLORATORY ANALYSIS SIMULATOR****")
        print("*************************************************")
        print("Following are the commands to execute \n1) Get list of files (Enter list) \n2) Exit (Press 0)")
        command_1 = input("Enter Command: ")
        
        if command_1 == 'list':
            print(os.listdir())
            print("Enter csv file names from above list to load into data frames (Write only file names with space-seperated): ")
            file_name1, file_name2 = input("").split()

            print("Loading CSV Files........")
            file_name1 = read_csv_file(file_name1)
            file_name2 = read_csv_file(file_name2)
            time.sleep(2)

            print("Cleaning Data Files........")
            restaurants_data, restaurant_menu_data = data_cleaning_file(file_name1, file_name2)
            time.sleep(2)
            # print(restaurants_data)
            # print(restaurant_menu_data)

            print("Merging Data Files........")
            modified_data_file = merge_file(restaurants_data,restaurant_menu_data,'left','restaurant_id')
            modified_data_file.to_csv('modified_data_file.csv')
            time.sleep(2)

            print("File Saved in Local Directory.")
            sys.exit()

        elif command_1 == '0':
            print("Good Bye!")
            sys.exit()    
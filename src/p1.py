

# import csv
# with open('q0c.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

# from multiprocessing import connection, render_template, request
# from flask import Flask
# import sqlite3
import pandas as pd
import csv


# app = Flask(__name__)

# df = pd.read_csv('/q0c.csv')
# df.columns = df.columns.str.strip() 

# for row in df.columns:
#             print(', '.join(row))

with open('src/q0c.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
              print(lines)


# @app.route('/')
# def index():
#    return render_template('index.html')

import pandas as pd

# Load the CSV file
file_path = 'src/q0c.csv'
df = pd.read_csv(file_path)

def fetch_row_by_column_value(df, column_name, value):
    filtered_row = df[df[column_name] == value]
    if filtered_row.empty:
        return None, df
    row = filtered_row.iloc[0]
    rest_of_columns = row.drop(labels=[column_name])
    return rest_of_columns, df.drop(filtered_row.index)

column_name = 'Name'  
value = 'cat' 
result, remaining_df = fetch_row_by_column_value(df, column_name, value)

print("Fetched Row :")
print(result)

print("\nRemaining DataFrame:")
print(remaining_df)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

df = pd.read_csv('nfl_offense_cleaned.csv')
print (df)

def cleanFile(csv):
    yearNum = 2017
    csv = csv[csv.YEAR != 2017.0]
    csv = csv.dropna(axis = 0, how = "any")
    csv = csv.reset_index(drop = True)
    csv = csv.drop(columns = ['RK'])
    return csv

def referenceSingle(csv, n):
    print(csv.loc[csv.PLAYER == n])

def referenceSingleYear(csv, y):
    print(csv.loc[csv.YEAR == y])

#implementation

df = cleanFile(df)
question = input("What stat would you like to view (Single or Cumulative): ")
if (question == "Single"):
    q1 = input("Would you like to search for Player or Year: ")
    if (q1 == "Player"):
        name = input("Enter the name of the player: ")
        referenceSingle(df, name)
    elif (q1 == "Year"):
        year = input("Enter the year: ")
        referenceSingleYear(df, year)

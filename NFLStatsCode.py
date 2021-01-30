import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

df = pd.read_csv('nfl_offense_cleaned.csv')
print(df.dtypes)

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

def referenceSingleYearPos(csv, y, p):
    print(csv.loc[(csv.YEAR == y) & (csv.POS == p)])

#implementation

df = cleanFile(df)
question = input("What stat would you like to view (Single or Cumulative): ")
if (question == "Single"):
    q1 = input("Would you like to search for Player or Year: ")
    if (q1 == "Player"):
        name = input("Enter the name of the player: ")
        referenceSingle(df, name)
    elif (q1 == "Year"):
        year = float(input("Enter the year: "))
        pos = str(input("What position would you like to search for (QB or ALL): "))
        if (pos == "QB"):
            referenceSingleYearPos(df, year, pos)
        elif (pos == "ALL"):
            referenceSingleYear(df, year)

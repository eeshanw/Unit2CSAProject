import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

#allows you to read the csv file and analyze the data
df = pd.read_csv('nfl_offense_cleaned.csv')

#removes the data for the year 2017 and resets the index column
def cleanFile(csv):
    yearNum = 2017
    csv = csv[csv.YEAR != 2017.0]
    csv = csv.dropna(axis = 0, how = "any")
    csv = csv.reset_index(drop = True)
    csv = csv.drop(columns = ['RK'])
    return csv

#finds entries for a certain player in the data set
def referenceSingle(csv, n):
    print(csv.loc[csv.PLAYER == n])

#finds entries for a certain year
def referenceSingleYear(csv, y):
    print(csv.loc[csv.YEAR == y])

#finds entries for a certain position in a certain year
def referenceSingleYearPos(csv, y, p):
    print(csv.loc[(csv.YEAR == y) & (csv.Positions == 'QB')])

#implementation

df = cleanFile(df)

#creates a new column for the position of each player in the dataframe
POSITION = []
for i in df.POS:
    POSITION.append((str(i)).strip())
df.insert(15, 'Positions', POSITION, True)

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
elif (question == "Cumulative"):
    q3 = input("Would you like to search for Player or Position: ")
    if (q3 == "Player"):
        q2 = input("Enter the name of the player: ")
        playerchart = (df.loc[df.PLAYER == q2])
        playerchart = playerchart.drop('YEAR', axis=1)
        average = playerchart.mean(axis=0)
        print(average)
    elif (q3 == "Position"):
        q4 = input("Enter the position: ")
        positionchart = (df.loc[df.POS == q4])
        print(positionchart)

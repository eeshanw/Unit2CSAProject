import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

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
    print(csv.loc[(csv.YEAR == y) & (csv.Positions == p)])

#averages the stats of all players from a certain position
def avgPerPos(csv, p):
    avgPlayerChart = csv.loc[df.Positions == p]
    averageStats = avgPlayerChart.mean(axis=0)
    print(averageStats)

#searches for all occurances with a certain team
def teamStat(csv, t):
    csv = csv.loc[csv.TEAM == t]
    print(csv)

#returns all players with a minimum of v yards thrown
def minStatisticYDS(csv, v):
    csv = csv.loc[csv.YDS >= v]
    print(csv)

#returns all players with a minimum of v touchdowns thrown
def minStatisticTD(csv, v):
    csv = csv.loc[csv.TD >= v]
    print(csv)

#returns all players with a minimum of v pass attempts
def minStatisticATT(csv, v):
    csv = csv.loc[csv.ATT >= v]
    print(csv)

#returns all players with v completions or more
def minStatisticCOMP(csv, v):
    csv = csv.loc[csv.COMP >= v]
    print(csv)

#returns the average of all the entries in the dataframe
def totalAverage(csv):
    averageChart = csv.drop('YEAR', axis=1)
    averageStats = averageChart.mean(axis=0)
    print('Average stats:')
    print(averageStats)

#returns the average of a single players
def playerAverage(csv, p):
    playerchart = (csv.loc[csv.PLAYER == q2])
    playerchart = playerchart.drop('YEAR', axis=1)
    average = playerchart.mean(axis=0)
    print(average)

#plots the spread of all players who threw a pass from 2007 to 2016
def plotPositions(csv):
    freqdict = {}
    totallist = []
    for i in csv.Positions:
        totallist.append(i)
    freqdict = Counter(totallist)

    labels = []
    numbers = []
    for i in csv.Positions:
        if i not in labels:
            labels.append(i)
    for i in freqdict:
        numbers.append(freqdict[i])

    x = np.arange(len(labels))
    width = 0.3

    fig, ax = plt.subplots()
    plot = ax.bar(x - width/2, numbers, width)

    ax.set_ylabel('Total Number')
    ax.set_title('Number of players that threw a pass by position')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    for l in plot:
        height = l.get_height()
        ax.annotate('{}'.format(height),
                    xy=(l.get_x() + l.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.show()

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
        pos = str(input("What position would you like to search for (Specific position or ALL): "))
        if (pos == "ALL"):
            referenceSingleYear(df, year)
        else:
            referenceSingleYearPos(df, year, pos)

elif (question == "Cumulative"):
    q3 = input("Would you like to search for Player or Position: ")
    if (q3 == "Player"):
        q2 = str(input("Enter the name of the player: "))
        playerAverage(df, q2)
    elif (q3 == "Position"):
        q4 = input("What statistic do you want to search for: Overall (ovr), Average per position (avperpos), Minimum stat (minstat), By team (team): ")
        if (q4 == "ovr"):
            totalAverage(df)
            print('Total number of players '+ str(len(df)))
            qG = input("Would you like to see the position breakdown as a graph (yes/no): ")
            if (qG == "yes"):
                plotPositions(df)
        elif (q4 == "team"):
            team = str(input("Which team would you like to search for: "))
            teamStat(df, team)
        elif (q4 == "avperpos"):
            q5 = str(input("Which position would you like to search for: "))
            avgPerPos(df, q5)
        elif (q4 == "minstat"):
            q6 = str(input("Which statistic (YDS, TD, ATT, COMP): "))
            q7 = int(input("Enter minimum value: "))
            if (q6 == "YDS"):
                minStatisticYDS(df, q7)
            elif (q6 == "TD"):
                minStatisticTD(df, q7)
            elif (q6 == "ATT"):
                minStatisticATT(df, q7)
            elif (q6 == "COMP"):
                minStatisticCOMP(df, q7)

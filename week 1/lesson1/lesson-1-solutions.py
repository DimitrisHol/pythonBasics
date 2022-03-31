# Week 1, Lesson 1 


# 4. Nested Lists
# Create a 2D array, 100x25 (rowsxcolumns)
# Fill the list with random integers (1,100) (min, max)
# For each row calculate the max and min number

import random

rows = 100
columns = 25

wholeArray = []
for i in range(rows) :
    columnArray = []
    for j in range(columns) : 
        columnArray.append(random.randint(1, 100))
    wholeArray.append(columnArray.copy())
print(wholeArray)

for i in range(len(wholeArray)) : 
    currentRow = wholeArray[i]
    print("For row :", i ,"(min/max) value (", min(currentRow), "/", max(currentRow), ")")


# 5.1 Single row files 
# 6,4,2,3,7,11,1,2,4,5

with open("singleRow.csv") as file : 
    contents = file.read()

data = contents.split(",")

maxValue = 0    
maxPosition = None

# Solution #1 : 

for i in range(len(data) - 1) : 
    intValue = int(data[i])

    if intValue > maxValue : 
        maxValue = intValue
        maxPosition = i

    # Check how the values are changing : 
    # print(i, maxValue, maxPosition)

print("The max value is :", maxValue, "at position", maxPosition)

# Alternate solution : 

# for number in data : 
#     intValue = int(number)
#     maxValue = max(intValue, maxValue)

#     # Check the max value as it's changing
#     print("Max Value : " , maxValue)

# print(maxValue, data.index(str(maxValue)))

# 5.2 File with multiple rows : 
"""
John,6
George,4
Lisa,2
Tom,3
Nick,7
Bill,11
Jean,1
Chris,2
Mary,4
Kevin,5
"""

with open("multiRow.csv") as file : 

    highestScore = 0
    winner = None

    for line in file : 
        data = line.rstrip().split(",")

        name = data[0]
        currentScore = int(data[1])

        if currentScore > highestScore : 
            highestScore = currentScore
            winner = name

print(winner, highestScore)

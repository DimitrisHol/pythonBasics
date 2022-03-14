## Lists : 

```python
a = [] # Empty List 
a = [1 ,2 ,3] # List of Numbers
a = [1, 2, 3, "Dimitris" , True , [4 , 5, 6]] # List can have whatever you want
```

     0  1  2  3  4  # Position
a = [1 ,2 ,3 ,4 ,5] # Value

```python
a[0] #  = 1
a[1] #  = 2
a[2] #  = 3
a[3] #  = 4
a[4] #  = 5
```

## Changing values within a list


```python
a = [1 ,2 ,3]

a[1] = 5

## a = [1 , 5, 3]

a.append(5) # a = [1,2,3,5]

a.pop(2) # a = [1,2,5]

x = "Hello" + " " + "World"

print (x) # Hello World
```

Strings work the same way as lists, but we **cannot** edit them

## Some useful builtIns 

x = ["a" , "b" , "c" , "a"]

print(x.index("a")) # 0
print(x.count("a")) # 2


## Splicing : (Κομμάτιασμα της λιστας)

a = [1, 2, 3, 4, 5]

a[2:4] # [3 ,4]

a[:4] # [1,2,3,4]

a [2:] # [3,4,5]

print (x[6:]) # World


## Check quadratic : 

```python
import math

quadratic = "x^2+5x+4"

a = 1
b = int(quadratic[4])
c = int(quadratic[7])

# print(b , c, type(b) , type(c))

D = b**2 - (4 * a * c)

# print("D = ", D)

x1 = ((-1 *b) + math.sqrt(D)) / 2 * a
x2 = ((-1 *b) - math.sqrt(D)) / 2 * a

print(x1, x2)
```

## Lists inside lists : 

a = [[1,2], [3,4]]

## How do the indexes work to get these ? 


x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]]
    
```python
oddNumbers = []
evenNumbers = []

for i in range(len(x)) : 

    for j in range(len(x[i])) : 

        number = x[i][j]

        print(i, j , number)

        if number % 2 == 0 : 
            evenNumbers.append(number)
        else : 
            oddNumbers.append(number)

print("Odd numbers : " , oddNumbers)
print("Even numbers : " , evenNumbers)
```
## Start reading from a file : 

```python
import os

print(os.getcwd())

totalSum = 0
totalCount = 0 

with open("/grades/test.csv") as file : 

    for line in file :

        currentNumber = int(line.rstrip())
        totalSum += currentNumber
        totalCount += 1

if (totalCount > 0) : 
    average = totalSum / totalCount
    print(average)
else : 
    print("Please give a better file")

```


## For loops / for number in a : loops

```python
myList = [["secondName", "thirdName"], ["Dimitris", "Giorgos"]]

for nestedList in myList : 

    for item in nestedList : 

        for character in item : 

            print(character)
```

Sorting on two different lists / same index for different lists ? 
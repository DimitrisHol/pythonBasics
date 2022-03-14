## Generic thought process behind writing a program : 

**Step 1 : Input** 

Get your input data either from : 
- the command line, such as a tool asking where to install an application
- through a file, reading a CSV file containing values
- generate them during the program, for example generating the first 100 prime numbers.

**Step 2 : Process the data** 

All the calculations to be done to your input in order
to produce the wanted result. 

This also includes taking the raw input and creating a model to convert it to useful information/data. 

**Step 3 : Return the result to the user** 

Return the data either by : 

- printing them to the console
- writing/appending them to a file. 

## Example program : 

Create a program that will calculate the average score from X numbers

```python
# 1. Read the student scores from a file called "scores.csv" : 
sumOfScores = 0
numberOfScores = 0

with open("scores.csv") as file: 

    for line in file: 

        # 2. Compute the average
        sumOfScores += int(line.rstrip())
        numberOfScores += 1
        
averageScore = sumOfScores / numberOfScores
 
# 3. Print out the average. 
print(averageScore) # 6
```
`scores.csv :` 
```csv
5
3
10
```

## Variables : 

Basic types of variables : 

- int : Integers
- float : numbers with decimal value
- string : Alphanumericals (basically text)
- bool : a variable containing either `True` or `False` 

Examples : 
```python
x = 5 
y = 6.3
z = "A message" 
v = True or False
```


| Python       |      Basic calculations      |
|--------------|:----------------------------:|
| `x = 5 + 4`  |           Addition           |
| `x = 5 - 4`  |          Subtraction         |
| `x = 5 * 4`  |        Multiplication        |
| `x = 5 **3`  |      Powers (`x = 125`)      |
| `x = 5 / 2`  |     Division (`x = 2.5`)     |
| `x = 5 // 2` |   Division result (`x = 2`)  |
| `x = 5 % 2`  | Division remainder (`x = 1`) |

Variable type casting (converting from one type to another)

> You can check the the type of a variable (x) by running 
```python
x = 5 
type(x) # <class 'int'>
```

Examples : 
```python
x = int("9") # x = 9 , type = Integer
x = int(9.5) # x = 9 , type Integer.
x = int("9.5") # Traceback Error (can't cast it!)
x = int(float("9.5")) # x = 9 , type Integer.
x = float ("9") # x = 9.0 , type Float
```

### Boolean Algebra : 

| **X** | **Y** | **OR** | **AND** |
|:-----:|:-----:|:------:|:-------:|
| False | False |  False |  False  |
| False |  True |  True  |  False  |
|  True | False |  True  |  False  |
|  True |  True |  True  |   True  |


|  **Boolean Operators** :  |       |
|:--------------------------:|-------|
|            4 < 5           |  True |
|         6.7 >= 6.7         |  True |
| "Different" == "Message" : | False |
|        False != True       |  True |

## Control Flow : 

Change the block of code to be executed, depending on a check : 

```python
if boolean_expression : 
    someCode()
    someMoreCode()
elif some_other_boolean_expression : 
    anotherBlockOfCode()
else : 
    thirdBlockOfCode()
```

Only one of the three blocks will be executed. Example : 

```python 
userGrade = input("Please give me an integer from 0-10")

grade = int(userGrade)

if grade >= 8 : 
    print("Excellent")
elif grade >= 5 : 
    print("Good enough")
else : 
    print("Fail")
```

Numbers 8,9,10 : "Excellent"
Numbers 5,6,7  : "Good enough"
Numbers 0,1,2,3,4 : "Fail"

> Notice that each number cannot match to multiple blocks

## Loops : 

What happens when we want to keep executing some code until a certain condition has been met ? 

### `While` loops : 

Have the user give you a positive integer until it's between 0-10 

```python

number = input("Give me a number from 0-10")

answer = int(number)

while (answer < 0 and answer > 10) : 

    print("Number not accepted, please try again...")
    number = input("Give me a number from 0-10")

print("The number you gave me is : ", answer)
```

The above code will keep asking for a positive integer between 0-10, **until** the user 
gives a number that meets the conditions. 

We use `while` when we don't know how many times a loop will take to complete. 


### `for` loops : 

- `range(X)` Returns a list of numbers starting from 0, up to but not including **X** :
E.g. for X = 5, range(5) = (0,1,2,3,4)
- `range(X,Y)` Returns a list of numbers starting from **X**, up to but not including **Y** :
E.g. for X = 3 and Y = 5, range(3,5) = (0,1,2,3,4)
- `range(X,Y,Z)` Returns a list of numbers starting from **X**, up to but not including **Y**, with a step of **Z**:
E.g. for X = 0, Y = 10, Z = 2 :  range(1,10,2) = (1,3,5,7,9)







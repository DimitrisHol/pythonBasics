## Lists : 

Lists is a collection of objects, be that of integers, floats, strings booleans, or even other lists. 

```python
a = [] # Empty List 
a = [1 ,2 ,3] # List of Numbers
a = [1, 2, 3, "Some String" , True , [4 , 5, 6]] 
# A single list may hold elements of all types, even other lists!
```

The elements of a list **are ordered**, and each one 
has a specific position in the list. The ordering of a list is as follows : 

```
     0  1  2  3  4  Position
a = [1 ,2 ,3 ,4 ,5] Value
```

The first index for a list, meaning the number that points
to the first element of the list, is 0 (instead of 1).

```python
a[0] #  = 1
a[1] #  = 2
a[2] #  = 3
a[3] #  = 4
a[4] #  = 5
```

## Changing values within a list

The contents of a list are mutable, meaning that elements of the list can change values 
(or even data types, although not advised).

```python
a = [1 ,2 ,3]

# Assigning a different value to a list element
a[1] = 5

# List is now : 
# a = [1, 5, 3]
```
> You can completely change the value of an element, although it's advised to stick to the same data type

```python
a[2] = "Some string"
# a = [1, 5, "Some string"]
```
Python also includes some basic functions to help you manipulate lists : 

```python
a = [1, 2, 3]

# Adding an element to the end of the list :
a.append(5) # a = [1,2,3,5]

# Removing an element from an specific index :
a.pop(2) # a = [1,2,5]
```
> Remember that index = 2 points to the 3rd element in the list
```python
# Returning the size of a list : 
listLength = len(a) # listLength = 3

x = ["a" , "b" , "c" , "a"]
# Returns the index of "a", in this case 0
print(x.index("a")) 
# Returns how many "a" exist in the list, in this case 2
print(x.count("a")) 
```


## Splicing : Taking parts of the list

`someList[start:end]`

Similarly to `range(start,end)`, this will return the element of a list
starting from the element at index = start, and stopping at the element with
index = end (but not including it.)

You can ommit either `start` or `end`, resulting in the slice starting from the beginning of the list, or extending the slice to the end of the list respectively.

Some examples : 

```python
a = [1, 2, 3, 4, 5]

a[2:4] # [3 ,4]

a[:4] # [1,2,3,4]

a[2:] # [3,4,5]
```


| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|----|
| H | E | L | L | O |   | W | O | R | L | D  |

Slicing also works with `strings` : 
```PYTHON
x = "Hello World"
print (x[6:]) # World
```

Let's see an example where we can use the list indexing to parse a quadratic equation and calculate the solutions

```python
import math

quadratic = "x^2+5x+4"

a = 1   # Simplify this, always 1
b = int(quadratic[4])   # We are targeting '5'
c = int(quadratic[7])   # We are targeting '4'

D = b**2 - (4 * a * c)
# print("D = ", D)

x1 = ((-1 *b) + math.sqrt(D)) / 2 * a
x2 = ((-1 *b) - math.sqrt(D)) / 2 * a

print(x1, x2)
```

## Lists inside lists : 

It was mentioned above that an element of a list, can be another list, resulting in nested lists. 

```python
a = [[1,2], [3,4]]

# a[0] = [1,2]
# a[1] = [3,4]
```
In order to get the elements of a nested list, you simply use the brackets, and the index of the element. To target element `3` we want to grab the second list, and of that the first element :

```python
nestedList = a[1] # Getting the 2nd list
desiredElement = nestedList[0] # Getting number 3.

# Or to write this more concisely : 
desiredElement = a[1][0]
```
Having lists inside lists can also be interpreted as a two-dimensional array : 

| 1 | 2 |
|---|---|
| 3 | 4 |

The element `3` is on the 2nd row, and on the first column, and since list indexing starts from 0, that translates into 

`array[1][0]`

- 2nd row : index 1 for our list 
- 1st column : index 0 for our list. 

Example with a bigger list : 

```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
|  |  |  |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

To retrieve element `8`, that would be on the 3rd row, 2nd column. Translating this to python lists : 

```python
targetElement = a[2][1] # 8
```

## Usages / Loops 

The biggest usage of lists, is that we can access the same data multiple times. There are some operations that might require more than one pass of the same data to calculate what we want. 

**Example :**

Let's calculate the average of some numbers. Let's say that the user gives us the numbers one by one : 

```python
sumOfNumbers = 0
countOfNumbers = 0

number = int(input("Please give me a number. Give 0 to stop. "))

while number != 0 : 
    sumOfNumbers += number
    countOfNumbers += 1
    number = int(input("Please give me a number. Give 0 to stop. "))

if countOfNumbers > 0 : 
    average = sumOfNumbers / countOfNumbers
    print(average)
```
In this example, we didn't have to store the values of the numbers.
Next, let's find out **how many numbers are greater than the average**. 

This is where the usage of lists comes into play, lists allow us to store information that we otherwise wouldn't be able to through a single iteration pass : 

```python
sumOfNumbers = 0
countOfNumbers = 0

# This time store the numbers in a list
numbers = []

number = int(input("Please give me a number. Give 0 to stop."))
while number != 0 : 
    sumOfNumbers += number
    countOfNumbers += 1
    if number != 0 : 
        numbers.append(number)
    number = int(input("Please give me a number. Give 0 to stop."))

if countOfNumbers > 0 : 
    average = sumOfNumbers / countOfNumbers
    
    countHigherThanAverage = 0

    # We can now iterate again through the list
    # to calculate what we need 
    for i in range(len(numbers)) : 
        if numbers[i] > average  : 
            countHigherThanAverage += 1
    print(average, countHigherThanAverage)
```

## Using files as inputs : 

So far we've seen using the user input to create data, or just hardcoding them into the program. The last way to input data into our program, is to read the contents of a file : 

Example : Let's assume we have a simple text file that contains 10 numbers seperated by commas. 

```
6,4,2,3,7,11,1,2,4,5
```
The only thing required to determine which file python should open, is the filename. (Careful to have the file inside the same directory as the python script.) For this example the name of our file would be `test.csv`.


```python
# Step 1 : Open the contents of the file : 
with open("test.csv") as file : 
    # Some code
    # Some other code
# Rest of the program
# Here the file is closed, contents no longer available.
```
Here we are opening a file with the name `test.csv` and we're storing it to a variable called `file`. With this implementation, the contents of the file are available only inside the block of code under `with`. 

```python
with open("test.csv") as file : 
    # Step 2 : Read the contents of the file : 
    contents = file.read()
    print(contents, type(contents))
```
Using the `read()` method, we are able to pass the contents of the file into memory. Note that the contents are now basically a big string. 

Next, comma seperated values are pretty convenient to convert to a list. We can easily do that with the `split()` method. This will return a list of strings, seperating each element with the delimiter. In our case the delimiter is the comma.

We can continue with the processing of the data outside the block of code that was used to read the file. This means that we release the file, since we no longer need it.  

```python
with open("test.csv") as file : 
    contents = file.read()
# Step 3 : Parse the data into a data structure
numbers = contents.split(",") # Comma seperated numbers, split them with ","
print(numbers) # ['6', '4', '2', '3', '7', '11', '1', '2', '4', '5']
```
Notice how the numbers are actually strings, so we should convert them to integers.

```python
with open("test.csv") as file : 
    contents = file.read()
data = contents.split(",")

# Step 4 : Convert the string into integers
numbers = []
for i in range(len(data)) : 
    numbers.append(int(data[i]))
print(numbers) # [6, 4, 2, 3, 7, 11, 1, 2, 4, 5]
```
And now this list is ready to be used however we want. 


## Alternative looping : 

So far to iterate through a list, we used an iterator to go through the size of a list, and then retrieve each of the elements in the list. 

```python
someList = [1,2,3,4]

for i in range(len(someList)) :
    print(someList[i])
```
```
1
2
3
4
```

There is an alternative way to loop through a list, without the use of an iterator. Instead we are simply looping over each **element** of the list.

```python
someList = [1,2,3,4]
for number in someList : 
    print(number)
```
With this way, within each iteration of loop, the `number` variable will take the value of the element in the list. Not having the index of the list might be more limiting, but there are lots of times where this can be easier both to read and to write.

Let's see an example with nested lists : 
```python
myList = [["apples", "oranges"], ["dog", "cat"]]

for nestedList in myList : 
    # This will loop through both nested lists
    for item in nestedList : 
        # This will loop through the items of the nested list
        for character in item : 
            # This will loop through the characters of each item of the nested list
            print(character)
```

## Files vol 2 : 

In the last example, the file contents were in a single line, seperated by commas.

```
6,4,2,3,7,11,1,2,4,5
```
Let's see an example where each number is on a different line : 
```
6
4
2
3
7
11
1
2
4
5
```
The basic logic behind parsing the file into a data structure is very similar, the differences are in how we loop through each line. Let's start by opening and reading the file contents :

```python
with open("test.csv") as file : 
    # This time we are gonna be directly looping through each line
    # instead of loading the whole file into a variable. 
    for line in file : 
        print(line)
```
This time instead of having a single variable that holds the entirety of the file as a string, we're now looping through each line of the file, and storing it to the `line` variable. The line variable is still a string, just now it only contains one line of the file.

Notice that when we print each line, we get a double new line each time. To fix this, we can strip the non-characters from each line with the `rstrip()` method. 


```python
with open("test.csv") as file : 
    for line in file : 
        # Use rstrip() to remove the new line at the end of each number
        print(line.rstrip())
```
Next up, as before we want to store the data into a list : 
```python
data = []

with open("test.csv") as file : 
    for line in file : 
        # Cast the number into an integer, and append it to our list
        number = int(line.rstrip())
        data.append(number)
# Print the data outside of the loop, and optionally outside of the file opening transaction
print(data)
```
We have successfuly parsed a file with each number stored vertically! 











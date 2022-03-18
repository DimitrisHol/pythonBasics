## List iteration : 

### 1. From the following list, print :

```python
x = [22,24,12,20,55,38,703,4,20]
```
1. The first three numbers
2. The last three numbers
3. Numbers starting from the 3rd, up to (also including) 6th
4. Numbers starting from 5th to the end
5. The 5th and 7th number
6. The position of number 22
7. How many times does number 20 appear

### 2. What is the output of the following operations : 

```python
x = [43,21,3 , [84,345,61], 75,89,96]
```

1. How do we get the number `345`
2. How do we get the numbers `89` and `96`
3. How do we get the number `84` and `345`
4. 
```python
x = [2,4,5,8]
x[2:4] = [10,12]
print(x)
```

### 3. What will each print statement output ? 

```python
x = ["a", "b"]
x.append("c")
print(x)

x.append(["d", "e"])
print(x)

x.insert(2, "o")
print(x)

x.extend(["f", "g"])
print(x)
```


### 4. Nested Lists : 

To pick a random number in python, you first import the library `random`
and then you can use the method `random.randint(a,b)` which returns a random integer 
from a to b.

```python
import random 

for i in range(10) : 
    print(random.randint(1,10))
```
For example, this will print 10 random numbers from 1 to 10.

#### Goal : 

- Create a "2D" list with 100 rows, and 25 columns.
- Fill the list with random integers from 1 to 100
- For each row, calculate and print the maximum and the minimum number that was generated.


### 5. Files : 

1. Create a file called `test.csv` that contains the following numbers : 
    ```
    6,4,2,3,7,11,1,2,4,5
    ```
    Calculate and print the largest number, and the position of that number.

2. Create a file called `test.csv` that contains the following data : 
    ```
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
    ```
    Calculate and print the name and the score of the highest scoring person. 
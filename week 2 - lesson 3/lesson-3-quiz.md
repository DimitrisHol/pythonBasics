## Dictionaries & Sets : 

### 1. From the following dictionary : 

```python

student = {
	"name" : "Sam",
	"age" : 24
	"score" : 88
	"classes" : ["CompScience" , "Science" , "Math"]
	}
```

1. Retrieve and print the name of the student
2. Retrieve and print the age of the student
3. Retrieve and print the first 2 classes of the student
4. Create a new dictionary that only contains the `name` and `score` keys/ values
```python
{"name" : "Sam","score" : 88}
```
5. Print a message whether the student is enrolled in class "Science"


### 2. Find a way to retrieve value 30 from the following dictionary : 

```python
x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]
```

### 3. Sets : What is the result of executing the following code : 

```python
z = set((1,2,2,2,2,2,2,1))
print(z)

z.add(1)
z.remove(2)

print(z)
print( 1 in z)


a = {2,3,4}

print(z & a)
print(z | a)

print(1 in Z & 1 in a)
print(1 in Z | 1 in a)

print(len(a))
print(a[0:2])
print(a[10])
```



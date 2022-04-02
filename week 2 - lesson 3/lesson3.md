## Lists vs Dictionaries : 

Until now we've seen that to group variables together, we've used lists. The characteristics of a list are as follows : 

- The elements of a list are ordered.
- The elements of a list can be retrieved by using an index. 
- We can have different types of elements within the same list, for example integers, floats, strings, or even other lists. 
- We can modify the contents of a list. (append or remove)

Now let's take a look at **Dictionaries** : 

WHat do they have common with lists : 

- They are both mutable, meaning we can modify their contents. 
- Their size is dynamic, meaning that they grow and shrink depending on how many elements they contain. 
- Dictionaries can also contain lists, and vice versa, a list can contain dictionaries. 

The important part is where the differ though, and **that is on how their elements are accessed.** 

1. Where lists are ordered, dictionaries are simply a collection, with no index. 
2. **Most importantly, dictionaries comprise of pairs of keys and values, instead of a single object of a list**. 

Each key in a dictionary is **unique** and corresponds to a value. To retrieve the value of the element, simply query the dictionary for its key. An example would be the index of a book, the chapter names are keys, and the values are the corresponding page numbers. 

```python 
a = {} # Empty Dictionary.
a = {"Naked Gun" : "Comedy", "Night of the Living Dead" : "Horror"} # A dictionary with keys holding movie names, and the values holding the genre of said movie. 
a = {"Naked Gun" : ["Leslie Nielsen", "Priscilla Presley"]} # The value of a dictionary can also be a list, in this example holding the actors of the movie, which name represents the key. 

print(a["Naked Gun"]) # Comedy
print(a.get("Naked Gun")) # Comedy (Alternative way to retrieve the value)
```

As mentioned before, we know don't retrieve elements through their index in the list, but through their key. Keys are always 

## Modifying values in a dictionary : 

```python 
a = {}
a["Chapter A"] = 10 # Chapter A is in page 10
a["Chapter B"] = 20
# a = {"Chapter A" = 10, "Chapter B" : 20}

a["Chapter A"] = 30 # Overrides the value, the key stays the same
# a = {"Chapter A" = 30, "Chapter B" : 20}

a.pop("Chapter B") # This will remove both key and value
# a = {"Chapter A" = 30}
```

## Limitations in the types of keys you can use. 

The most common types of variables to use as keys are integers, floats, booleans, strings. 

```python
someDictionary = {1 : "A", 1.5 : "B" , True : "Yes", "Python" : "Cool"}
```

List elements could be any type of variable, but in dictionaries, the **keys** have some limitations. That doesn't mean that we can't have different types of variables inside the same dictionary as you see in the code above.

You can even use types of variables as the key : 

```python
typesDictionary = {int: 1, float: 2, bool: 3, str : 4}
print(typesDictionary[int]) # 1
```
The restrictions are the following : 

1. Keys are unique, meaning that a single key can appear only once inside the dictionary. 
Trying to set the value of a key that already exists in the dictionary, will override the previous corresponding value. 

```python
a = {1 : "A" , 2 : "B"}
a[1] = "C"
print(a) # {1 : "C", 2 : "B"}
```

2. The keys of a dictionary must be an immutable type. Immutables are `int`, `float`, `bool`, but most importantly `list` are not. Same goes for dictionaries, so that basically means that you can use pretty much anything for a key apart from lists and dictionaries. 

> Note : Although lists and dictionaries cannot be a key to a dictionary, they can be a value to a key. 

```python 
someDictionary = {[1,2,3] : "A"} # This isn't allowed
someDictionary = {{2 : "B"} : "A"} # This isn't allowed also
someDictionary = {1 : [1,2,3]} # This is good ! 
someDictionary = {1 : {2 : "B"}} # This is also good ! 
```

## Some basic functions for dictionaries : 

**1. Merging two dictionaries :**

```python
dict1 = {1 : [1, 3, 5]}
dict2 = {2 : [2, 4, 6]}

dict1.update(dict2)
print(dict1) # {1 : [1, 3, 5], 2 : [2, 4, 6]}
```
> Be careful as same keys are overriden

**2. Checking if a key is in the dictionary :** 

```python 
dict1 = {"Dimitris" : "123456789" , "Giorgos" : "789456123"}
print("Dimitris" in dict1) # True
print("123456789" in dict1) # False
```
The `in` keyword searches only through the keys, not the values.

If we want to iterate through the dictionary keys or values, or both the ways to do are the following : 

The keys of a dictionary can be returned by using `dictionary.keys()`
The values of a dictionary can be returned by useing `dicdtionary.values()`

And a data structure that contains all the key/value pairs can be returned by using `dictionary.items()`

```python
# By default iteration used the keys :
dictionary = {1 : "A" , 2 : "B", 3 : "C"}
for key in dictionary : 
    print(key)
# 1
# 2
# 3
```
**3. Iterating through the values of a dictionary :** 
```python
dictionary = {1 : "A" , 2 : "B", 3 : "C"}
for value in dictionary.values() : 

    print(value)
# A
# B
# C
```
**4. A bit weird, but we can use two values before `in` to iterate using the pair of the key/value.**

```python
dictionary = {1 : "A" , 2 : "B", 3 : "C"}
for (key, value) in dictionary.items() : 
    print (key , value)
# 1 A
# 2 B
# 3 C
```


## Sets : 

The final widely used data structure is **Sets**.

Very similar to the sets seen in Maths, the purpose of sets is that each of their elements are unique, and can appear only once. 

```python 
x = {1 , 3, 2, 1, 1, 2, 1, 3}
print (x) # set (2,1,3)
```
> Notice how there are no duplicate values. 

Sets also are similar with dictionaries in two ways : 

1. The elements in a set are not ordered.
2. Just like dictionary keys, the elements of a set are immutable. In essence that means you cannot add a list or a dictionary as an element of a set. 

```python
x = {[1,2,3], [4,5,6]}
# TypeError: unhashable type: 'list'
```

## Some basic functions for dictionaries : 

One of the most common usages of a set is to check if some element exists in that set. That can be easily done by : 

```python 
x = {1,2,3}
1 in x # True
4 in x # False
```

The most basic methods, like insertion and deletion are supported

```python

x = {1,2}
x.add(3) # x = {1,2,3}
x.remove(2) # x = {1,3}
```

Let's create 3 different sets, containing the first 4 odd, even and prime numbers : 

```python
odds = {1, 3, 5 , 7}
evens = {2, 4, 6, 8}
primes = {2, 3, 5 , 7}
```

Sets have already defined methods to calculate common elements, different elements, or the sum of the elements, very similarly to maths. 

```python
odds.intersection(primes) # {3, 5, 7}
odds.intersection(evens) # {}

odds.difference(primes) # {1}
odds.difference(evens) # {1, 3, 5, 7}

odds.union(evens) # {1, 2, 3, 4, 5, 6, 7, 8}
odds.union(primes) # {1, 2, 3, 5, 7}

# You can also use boolean operators : 

odds & primes # {3, 5, 7}
primes - odds # {2}
odds | evens # {1,2,3,4,5,6,7,8}
```




# Week 1 , Lesson 0 Solutions : 

# 1. 
colour = input("Please give me one of the primary colours (Red, Green Blue): ")
while not (colour == "Blue" or colour == "Red" or colour == "Green") : 
    colour = input("Please give me one of the primary colours : ")

print("Congrats on giving me a primary colour.")


## 2. Number Guessing : 
numberToGuess = 3
guessingNumber = int(input("Guess the number : "))
while guessingNumber != numberToGuess : 
    guessingNumber = int(input("Please try again : "))
print("You found my number !")

## 3. Number Guessing with available tries :
availableTries = 3

guessingNumber = 5
userNumber = None

while userNumber != guessingNumber and availableTries > 0 : 
    print("The available tries are : ", availableTries)
    userNumber = int(input("Please give me your number "))
    availableTries -= 1

if (availableTries >= 0) : 
    print("You found the number")
else : 
    print("You're out of tries")

## 4. Sum of integers up until number given 
numberGiven = int(input("Please give me a positive integer : "))
total = 0  
for i in range(1, numberGiven + 1) : 
    total += i

print("Final Sum for " , numberGiven , "is : ", total)


## 5. Sum of prime integers up until number given 
def isPrime(number) : 
    for i in range(2, int(number/2)) : 
        if number % i == 0 : 
            return False
    return True

givenNumber = int(input("Please give me your number "))
total = 0
for number in range(1, givenNumber + 1) : 
    if isPrime(number) : 
        print("I am a prime number : ", number)
        total += number
print(total)

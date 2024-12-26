import random

number = random.randint(10,20)

while True :
    guessed_number = int(input("Enter the number: "))
    if guessed_number == number :
        print("You have guessed it right!!🏆")
        break
    else :
        print("Your guess is wrong. Try again!!")


import random

secret_number = str(random.randint(10,99))

print(" Welcome To The Cows & Bulls Game")

print("It's Two Digit Number Guessing Game")

chances = 7

while chances >0:

    player_guess = input("Enter Your Guess Number :")

    if secret_number == player_guess:
        print("Congrats !!! You Won The Game")
        break

    
    else:

        cows=0
        bulls=0

        if secret_number[0] == player_guess[0]:
            bulls+=1

        if secret_number[1] == player_guess[1]:
            bulls+=1

        if secret_number[0] == player_guess[1]:
            cows+=1

        if secret_number[1] == player_guess[0]:
            cows+=1


        print("Bulls :",bulls)

        print("Cows :",cows)

        chances -=1


        if chances <1:
            print("You Lost The Game!!!")
            print("The Secret Number is :",secret_number)
            break

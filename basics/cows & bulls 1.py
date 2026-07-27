import random

secret_no = str(random.randint(10,99))

print("Welcome To The Number Guessing Game(Two Digit)")


chances = 7

while chances >0:

    player_gue = input("Enter Your Guessing Number :")

    if secret_no == player_gue :
        print("Congrats!!! You Win The Game!!!")
        break

    else:
        cows=0
        bulls=0

        if secret_no[0] == player_gue[0]:
            bulls+=1

        if secret_no[1] == player_gue[1]:
            bulls+=1

        if secret_no[0] == player_gue[1]:
            cows+=1

        if secret_no[1] == player_gue[0]:
            cows+=1

        print("Bulls :",bulls)

        print("Cows :",cows)


        chances -=1

        if chances <1:

            print("You Lost The Game!!!")
            print("The Secret Number is :",secret_no)
            break

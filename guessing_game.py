import random

def guessing_game():
    num = random.randint(1, 100) 
    guess =
    while guess != num:
        guess = int(input("what number would you like to choose?: "))
        if (num  == guess):
            print("You won!")
            break
        elif guess < num: 
            print("Your number is lower so keep trying!")
        else:  
            print("Your number is higher so keep trying!")

        


    


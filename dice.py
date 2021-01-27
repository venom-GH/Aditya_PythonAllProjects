import random

#taking input to start the game
roll = input ("do you wanna roll the dice: \n >>>")

#the loop to check if the user wants to continue the game
while roll == "yes" or roll == "y":
    numberList = [1,2,3,4,5,6]

    #the random value is picked and printed
    print("Your value is: ", random.choice(numberList))
    roll = input("Roll the dices again?")

#user exits the game
input ("press any key to exit the game....")

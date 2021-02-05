import random
choice=["rock","paper","scissors"]
rock = choice[0]
paper = choice[1]
scissors = choice[2]
print(" WELCOME to rock, paper, scissors game. Press 'q' to end the game.")
while True:
    user_choice = input(" What is your choice? rock, paper or scissors?:\n ").lower()
    computer_choice = random.choice(choice)
    if user_choice not in choice:
        print(" You entered the wrong word.Let's try again...")
    if user_choice == rock:
        if computer_choice == rock:
            print(" Computer choice is : rock. Result: Draw")
        elif computer_choice ==paper:
            print(" Computer choice is : paper. You Lost!")
        else:
            print(" Computer choice is : scissors. Result:You Won.")
    if user_choice == paper:
        if computer_choice == rock:
            print(" Computer choice is : rock. Result: You Won.")
        elif computer_choice == paper:
            print(" Computer choice is : paper. Result: Draw")
        else:
            print(" Computer choice is : scissors. Result:You Lost!")
    if user_choice == scissors:
        if computer_choice == rock:
            print(" Computer choice is : rock Result: You Lost!")
        elif computer_choice == paper:
            print(" Computer choice is : paper Result: You Won.")
        else:
            print(" Computer choice is : scissors Result:Draw")
    if user_choice == 'q' or user_choice == 'Q':
        print("Exiting...")
        break
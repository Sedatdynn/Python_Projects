import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print(f'Sorry your guess:{guess} low! Guess again..')
            elif guess > random_number:
                print(f'Sorry your guess:{guess} high! Guess again..')
        except:
            print("Try again")
    print(f'Congrats. You have guessed the number {random_number} correctly.')
            

guess(100) 
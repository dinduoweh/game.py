import random


options = ("rock", "paper","scissors" )

container= True


while container:

    player = None

    computer = random.choice(options)
    while player not in options:
        player = input('Enter your choice(rock,  paper, scissors):')
    print(F" player: {player}")
    print(F" computer: {computer}")
    if player == computer:
        print("it is a tie!")
    elif player == "rock" and computer == "scissors" :
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")


    if not input("Play again? (y/n): ").lower()  == "y" :
      

      container = False

    


print("Thanks for playing ")
    

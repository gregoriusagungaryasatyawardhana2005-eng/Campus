import random
options = ("rock","paper","scissor")
running = True
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice: ").lower()
        

    print(f"Player : {player}")
    print(f"Computer : {computer}")
    
    if player == computer:
        print("It's a tie")
        done = True
    elif player == "rock" and computer == "scissor":
        print("you win")
        done = True
    elif player == "scissor" and computer == "paper":
        print("you win")
        done = True
    elif player == "paper" and computer == "rock":
        print("you win")
        done = True
    else:
        print("you lose")
        done = True
    if done == True:
        play_again = input("Play Again (y/n)").lower()
        if play_again == "n":
            running = False
        if play_again == "y":
            done = False
        else:
            print("Insert (y/n)")


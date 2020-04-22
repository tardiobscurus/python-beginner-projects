import random


while True:
    rand = random.randint(1, 3)

    user_input = input("Rock, paper, or scissors? > ").lower()
    computer_inp = ""

    if rand == 1:
        computer_inp = "rock"
    elif rand == 2:
        computer_inp = "paper"
    else:
        computer_inp = "scissors"

    print(f"\nComputer chose: {computer_inp} \nYou chose: {user_input}")
    print()

    if user_input == computer_inp:
        print("Draw!")
    elif user_input == "rock":
        if computer_inp == "scissors":
              print("You won\n")
        else:
             print("You lost...\n")

    elif user_input == "paper":
        if computer_inp == "rock":
              print("You won\n")
        else:
             print("You lost...\n")
             
    elif user_input == "scissors":
        if computer_inp == "paper":
              print("You won\n")
        else:
             print("You lost...\n")
    else:
        print("Invalid input...\n")
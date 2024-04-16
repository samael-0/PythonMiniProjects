import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Please give a valid response")
        continue

    random_number = random.randint(0, 2)
    # rock:0 paper:1 scissor:2
    computer_picks = options[random_number]
    print("Computer Picked", computer_picks + ".")

    if user_input == "rock" and computer_picks == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_picks == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_picks == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == "rock" and computer_picks == "rock":
        print("Its Draw!")
        user_wins += 1

    elif user_input == "paper" and computer_picks == "paper":
        print("Its Draw!")
        user_wins += 1
    elif user_input == "scissors" and computer_picks == "scissors":
        print("Its Draw!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1


print("Your won", user_wins, "times")
print("Computer won", computer_wins, "times")

print("Better luck next time")

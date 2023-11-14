import random

player_score = 0
computer_score = 0

while True:
    print("Let's play Rock-Paper-Scissors!")
    player_choice = input(
        "Enter your choice (rock, paper, or scissors), or 'q' to quit: ")
    

    # Check if player wants to quit
    if player_choice == "q":
        break

    # Check if player input is valid
    if player_choice not in ["q", "rock", "paper", "scissors"]:
        print("Invalid input, please try again.")
        continue

    # Computer randomly selects an option
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print(f"\nYou chose {player_choice}, and computer chose {computer_choice}.\n")

    # Check for a tie
    if player_choice == computer_choice:
        print("It's a tie!")
        player_score += 1
        computer_score += 1

    # Check for player win conditions
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1

    # Otherwise, computer wins
    else:
        print("Computer wins!")
        computer_score += 1

    #Print current score
    print(f"\nScoreboard: You {player_score}, computer {computer_score}\n")

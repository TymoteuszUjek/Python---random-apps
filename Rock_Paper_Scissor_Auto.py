import random

computer_1_score = 0
computer_2_score = 0
games_played = 0

while True:
    print("Auto game: Rock, Paper Scissors")
    input("Press enter to continue, or 'q' to quit:")

    #Check if player wants to quit
    if input() == "q":
        break

    #Computer randomly selects an option
    options = ["rock", "paper", "scissors"]
    computer_1_choice = random.choice(options)
    computer_2_choice = random.choice(options)

    print(f"\nComputer 1 chose {computer_1_choice}, and Computer 2 chose {computer_2_choice}.\n")

    # Check for a tie
    if computer_1_choice == computer_2_choice:
        print ("It's a tie!")
        computer_1_score += 1
        computer_2_score += 1

    #Check for computer 1 win conditions
    elif computer_1_choice == "rock" and computer_2_choice == "scissors":
        print ("Computer 1 wins!")
        computer_1_score +=1
    elif computer_1_choice == "paper" and computer_2_choice == "rock":
        print("Computer 1 wins!")
        computer_1_score += 1
    elif computer_1_choice == "scissors" and computer_2_choice == "paper":
        print("Computer 1 wins!")
        computer_1_score += 1
        
    #Otherwis, computer 2 wins
    else:  
        print ("Computer 2 wins!")
        computer_2_score += 1

    
    games_played += 1


    #Print current score
    print(f"\nScoreboard: Computer 1 = {computer_1_score}, Computer 2 = {computer_2_score}\n")
    print(f"Games played = {games_played} \n")
from random import randint

# Create a list of play options
tim = ["Stone", "Paper", "Scissors"]

# Set player and computer scores to 0
player_score = 0
computer_score = 0

# Game loop
while True:
    # Assign a random play to the computer
    computer = tim[randint(0, 2)]

    # Get the player's move
    player = input("What's your play? Type: Stone, Paper, or Scissors? ('stop' to quit game) ")

    # Check if the player wants to quit
    if player.lower() == 'stop':
        break

    # Check the outcome of the game
    if player == computer:
        print("It's a tie!")
    elif player == "Stone":
        if computer == "Scissors":
            print("Nice choice, you win!", player, "smashes", computer)
            player_score += 1
        else:
            print("Sorry, you lose!", computer, "covers", player)
            computer_score += 1
    elif player == "Paper":
        if computer == "Stone":
            print("Good play, you win!", player, "covers", computer)
            player_score += 1
        else:
            print("Better luck next time, you lose!", computer, "cuts", player)
            computer_score += 1
    elif player == "Scissors":
        if computer == "Paper":
            print("Excellent play, you win!", player, "cuts", computer)
            player_score += 1
        else:
            print("You lose...", computer, "smashes", player)
            computer_score += 1
    else:
        print("That's not a valid play. Please check your spelling!")

    # Display current scores
    print(f"Score - Player: {player_score}, Computer: {computer_score}")

# Final scores after the player quits
print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
print("Thanks for playing! Come back soon!")
from random import randint

#create a list of play options
t = ["Paper", "Stone", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Paper, Stone, Scissors?")
    if player == computer:
        print("Push!")
    elif player == "Paper":
        if computer == "Stone":
            print("You Win!", player, "covers", computer)
        else:
            print("You lost!", player, "gets cut by", computer)
    elif player == "Stone":
        if computer == "Scissors":
            print("You Win!", player, "smashes", computer)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Stone":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "gets cut by", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but I want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

#create a list of play options
t = ["Stone", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Stone, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Stone":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Stone":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "gets cut by", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but I want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
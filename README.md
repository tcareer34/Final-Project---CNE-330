Tim Nguyen
CNE 330
Final Project: 
Paper, Stone, Scissors Game 

Step-by-Step Explanation of the Game Logic:

The code requires Python. Pycharm IDE is recommended, but not required.

Python 3 and recommended PyCharm IDE

Importing the Necessary Function: First, I imported the randint function from the random module. This is how my computer opponent will randomly select its move.

Defining the Play Options: I created a list called t that holds the three possible moves:  "Rock", "Paper", and "Scissors". These are the choices both I and the computer can make during the game.

Setting Up the Players: Next, I set up the two players: the computer and myself. I assign a random move to the computer by using randint(0, 2) to select a number between 0 and 2.

The reason for this range (0, 2) is that computers count starting from 0. So, the list t has:

"Rock" at index 0,
"Paper" at index 1,
"Scissors" at index 2.

Waiting for My Move: Unlike playing with friends in person, the computer makes its move first and waits for me to decide mine. The computer doesn’t cheat or change its move after making it. Initially, I set the player variable to False, meaning the game is waiting for me to make my move.

Making My Move and the Game Loop: Once the while loop starts, the computer waits for me to make my move. After I enter my choice, the value of the player variable changes from False to True. I use the input() function to capture my choice and assign it to the player variable.

Determining the Outcome: I use nested if, elif, and else statements to check all possible outcomes:

Win, Lose, or Tie: Based on my choice and the computer’s move, the program prints a message indicating whether I win, the computer wins, or if it’s a tie.

Error Handling: I use else at the end to catch any invalid inputs. If I enter something other than "Rock", "Paper", or "Scissors", the program will print an error message.

Restarting the Game: After each round, I reset the player variable to False so the game can start over, allowing me to play again if I wish. The game continues in a loop until I decide to stop.

The location of my code is shared on GitHub: https://github.com/tcareer34/Paper_Rock_Scissors_Game/blob/main/Final-Project.py
This code was cited from: https://careerkarma.com/blog/python-projects-beginners/

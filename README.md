# Final Project:  Stone, Paper, Scissors Game

### Tim Nguyen
**Course:** CNE 330

---

## **Game Overview:**
The Stone, Paper, Scissors game is a classic hand game recreated in Python. The project includes game logic for determining winners, handling ties, tracking scores, and a fun win-streak feature.

## **Game Logic Explained:**

1. **Importing the Required Function:**
   - The `randint` function from Python's `random` module allows the computer to randomly select its move.

2. **Defining Play Options:**
   - The list `a` includes the three possible moves—Stone, Paper, and Scissors—which both the player and computer choose from during the game.

3. **Setting Up the Players:**
   - The computer’s move is assigned using `randint(0, 2)`, where:
     - "Stone" is at index 0
     - "Paper" is at index 1
     - "Scissors" is at index 2

4. **Waiting for Player's Move:**
   - Initially, `player` is set to `False` to indicate the game is waiting for input. The computer won’t change its move after selection.

5. **Game Loop and Player Move:**
   - Inside the `while` loop, the `input()` function collects the player’s choice, and `player` changes to `True` after a move is entered.

6. **Outcome Determination:**
   - Using `if-elif-else` statements, the program compares the player’s choice with the computer’s to declare a win, loss, or tie.

7. **Tracking Wins:**
   - The game tracks the player's and the computer's scores throughout the game. Each win increments the player’s or computer’s score, and the current score is displayed after every round.
   - A message will be displayed if the player achieves a win streak, such as "You're on fire!" if the player wins three games in a row.

8. **Error Handling:**
   - An `else` statement catches any invalid inputs, displaying an error if the input doesn’t match "Stone," "Paper," or "Scissors."

9. **Restarting the Game:**
   - After each round, `player` resets to `False`, allowing the game to loop for additional rounds or exit as desired.

## **Code Repository Location**
My project’s code is available on [GitHub](https://github.com/tcareer34/Final-Project---CNE-330).
Please use Pycharm to open the Final-Project.py code.
To view my presentation video, please download the video1531690495.mp4 and play it using your Window's Media Player.

## **Project Source and Inspiration**
The concept of the game was adapted from Career Karma's beginner Python projects guide.
For more details, refer to this [inspired code](https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/).



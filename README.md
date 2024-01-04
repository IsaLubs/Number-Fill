# Number Fill 

- This is a game where players must fill a grid with numbers in a sequence. Players can only place a number next to the  previous number and in the adjacent cell of the  previous number. The game ends when the grid is completely filled.

![2](https://github.com/IsaLubs/Number-Fill/assets/147058041/968e3b8c-ba1c-4a87-88cf-8cd96dbfdd53)

# How to Play

### Starting the Game.
- After installing and running the game, you will be prompted to enter a number between 2 and 25. This number will be the first number placed on the grid.
### Placing Numbers.
- Placing Numbers**: You can only place a number next to the previous number and in the adjacent cell of the previous number. Try to create a sequence of numbers across the grid.
### Game Controls.
While playing, you can use the following controls:
 - Type 'S' to save the current game state.
 - Type 'U' to undo the last move.
 - Type 'R' to reset the game.
 - Input coordinates to place a number on the grid.
### Winning the Game.
- The game ends when the grid is completely filled with numbers in a sequence. Congratulations, you've won!
Remember, the goal of the game is to fill the entire grid with numbers in a sequence. Good luck and enjoy the game!


# Features
### Save and Load Game State.
- You can save your current game state at any time by typing 'S'. This allows you to resume your game later from exactly where you left off.
  ![1](https://github.com/IsaLubs/Number-Fill/assets/147058041/72d20da3-81eb-480e-bcff-906d6ad5a656)
### Undo Last Move.
- If you accidentally place a number incorrectly, you can undo your last move by typing 'U'. This gives you another chance to correct your mistake.
### Reset Game.
- If you want to start over, you can reset the game by typing 'R'. This clears the grid and lets you start a new game.
### Input Coordinates
- You can directly input coordinates to place a number on the grid. This gives you precise control over where you want to place your numbers.
### Deployable to Heroku
- This game can be easily deployed to Heroku. This makes it accessible to anyone, anywhere, at any time.

   These features enhance the gameplay experience and make the game more engaging and fun to play.

![Number fil README](https://github.com/IsaLubs/Number-Fill/assets/147058041/87be1a0d-d706-4421-95a7-0e2d1dfaed4f)


# Data Models
- The game uses a dictionary to store the game state, which includes the grid, memory, position, and already placed positions. The grid is a 2D list representing the game board. The memory is a list storing all the numbers placed so far. The position is a list storing the positions of the numbers placed. The already placed positions is a list storing the positions that have been filled with numbers.

# Testing
I have manually tested this project by doing the following.
- Given invalid inputs: Strings when numbers are expected, out of bounds inputs, same input twice, wrong coordinates
- Tested in my local terminal and the Code Institute Heroku terminal
![t](https://github.com/IsaLubs/Number-Fill/assets/147058041/d4c0eaeb-ded3-4a13-ad22-f82fb97a9e97)


# Bugs
- No bugs were encountered.

# Validator Testing 
- PEP8
   * No errors were returned from PEP8oline.com
# Deployment
- This project was deployed using Code Institute's mock terminal for Heroku.
### Steps for deployment
   * Fork or clone this repository
   *  Create a new Heroku app
   * Set the build back to Python and NodeJS in that order
   * Link the Heroku app to the repository
   * Click on Deploy

# Credits
- Code Institute for the deployment terminal

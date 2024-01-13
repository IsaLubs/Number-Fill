# Number Fill 
[Visit the website here](https://numberfill-a461588b1f61.herokuapp.com/)

This is a game where players must fill a grid with numbers in a sequence. Players can only place a number next to the  previous number and in the adjacent cell of the  previous number. The game ends when the grid is completely filled.

![g](https://github.com/IsaLubs/Number-Fill/assets/147058041/08c009a9-c5eb-4598-a75b-342991283929)

## Repository
https://github.com/IsaLubs/Number-Fill

## UX & Design

### User Stories
As a user,  
* I would like to understand how to play the game with ease.
* I would like to be able to set the difficulty to suit my level.
* I would like feedback on each level while playing the game.
* I would like to see an error message if my guess is invalid and understand why.
* I would like to know the progress of the game while playing the game.
* I would like to have the option to play again or finish the game after each game. 

# How to Play

### Starting the Game.
- After installing and running the game, you will be prompted to enter a number between 2 and 25. This number will be the first number placed on the grid.

  ![1](https://github.com/IsaLubs/Number-Fill/assets/147058041/929fb890-e228-47ff-ba61-74fd1ad11950)
  
### Placing Numbers.
- Placing Numbers**: You can only place a number next to the previous number and in the adjacent cell of the previous number.
  Try to create a sequence of numbers across the grid.
  
  ![2](https://github.com/IsaLubs/Number-Fill/assets/147058041/c5067cde-ff30-4c52-87f3-b0516d121868)

  
### Game Controls.
While playing, you can use the following controls:
 - Type 'S' to save the current game state.
 - Type 'U' to undo the last move.
 - Type 'R' to reset the game.
 - Input coordinates to place a number on the grid.

   ![y](https://github.com/IsaLubs/Number-Fill/assets/147058041/ce3942d6-917f-4f87-b1d8-c8f2a248bcb3)
### Winning the Game.
- The game ends when the grid is completely filled with numbers in a sequence. Congratulations, you've won!
Remember, the goal of the game is to fill the entire grid with numbers in a sequence. Good luck and enjoy the game!


# Features
### Save and Load Game State.
- You can save your current game state at any time by typing 'S'. This allows you to resume your game later from exactly where you left off.
 
  ![p](https://github.com/IsaLubs/Number-Fill/assets/147058041/f01530f6-49d6-41a7-98f6-bd680846272d)

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

# Technologies Used
### Main Language 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used to build the contents and structure of the game. 

### Tools used for Developing the Game
* [Gitpod](https://www.gitpod.io/) was used to create, edit and preview the codes during the development.
* [Git](https://git-scm.com/) was used for version control and tracked changes in the codes.
* [GitHub](https://github.com/) was used to store the repository and the codes.
* [Heroku](https://www.heroku.com) was used to deploy the application.

### Tool used for Validating the Codes
* [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate Python codes. 

### Other Online Resources used
* [Figma](https://www.figma.com) was used to generate the flow chart to plan the logic flow of the game.
* [ScreenToGif](https://www.screentogif.com/) was used to create the GIF images.
* [Compressor.io](https://compressor.io/) was used to compress the images used in the README file.
* [Grammarly](https://app.grammarly.com/) was used to remove grammatical and typographical errors in the game and README file.

# Testing
I have manually tested this project by doing the following.
- Given invalid inputs: Strings when numbers are expected, out of bounds inputs, same input twice, wrong coordinates
- Tested in my local terminal and the Code Institute Heroku termina

# Bugs
- No bugs were encountered.

# Validator Testing 
- PEP8
   * No errors were returned from PEP8oline.com

![t](https://github.com/IsaLubs/Number-Fill/assets/147058041/d4c0eaeb-ded3-4a13-ad22-f82fb97a9e97)
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

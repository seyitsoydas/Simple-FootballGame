
# Football Game (Python)

This is a simple football game application written in Python. In this game, players try to score goals by controlling their goalkeeper with the mouse while the ball moves around the field. The game is played against the computer, and the objective is to score 3 goals before time runs out. If 3 goals are scored, the player wins, otherwise, the player loses.

## Features

- **Football Field**: The playing field contains the player's and opponent's goalkeepers, as well as the area where the ball moves.
- **Ball Movement**: The ball moves randomly across the field and bounces off the boundaries when it hits them.
- **Goalkeeper Control**: The left goalkeeper is controlled by the player using the mouse, while the right goalkeeper moves automatically up and down.
- **Score Tracking**: The score is tracked based on goals scored by either goalkeeper.
- **Timer**: The game runs for 60 seconds. If the player scores 3 goals within this time, they win; otherwise, they lose.
- **Basic Graphics**: Simple shapes are used for visualization through the `graphics` module.

## Requirements

- Python 3.x
- `graphics` module

## Installation

1. Ensure that Python 3.x is installed on your system.
2. Install the `graphics` module by running the following command in your terminal or command prompt:

   ```
   pip install graphics
   ```

3. Run the game by executing the `futbol_oyunu.py` file.

## How to Play

1. When the game starts, the football field appears with the player's and opponent's goalkeepers.
2. Control the left goalkeeper by moving the mouse up and down.
3. The objective is to score goals by getting the ball into the opponent's goal while preventing the opponent from scoring.
4. If the timer reaches 60 seconds, the player who has scored 3 goals wins. If no one reaches 3 goals, the game ends in a loss for the player.

## Game Start

At the start of the game, a text with game instructions appears on the screen. The user can start the game by clicking anywhere on the screen after reading the instructions.

## Main Functions

- `futbolsahasi(canvas)`: Creates the visual elements of the football field.
- `main_game(canvas, TIME, PIECE)`: Manages the main game loop, including the ball's movement, goalkeepers' actions, and the timer.
- `giris_ekrani(canvas)`: Displays the information screen at the beginning of the game.
- `main()`: Initializes the game, creates the football field, and starts the main game loop.

## Game Flow

1. The user clicks to start the game, which triggers the display of instructions.
2. Once the game starts, the user tries to score goals by controlling the ball and preventing the opponent from scoring.
3. The game continues, updating the ball's movement and the goalkeepers' positions.
4. The game ends when the timer reaches 0, or when one of the goalkeepers scores 3 goals.

## License

The software and tools used in this project are open-source. This project is free for personal use. Please use the game code for personal development or educational purposes.

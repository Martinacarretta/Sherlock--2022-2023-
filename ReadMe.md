# Sherlocked

This project is a Python program implementing a game called "Sherlocked" where you, playing as Sherlock Holmes, have to save the city of London from explosive hostages set up by Moriarty. The game involves a grid where you need to locate the hostages before they explode. The game generates a text file containing the solution, including the grid, the board, and the result of the game.

## How to Play

1. Run the Python script `Sherlocked.py`.
2. Enter the size of the grid `N`.
3. Enter the number of explosive hostages `M`.
4. The program will create the grid and randomly place the hostages.
5. You, as Sherlock Holmes, will try to locate the hostages by selecting cells on the grid. You have a limited number of attempts.
6. If you successfully locate all the hostages, you save London. Otherwise, the city will be destroyed.

## Functions

### Exercise 1
`Lets_Play_Shecklocked()`: Displays instructions for playing the game.

### Exercise 2
- `create_subgrid_to_check(i, j)`: Creates a subgrid to check if placing a bomb at coordinates `(i, j)` is valid.
- `isValid(grid, i, j)`: Checks if placing a bomb at coordinates `(i, j)` is a valid move.

### Exercise 3
`PlantExplosives(m)`: Places `m` explosive hostages on the grid.

### Exercise 4
- `place_bombs(possible_positions, m)`: Places `m` explosive hostages on the grid.
- `assign_next_to_bombs(grid, i, j)`: Assigns numbers indicating the number of bombs surrounding a cell.

### Exercise 5
`Play_Sherlock()`: Allows the player to try to locate the hostages.

## Main Program Flow
1. Displays instructions.
2. Asks for the size of the grid and the number of explosive hostages.
3. Checks if it's possible to place the specified number of hostages.
4. If possible, the hostages are placed, and numbers indicating the number of surrounding bombs are assigned.
5. The player attempts to locate the hostages.
6. If successful, a success message is displayed, and the solution is written to a text file. Otherwise, an error message is shown.


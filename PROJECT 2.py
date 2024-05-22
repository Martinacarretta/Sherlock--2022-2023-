#This group is composed by Martina Carretta (niu:1673930) and Meritxell Carvajal (niu: 1671647)

import numpy as np
import random

### EXERCISE 1 ###
def Lets_Play_Shecklocked():
    print('''Welcome to the game “Sherlocked”. You will need to save the city of
London from Moriarty’s “explosive hostages”. The program will receive
as input:
- N, defining the size of the square grid.
- M, defining the number of hostages wearing explosive vests.
The program will create the NxN grid and find the place for the M
explosive hostages. Afterwards, the NxN board will be created and
Sherlock will try to find the location of the hostages by selecting
cells. Sherlock has a limited time to save the city of London from the
explosions, so he can only check a maximum of 2*M cells.
The program will generate a txt file containing the solution (the grid,
the board, and the result of the game).''')
    print()

### EXERCISE 2 ###
def create_subgrid_to_check (i, j): #used in exercise 2 and in exercise 4
    if i == 0: #these ifs are in case the coordinates are placed in a border
        inii = i
        finii = i+2
    elif i == n-1:
        inii = i-1 
        finii = n 
    else:
        inii = i-1
        finii = i+2

    if j == 0:
        inij = j
        finij = j+2
    elif j == n-1:
        finij = n
        inij = j-1 
    else:
        inij = j-1
        finij = j+2
    return inii, inij, finii, finij

def isValid (grid, i, j):
    if grid[i, j] == -1: #in case there already is a bomb
        return False
    else:
        #these ifs are in case the coordinates are placed in a border
        inii, inij, finii, finij = create_subgrid_to_check (i, j) #we call the function to create a subgrid to check it it's valid
        grid2 = grid [inii:finii, inij:finij] #create a 3x3 grid to check if it's valid
        if -1 in grid2: #if there is a -1, there is a bomb in the area of the coordinate, so it's not valid to place a bomb there
            return False
        else:
            return True
    
### EXERCISE 3 ###
def PlantExplosives(m):
    if m == 0:
        return True
    else:
        x = []
        y = []
        for i in range (0, n, 1): # creating possible 'moves'
            x.append(i)
            y.append(i)
        for i in range(len(x)):
            for j in range(len(y)):
                if isValid(grid, x[i], y[j]): # checking is it's valid
                    grid[x[i], y[j]] = -1
                    if PlantExplosives (m-1): # recursive
                        return True
                    else:
                        grid[x[i], y[j]] = 0 #backtracking
                    
        return False

### EXERCISE 4 ###
def place_bombs(possible_positions, m):
    if m == 0: #base case
        return True
    else: #generic case
        for i in range(0, len(possible_positions), 1): #begin assigning bombs
            if isValid(grid, possible_positions[i][0], possible_positions[i][1]): # checking is it's valid
                grid [possible_positions[i][0], possible_positions[i][1]] = -1 #placing the bomb
                if place_bombs (possible_positions, m-1): # recursive
                    return True
                else:
                    grid [possible_positions[i][0], possible_positions[i][1]]  = 0 #backtracking

def assign_next_to_bombs (grid, i, j): #to place the numbers to indicate how many there are around
    #these ifs are in case the coordinates are placed in a border
    inii, inij, finii, finij = create_subgrid_to_check (i, j) #we call the function to create a subgrid to check how many bombs there are
    grid2 = grid [inii:finii, inij:finij] #create a 3x3 grid to check if it's valid
    count_of_bombs = 0
    sizei = finii-inii #calculate how many rows do we need to check
    sizej = finij-inij #calculate how many columns do we need to check
    for i in range (0, sizei, 1):
        for j in range (0, sizej, 1):
            if grid2[i][j] == -1: #checking each cell
                count_of_bombs += 1 #updating in case there is a bomb
    return count_of_bombs #returning the number of bombs there are next to the cell

def Assign_numbers_to_grid(): #taking into account plantexplosives returns true 
    possible_positions = [] #creating al possible positions in grid
    for i in range (n):
        for j in range (n):
            possible_positions.append([i, j]) 
    random.shuffle(possible_positions) #random position
    place_bombs(possible_positions, m) #call function to place -1
    #Now we have to place the numbers indicating if there is a bomb
    for i in range (0, n, 1):
        for j in range (0, n, 1):
            if grid[i][j] == 0: #if there is not a bomb, we need to count how many bombs it's touching
                grid[i][j] = assign_next_to_bombs (grid, i, j) #counting of bombs
    #print(grid)
    
### EXERCISE 5 ###
def Play_Sherlock():
    board = np.full((n, n), 9) #create a board full of 9 of the same size as the board
    M = m*2 #we calculate how many tries does sherlock have
    tries = 0 #we set a counter of tries to 0
    found = 0 #we set a counter of found to 0
    while tries < M and found < m:
        x = int(input('Write the position (x): ')) #asking input of coordinates
        y = int(input('Write the position (y): '))
        while x >= n or y >= n: #in case the coordenates are out of range
            print('The position entered is not in the grid.')
            x = int(input('Write the position (x): ')) #asking input of coordinates
            y = int(input('Write the position (y): '))
        board [x, y] = grid [x, y] #updating board 
        tries += 1 #update tries
        print(board) #showing the move made
        if grid [x, y] == -1: #in case there is a bomb
            found += 1 #un hostage has been found
    if found == m: #success
        return True, board
    else: #failure
        return False, board
        
    
### MAIN ###
Lets_Play_Shecklocked() #printing of the text
n = int(input('Introduce de size: ')) #asking size of matrix
m = int(input('Introduce the number of expplosive hostages: ')) #asking number of hostages / bombs
grid = np.full((n, n), 0) #inicialization of grid with 0's
if PlantExplosives(m): #if there is a way of puting m bombs in a nxn matrix, we beggin
    grid = np.full((n, n), 0) #reseting grid to 0
    Assign_numbers_to_grid() #assigning numbers next to the bombs
    found, board = Play_Sherlock() #calling to play Sherlock and saving the success/failure and the board
    if found:
        message = 'Sherlock saved London!'
    else:
        message = 'London has been destroyed!'
    print(message) #printing of whatever message we got
    
    doc = open ('solution_'+ str(n) + '_' + str(m) + '.txt', 'w') #writing in document
    for i in range (0, n, 1): #writing in document the grid
        for j in range (0, n, 1):
            doc.write (str(grid[i][j]) + ' ')
        doc.write('\n')
    doc.write('\n')
    
    for i in range (0, n, 1): #writing in document the board
        for j in range (0, n, 1):
            doc.write (str(board[i][j]) + ' ')
        doc.write('\n')
    doc.write('\n')
    
    doc.write (message) #writing in document the message
    doc.close() #closing the doc
    
else: #in case there is no possibility of putting m bombs in a nxn matrix
    print('Error: It is not possible to place ', str(m), ' hostages in the grid.')
# Level 1
import random
import pickle


def save_game(grid, memory, pos, alread_pos):
    game_state = {
        'grid': grid,
        'memory': memory,
        'pos': pos,
        'alread_pos': alread_pos
    }
    with open('game_state.pkl', 'wb') as f:
        pickle.dump(game_state, f)

        def load_game():
    with open('game_state.pkl', 'rb') as f:
        game_state = pickle.load(f)
    return game_state['grid'], game_state['memory'], game_state['pos'], game_state['alread_pos']

def get_adjacent_cells(row, col, grid_size):
    adjacent_cells = []

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 1 <= i <= grid_size and 1 <= j <= grid_size and (i != row or j != col):
                adjacent_cells.append((i, j))

    return adjacent_cells

    def print_Grid(grid):
    if len(grid[0]) == 5:
        print("---------------------")
        for x in grid:
            tmp = [str(y) for y in x]
            tmp = " |".join([" " + y if len(y) == 1 else y for y in tmp])
            print("|" + tmp + " |")
            print("---------------------")
    else:
        print("-----------------------------")
        for x in grid:
            tmp = [str(y) for y in x]
            tmp = " |".join([" " + y if len(y) == 1 else y for y in tmp])
            print("|" + tmp + " |")
            print("-----------------------------")

def game():
    print("Welcome to NUMBER FILL board game")
    print("Rules: ")
    print("1. You can only place a number next to the previous number")
    print("2. You can only place a number in the adjacent cell of the previous number")
    print("3. You can place the number in North, South, East, West North-East, North-West, South-East, South-West")
    print()
    
    
    undo = 5
    grid_size = 5

    
    # Show a 5x5 grid with number 1 randomly placed
    try:
        grid = load_game()[0]
        memory = load_game()[1]
        Pos = load_game()[2]
        alread_pos = load_game()[3]
        successor = memory[-1]

        except:
        
        grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
        
        # Place 1 at a random position and get the position
        x = random.randint(1, grid_size)
        y = random.randint(1, grid_size)
        print("Current Position: ", x, "," ,y)
        grid[x - 1][y - 1] = 1
        Pos = [(x, y)]
        memory = [1]
        alread_pos = []
        successor = 1

         print_Grid(grid)
    level = True
    while level:

        number = input("\nEnter a number from 2 to 25  or S(save) or U(Undo) or R(Reset): ")
        if number.isdigit():
            number = int(number)
        
            if number - 1 != successor:
                print("Invalid number")
                continue
            
            elif number in memory:
                print("Number already used")
                continue

            else:
                while True:
                    temp = input("Enter the position to place the number: ").split()
                    if len(temp) == 2:
                        x_u = int(temp[0])
                        y_u = int(temp[1])
                        adjacents = get_adjacent_cells(Pos[-1][0], Pos[-1][1], grid_size)

                        if (x_u, y_u) in adjacents:

                            if (x_u, y_u) in alread_pos:
                                print("Already used position")
                                continue
                            else:
                                x = x_u
                                y = y_u
                                grid[x_u - 1][y_u - 1] = number
                                successor = number
                                memory.append(number)
                                alread_pos.append((x, y))
                                Pos.append((x, y))
                                print_Grid(grid)
                                #print(grid)

                                # if no 0 left in the grid
                                flag = True
                                for x in grid:
                                    if 0 in x:
                                        flag = False
                                        break
                                if flag:
                                    print("You won the game")
                                    
                                    while True:
                                        replay =  input("Do You want to  play again (Y/N)?")
                                        if replay == 'Y': 
                                            grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
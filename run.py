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
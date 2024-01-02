import random
import pickle


def save_game(grid, memory, pos, alread_pos):
    g_state = {
        'grid': grid,
        'memo': memory,
        'pos': pos,
        'al_pos': alread_pos
    }
    with open('game_state.pkl', 'wb') as f:
        pickle.dump(g_state, f)


def load_game():
    with open('game_state.pkl', 'rb') as f:
        g_state = pickle.load(f)
    return g_state['grid'], g_state['memo'], g_state['pos'], g_state['al_pos']


def adj_cell(row, col, grid_size):
    adjacent_cells = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            a = 1 <= i <= grid_size
            b = 1 <= j <= grid_size
            if a and b and (i != row or j != col):
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
    print("....NUMBER FILL....")
    print("Rules: ")
    print("1. You can only place a number next to the previous number")
    print("2. You can only place a number")
    print("in the adjacent cell of the previous number")
    print("3. You can place the number in North, South, East,")
    print("West North-East, North-West, South-East, South-West")
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
    except EOFError:
        grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
        # Place 1 at a random position and get the position
        x = random.randint(1, grid_size)
        y = random.randint(1, grid_size)
        print("Current Position: ", x, ",", y)
        grid[x - 1][y - 1] = 1
        Pos = [(x, y)]
        memory = [1]
        alread_pos = []
        successor = 1

    print_Grid(grid)
    level = True
    while level:
        print("Enter a number from 2 to 25  ")
        number = input("or S(save) or U(Undo) or R(Reset): ")
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
                    print("Enter the position to place the number: ")
                    temp = input().split()
                    if len(temp) == 2:
                        x_u = int(temp[0])
                        y_u = int(temp[1])
                        adjacents = adj_cell(Pos[-1][0], Pos[-1][1], grid_size)

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

                                # if no 0 left in the grid
                                flag = True
                                for x in grid:
                                    if 0 in x:
                                        flag = False
                                        break
                                if flag:
                                    print("You won the game")
                                    while True:
                                        print("Do You want to  play again?")
                                        replay = input(" (Y/N) : ")
                                        if replay == 'Y':
                                            g = grid_size
                                            lst = [0 for x in range(g)]
                                            grid = [lst for y in range(g)]
                                            # Place 1 at a random position
                                            x = random.randint(1, grid_size)
                                            y = random.randint(1, grid_size)
                                            print("Current Position: ")
                                            print(x, ",", y)
                                            grid[x - 1][y - 1] = 1
                                            Pos = [(x, y)]
                                            memo = [1]
                                            al_pos = []
                                            successor = 1
                                            save_game(grid, memo, Pos, al_pos)
                                            print_Grid(grid)
                                            game()
                                        elif replay == 'N':
                                            level = False
                                            break
                                        else:
                                            print("Invalid Input")
                                break
                        else:
                            print("Invalid position")

                            print()
                            print_Grid(grid)

                    else:
                        print("Invalid position")

                        print()
                        print_Grid(grid)

        else:
            if number == "S":
                save_game(grid, memory, Pos, alread_pos)
                print("Game saved")
                break
            elif number == "U":
                print("Undo")
                if memory[-1] != 1:
                    undo -= 1
                    successor = memory[-1] - 1
                    memory.pop()

                    grid[Pos[-1][0] - 1][Pos[-1][1] - 1] = 0
                    alread_pos.pop()
                    Pos.pop()
                    print_Grid(grid)
                elif undo == 0:
                    print("No more Rollback left...")
                else:
                    print("Cannot undo anymore")
            elif number == "R":
                g_size = grid_size
                grid = [[0 for x in range(g_size)] for y in range(g_size)]
                # Place 1 at a random position and get the position
                x = random.randint(1, grid_size)
                y = random.randint(1, grid_size)
                print("Current Position: ", x, ",", y)
                grid[x - 1][y - 1] = 1
                Pos = [(x, y)]
                memory = [1]
                alread_pos = []
                successor = 1
                save_game(grid, memory, Pos, alread_pos)
                game()

            else:
                print("Invalid Input")
                print("Please enter a number or S or U for saving or rollback")
                continue


if __name__ == "__main__":
    game()

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



import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    rows, cols = current_board.shape
    updated_board = np.zeros_like(current_board)

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            # Count neighbors
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    live_neighbors += current_board[ni, nj]

            # Apply rules
            if current_board[i, j] == 1:
                if live_neighbors in (2, 3):
                    updated_board[i, j] = 1
            else:
                if live_neighbors == 3:
                    updated_board[i, j] = 1

    return updated_board

def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # Update board
        game_board = update_board(game_board)

        # Display board
        sns.heatmap(
            game_board, cmap='tab20c_r',
            cbar=False, square=True, linewidths=1
        )
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # Pause between steps
        if step + 1 < n_steps:
            time.sleep(pause)

def recursive_game_of_life(board=None, generations=5):
    if board is None:
        board = np.random.randint(2, size=(10, 10))

    print("Generation:")
    print(board, "\n")

    if generations == 0:
        return board
    
    # Compute next generation
    next_board = update_board(board)
    
    # Recursive call
    return recursive_game_of_life(next_board, generations - 1)
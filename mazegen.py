import numpy as np
import random
import matplotlib.pyplot as plt

def generate_maze(width, height):
    # Initialize the maze grid, 0's are walls, 1's are paths
    maze = np.zeros((height, width), dtype=bool)

    # Stack for depth-first search
    stack = []

    # Choose a starting point
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    stack.append((start_x, start_y))
    maze[start_y][start_x] = True

    # Possible movements: up, down, left, right
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while stack:
        x, y = stack[-1]

        # Find possible directions
        possible_directions = []
        for dx, dy in moves:
            nx, ny = x + dx*2, y + dy*2
            if 0 <= nx < width and 0 <= ny < height and not maze[ny][nx]:
                possible_directions.append((dx, dy))

        if possible_directions:
            # Move in a random possible direction
            dx, dy = random.choice(possible_directions)
            maze[y + dy][x + dx] = True
            maze[y + dy*2][x + dx*2] = True
            stack.append((x + dx*2, y + dy*2))
        else:
            # Backtrack if no moves are possible
            stack.pop()

    return maze

def plot_maze(maze):
    plt.figure(figsize=(6, 6))
    plt.imshow(maze, cmap='binary', interpolation='nearest')
    plt.xticks([]), plt.yticks([])  # Hide the axes ticks
    plt.show()

# Generate a 10x10 maze
maze = generate_maze(10, 10)

# Plot the maze
plot_maze(maze)

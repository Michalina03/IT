import random
from characters.basic_character import BasicCharacter


# Generating the maze
def generate_maze(size):
    maze = [["#" for _ in range(size)] for _ in range(size)]

    # Placing the player at the top left corner
    maze[0][0] = "S"

    # Placing the goal at the bottom right corner
    maze[size - 1][size - 1] = "E"

    # Creating obstacles
    obstacles = int(size * size * 0.2)  # 20% of cells will be obstacles
    for _ in range(obstacles):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        maze[x][y] = "X"  # 'X' represents an obstacle

    return maze


# Displaying the maze
def display_maze(maze):
    for row in maze:
        print(" ".join(row))


# Checking player's movement possibilities
def can_move(maze, x, y):
    size = len(maze)
    if 0 <= x < size and 0 <= y < size and maze[x][y] != "X":
        return True
    return False


# Main game function
def maze_game(hero):
    size = 10  # Maze size
    maze = generate_maze(size)
    x, y = 0, 0  # Initial player position

    # Ensure start and end points are present
    maze[0][0] = "S"
    maze[size - 1][size - 1] = "E"

    print("Welcome to the Maze Game!")

    while True:
        display_maze(maze)

        move = input(
            "Enter movement direction (W - up, S - down, A - left, D - right, Q - quit): "
        ).upper()

        if move == "W":
            if can_move(maze, x - 1, y):
                x -= 1
        elif move == "S":
            if can_move(maze, x + 1, y):
                x += 1
        elif move == "A":
            if can_move(maze, x, y - 1):
                y -= 1
        elif move == "D":
            if can_move(maze, x, y + 1):
                y += 1
        elif move == "Q":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid move. Enter W, S, A, D, or Q.")

        if maze[x][y] == "E":
            hero._gold += 150
            print("Congratulations! You reached the goal!")
            break

# Question 1

import matplotlib.pyplot as plt
import numpy as np

# func to load the maze
def load_maze(file_path):
    maze_img = plt.imread(file_path)  # reading the image
    if len(maze_img.shape) == 3:  # converting to grayscale if it's RGB
        maze_img = np.mean(maze_img, axis=2)

    maze = (maze_img < 0.5).astype(int)  # to make sure we get int not a float
    return maze

# func to display the maze
def display_maze(maze, path, visited):
    plt.figure(figsize=(10, 10))  # Set a larger figure size to see details more clearly
    plt.imshow(maze, cmap='binary')  # displaying the maze using a black-and-white colormap

    if visited:  # visited cells in blue
        visited_x, visited_y = zip(*visited)
        plt.scatter(visited_y, visited_x, color='blue', s=10, label='Visited Cells')

    if path:  # the solution path in red
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color='red', linewidth=3, label='Solution Path')  # Increased linewidth for better visibility

    plt.legend()
    plt.title("Maze with Solution Path and Visited Cells")
    plt.show()

# func to check if a move is valid, and has not been visited
def is_valid_move(maze, position, visited):
    x, y = position
    rows, cols = maze.shape
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    if maze[x][y] != 0:
        return False
    if position in visited:
        return False
    return True

# func to find first valid point for start or end
def find_valid_point(maze, search_from='top-left'):
    rows, cols = maze.shape

    if search_from == 'top-left':
        for i in range(rows):
            for j in range(cols):
                if maze[i, j] == 0:
                    return (i, j)
    elif search_from == 'bottom-right':
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if maze[i, j] == 0:
                    return (i, j)

    return None

# backtracking function
def backtracking_func(maze, start, end, visualize=True):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    stack = [start]  # to manage the positions that need to be visited
    visited = set([start])  # track visited
    predecessors = {start: None}  # to keep track of predecessors to reconstruct the path later

    while stack:
        current = stack.pop()

        if current == end:
            if visualize:
                print("Backtracking: Path found!")
                # reconstructing path from end to start using predecessors
                path = []
                while current is not None:
                    path.append(current)
                    current = predecessors[current]
                path.reverse()  # reversing the path to get it from start to end

                display_maze(maze, path, visited)
            return True

        # Checking directions around
        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)
            if is_valid_move(maze, next_pos, visited):
                stack.append(next_pos)  # Adding valid move to stack
                visited.add(next_pos)  # Marking it as visited
                predecessors[next_pos] = current  # Track predecessor to reconstruct path later

    if visualize:
        # If no path is found, display the visited cells
        print("Backtracking: No path found.")
        display_maze(maze, [], visited)
    return False

# Las Vegas BFS function with path tracking
def las_vegas_func(maze, start, end, max_steps=400, visualize=True):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = [start]  # to manage positions to visit
    visited = set([start])  # to keep track of visited
    predecessors = {start: None}  # to keep track of the path
    step_count = 0

    while queue and step_count < max_steps:
        current = queue.pop(0)  # taking the current position from the front of the list (queue)

        # the end
        if current == end:
            if visualize:
                print("Las Vegas: Path found!")
                # Reconstruct path from end to start using predecessors
                path = []
                while current is not None:
                    path.append(current)
                    current = predecessors[current]
                path.reverse()  # Reverse the path to get it from start to end

                display_maze(maze, path, visited)
            return True

        # possible directions
        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)
            if (0 <= next_pos[0] < len(maze)) and (0 <= next_pos[1] < len(maze[0])) and maze[next_pos[0]][next_pos[1]] == 0 and next_pos not in visited:
                queue.append(next_pos)  # adding valid move
                visited.add(next_pos)  # marking it as visited
                predecessors[next_pos] = current  # track predecessor

        step_count += 1

    if visualize:
        # If no path is found within max steps, return False
        print("Las Vegas: No path found after reaching the step limit.")
        display_maze(maze, [], visited)
    return False

# Example usage
file_path = 'maze.png'  # Replace with your file path

try:
    maze = load_maze(file_path)
    print(maze)

    # Find start and end points
    start = find_valid_point(maze, search_from='top-left')
    end = find_valid_point(maze, search_from='bottom-right')

    if start is None or end is None:
        print("Error: Could not find a valid start or end point in the maze.")
    else:
        print(f"Start point: {start}")
        print(f"End point: {end}")

        # Ask user for the approach to use
        choice = int(input(
            "\nChoose the approach:\n1: Backtracking\n2: Las Vegas\nEnter your choice (1 or 2): "))

        if choice == 1:
            print("\nRunning Backtracking...")
            backtracking_func(maze, start, end)
        elif choice == 2:
            print("\nRunning Las Vegas...")
            las_vegas_func(maze, start, end)
        else:
            print("Invalid choice. Please enter 1 or 2.")

except Exception as e:
    print(f"Error: {e}")

# Success rate calculation for 10,000 runs
# success_backtracking = 0
# success_las_vegas = 0
# runs = 10000
#
# # Success rate calculation for 10,000 runs
# success_backtracking = 0
# success_las_vegas = 0
# successful_runs = 0  # Track how many times we were able to run a successful trial with valid start and end points
#
# for i in range(runs):
#     try:
#         print("Running success rate ..")
#         # Load the maze and find start and end points
#         maze = load_maze(file_path)
#         start = find_valid_point(maze, search_from='top-left')
#         end = find_valid_point(maze, search_from='bottom-right')
#
#         # If start or end cannot be found, skip this iteration
#         if start is None or end is None:
#             print(f"Run {i+1}: Start or end point not found. Skipping.")
#             continue
#
#         successful_runs += 1
#
#         # Run Backtracking without visualization
#         if backtracking_func(maze, start, end, visualize=False):
#             success_backtracking += 1
#
#         # Run Las Vegas without visualization
#         if las_vegas_func(maze, start, end, max_steps=400, visualize=False):
#             success_las_vegas += 1
#
#     except Exception as e:
#         # Print the exception if needed for debugging
#         print(f"Run {i+1} failed with error: {e}")
#         continue
#
# # Print the final success rates
# if successful_runs > 0:
#     print(f"Total Successful Runs: {successful_runs}")
#     print(f"Backtracking Success Rate: {(success_backtracking / successful_runs) * 100:.2f}%")
#     print(f"Las Vegas Success Rate: {(success_las_vegas / successful_runs) * 100:.2f}%")
# else:
#     print("No successful runs were completed.")



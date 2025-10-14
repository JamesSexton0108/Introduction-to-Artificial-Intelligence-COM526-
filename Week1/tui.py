from Week1 import pathfinding
import utils
import time


def display_map(maze):
    for line in maze:
        print(line)



def show_path(maze, path):
    grid = [row[:] for row in maze]
    if not path:
        print("No path found.")
        return

    for step_idx, (x, y) in enumerate(path):
        if grid[y][x] not in ("s","g"):
            grid[y][x] = '-'

        display_map(grid)
        print(f"\nStep {step_idx + 1}/{len(path)} at {(x, y)}\n")
    # We are going to show the path the A* took one step at a time
    # for each coordinate provided in path:
        # print the map, showing a dash at that coordinate.
        # However, do not overwrite the start and goal, these should continue to be displayed as 's' and 'g' # DELETE THIS LINE!


if __name__ == "__main__":
    maze_map = utils.import_maze("mazes/maze1.txt")
    start = utils.locate(maze_map, 's')
    goal = utils.locate(maze_map, 'g')
    #display_map(maze_map)
    #print(utils.locate(maze_map, 's'))
    #print(utils.locate(maze_map, 'g'))
    path = pathfinding.a_star(maze_map, start, goal)
    show_path(maze_map, path)

    show_path(maze_map, pathfinding.a_star(maze_map, start, goal))

import pygame
import numpy as np
from sys import exit
import sys
import math
import time
import matplotlib.pyplot as plt


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

def heuristic(start, goal):

    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])

    return math.sqrt(dx**2 + dy**2)


def get_moves() :
    return moves

def trajectory():

    return


def astar(maze, start, end, distance, lw, rw):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    start_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Make sure the robot does not revolve at its own place
    if start_node.position[2] > 360:
        start_node.position[2] = start_node.position[2] - 360
    elif start_node.position[2] < 0:
        start_node.position[2] = 360 - abs(start_node.position[2])
    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        print("##### Exploring #####")

        # Get the current node   Based on the f scores
        open_list.sort(key=lambda x: x.f, reverse=True)
        # Pop current off open list, add to closed list
        current_node = open_list.pop()

        # Found the goal

        if (math.sqrt((current_node.position[0] - end_node.position[0]) ** 2 + (
                current_node.position[1] - end_node.position[1]) ** 2) < 1.5):
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Return reversed path
            return path[::-1], closed_list, open_list
            # Make sure the robot does not revolve at its own place
        if current_node.position[2] > 360:
            current_node.position[2] = current_node.position[2] - 360
        elif current_node.position[2] < 0:
            current_node.position[2] = 360 - abs(current_node.position[2])
        closed_list.append(current_node)

        # Generate children
        children = []
        for new_position in get_moves(current_node.position[2], lw, rw):
            # Get node position
            node_position = trajectory(current_node.position[0], current_node.position[1], current_node.position[2],new_position[0], new_position[1])
            print(node_position)
            # check within range
            if node_position[0] > 10 or node_position[0] < 0 or node_position[1] > 10 or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            tempx = node_position[0]
            tempy = node_position[1]

            if obstacle_test(tempx, tempy, distance) != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            new_node.g = current_node.g + 1
            new_node.f = new_node.g + heuristic(end, new_node.position)
            # Append
            if new_node.position[2] > 360:
                new_node.position[2] = new_node.position[2] - 360
            elif new_node.position[2] < 0:
                new_node.position[2] = 360 - abs(new_node.position[2])
            children.append(new_node)

        # Loop through children
        for neighbour in children:

            if [int(neighbour.position[0]), int(neighbour.position[1]),
                neighbour.position[2]] in closed_list:
                continue

            temp = [[int(items.position[0]), int(items.position[1])] for items in open_list]
            # check if child in openset
            if [int(neighbour.position[0]), int(neighbour.position[1])] in temp:
                # Make sure the robot does not revolve at its own place
                if neighbour.position[2] > 360:
                    neighbour.position[2] = neighbour.position[2] - 360
                elif neighbour.position[2] < 0:
                    neighbour.position[2] = 360 - abs(neighbour.position[2])
                # swap child if present in openlist
                for i in range(len(open_list)):
                    if open_list[i].position == neighbour.position:
                        dis1 = heuristic(open_list[i].parent.position, start_node.position)
                        dis2 = heuristic(neighbour.parent.position, start_node.position)
                        if dis1 > dis2:
                            open_list[i].parent = neighbour.parent
                            open_list[i].f = neighbour.f
            else:
                # Make sure the robot does not revolve at its own place
                if neighbour.position[2] > 360:
                    neighbour.position[2] = neighbour.position[2] - 360
                elif neighbour.position[2] < 0:
                    neighbour.position[2] = 360 - abs(neighbour.position[2])

                neighbour.parent = current_node
                open_list.append(neighbour)


def obstacle_test(x, y, distance):

    return index


def obstacle(x, y, distance):
    index = 0

    if ((x ** 2) + (y ** 2) - 1) <= 0:
        index = 1
    # Upper right circle
    if ((x - 2) ** 2) + ((y - 3) ** 2) - 1 <= 0:
        index = 1
    # Lower right circle
    if ((((x - 2) ** 2)) + ((y + 3) ** 2) - 1) <= 0:
        index = 1
    # Lower left circle
    if (((x + 2) ** 2)) + ((y + 3) ** 2) - 1 <= 0:
        index = 1

    return index


def obstacle_plot(x, y):
    index = 0

    if ((x ** 2) + (y ** 2) - 1) <= 0:
        index = 1
    # Upper right circle
    if ((x - 2) ** 2) + ((y - 3) ** 2) - 1 <= 0:
        index = 1
    # Lower right circle
    if ((((x - 2) ** 2)) + ((y + 3) ** 2) - 1) <= 0:
        index = 1
    # Lower left circle
    if (((x + 2) ** 2)) + ((y + 3) ** 2) - 1 <= 0:
        index = 1

    return index


def plotPygame(new_endgoal, visited, openList):


    pygame.quit()


def main():
    print("Enter robot parameters")
    radius = int(input("radius =  "))
    clearance = int(input("clearence =  "))
    distance = radius + clearance
    print("Enter initial node cordinates")
    xi = int(input("x =  "))
    yi = int(input("y =  "))
    theta = int(input("angle= "))

    print("Enter goal node cordinates")
    xg = int(input("x =  "))
    yg = int(input("y =  "))

    # step = int(input("Step Size (between 1 and 10) =  "))

    print("wheel RPM's")
    lw = int(input("left wheel velocity"))
    rw = int(input("right wheel velocity"))

    start = [xi, yi, theta]
    goal = (xg, yg)

    maze = [[0] * 10 for i in range(10)]
    print("here")



    for i in range(0, 10, 1):
        for j in range(0, 10, 1):
            c = obstacle(i - 5, j - 5, distance)
            if c != 1:
                maze[i][j] = 1

    arr = np.array(maze)
    x, y = arr.nonzero()
    plt.scatter(x, y, c=arr[x, y], s=100, cmap='hot', marker='s')
    plt.colorbar()
    plt.show()

    if (obstacle(goal[0], goal[1], distance) == 1):
        sys.exit("Goal node in obstacle")
    if (obstacle(start[0], start[1], distance) == 1):
        sys.exit("Goal node in obstacle")

    start = [xi + 5, yi + 5, theta]
    goal = (xg + 5, yg + 5)

    begin = time.time()
    path, explored_nodes, openList = astar(maze, start, goal, distance, lw, rw)
    print(path)
    end = time.time()
    print(end - begin)

    plotPygame(path, explored_nodes, openList)


if __name__ == '__main__':
    main()

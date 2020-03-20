# Author Shivam Akhauri, Raghav Aggarwal
import pygame
import numpy as np
from sys import exit
import sys
import math


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
    return dx ** 2 + dy ** 2


def get_moves(step):
    moves = [(0, -1 * step), (0, 1 * step), (-1 * step, 0), (1 * step, 0),
             (math.cos(math.pi / 6) * step, math.sin(math.pi / 6) * step), (math.cos(math.pi / 3) * step, math.sin(
            math.pi / 3) * step)]
    return moves


def astar(maze, start, end, distance, step):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    start_node.f = heuristic(start_node.position, end_node.position)

    # Initialize both open and closed list
    # Initialize both open and closed list
    open_list = []
    closed_list = []
    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node   Based on the f scores
        # Get the current node   Based on the f scores
        current_node = open_list[0]
        open_list.sort(key=lambda x: x.f, reverse=True)
        current_node = open_list.pop()

        # Pop current off open list, add to closed list

        # Found the goal
        if (math.sqrt((current_node.position[0] - end_node.position[0]) ** 2 + (
                current_node.position[1] - end_node.position[1]) ** 2) < 1.5):
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path



    while len(open_list) > 0:


            return path[::-1]








def obstacle(x, y, distance):
    index = 0
    # circle
    if ((x - 225) ** 2) + ((y - 150) ** 2) - ((25 + distance) ** 2) <= 0:
        index = 1
    #  ellipse200
    if ((x - 150) / (40 + distance)) ** 2 + ((y - 100) / (20 + distance)) ** 2 - 1 <= 0:
        index = 1
    # quad
    if (y - (3 / 5) * (x + distance) + ((475 / 5) - distance) <= 0) and (
            y - (3 / 5) * (x - distance) + (625 / 5) + distance >= 0) and (
            y + (3 / 5) * (x + distance) - (725 / 5) + distance >= 0) and (
            y + (3 / 5) * (x - distance) - (875 / 5) - distance <= 0):
        index = 1
    # poly
    if (y - 13 * (x + distance) + 140 - distance <= 0) and (y - 185 - distance <= 0) and (
            y - (x - distance) - 100 + distance >= 0) and (5 * y - 7 * x - 400 >= 0):
        index = 1
    if (y + (7 / 5) * (x - distance) - (1450 / 5) - distance <= 0) and (
            y - (6 / 5) * (x - distance) - (150 / 5) + distance >= 0) and (
            y + (6 / 5) * (x + distance) - (1050 / 5) + distance >= 0) and (y - (7 / 5) * x - (400 / 5) <= 0):
        index = 1
    # rect
    if (y - 1.732 * (x + distance) - 15.456864 - distance <= 0) and (
            y + 0.577 * (x - distance) - 96.382696 - distance <= 0) and (
            y - 1.732 * (x - distance) + 134.54 + distance >= 0) and (
            y + 0.577 * (x + distance) - 84.815 + distance >= 0):
        index = 1
    return index







def plotPygame(new_endgoal, visited, resolution=1):




    pygame.quit()


def main():
    print("Enter robot parameters")
    radius = int(input("radius =  "))
    clearance = int(input("clearence =  "))
    distance = radius + clearance
    print("Enter initial node cordinates")
    xi = int(input("x =  "))
    yi = int(input("y =  "))

    print("Enter goal node cordinates")
    xg = int(input("x =  "))
    yg = int(input("y =  "))

    step = float(input("Step Size (between 0.5 and 10) =  "))

    start = (xi, yi)
    goal = (xg, yg)

    maze = [[0] * 201 for i in range(301)]

    for i in range(301):
        for j in range(201):
            c = obstacle(i, j, distance)
            if c == 1:
                maze[i][j] = 1

    if (obstacle(goal[0], goal[1], distance) == 1 or obstacle(start[0], start[1], distance)):
        sys.exit("Either goal node or start node lies inside obstacle or outside the workspace")
    path = astar(maze, start, goal, distance, step)

    plotPygame(path, path, resolution=1)


if __name__ == '__main__':
    main()
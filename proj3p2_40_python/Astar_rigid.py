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

    return dx ** 2 + dy ** 2


def get_moves(step):
    return moves


def astar(maze, start, end, distance, step):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""


    # Loop until you find the end
    while len(open_list) > 0:


            return path[::-1]  # Return reversed path








def obstacle(x, y, distance):
    index = 0
    # circle

        index = 1
    #  ellipse200

        index = 1
    # quad

        index = 1
    # poly

        index = 1

        index = 1
    # rect

        index = 1
    return index


def obstacle_plot(x, y):
    index = 0
    # circle

        index = 1
    #  ellipse200

        index = 1
    # quad

        index = 1
    # rect


        index = 1
    # poly

        index = 1
    return index


def plotPygame(new_endgoal, visited, resolution=1):
    index = 1
    # read the obstacles and fill it in the pygame



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






if __name__ == '__main__':
    main()
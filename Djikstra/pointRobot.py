#!/usr/bin/env python
# coding: utf-8
import pygame
import numpy as np
from sys import exit
import math


class Djik():
    def __init__(self, resolution, previousNode, endgoal):
        self.resolutionCriteria(resolution)
        self.navigate(previousNode, resolution)
        self.endNavigation(endgoal, resolution)
        self.black = [0, 0, 0]
        self.white = [255, 255, 255]
        self.blue = [0, 0, 255]
        self.green = [0, 255, 0]
        self.index = 2

    def obstacle(self,x,y,resolution):
        index = 0
        if ((x-math.ceil(160/resolution))**2+math.ceil(y-(50/resolution))**2-math.ceil(40/resolution)**2)<=0:
            index=1
        if (x-math.floor(90/resolution) >= 0) and (x - math.floor(110/resolution) <= 0) and (y - math.floor(40/resolution) >= 0) and (y - math.floor(60/resolution) <= 0):
            index=1
        return index
    def navigate(self,previousNode,resolution):
        c=self.obstacle(previousNode[0],previousNode[1],resolution)
        if c ==1 or previousNode[0]  not in range(0,201) or (previousNode[1] not in range(0,101)):
            print("Start point inside obstacle space/not in workspace space.Try again")
            exit()
        else:
            pass

    def endNavigation(self,endgoal,resolution):
        c=self.obstacle(endgoal[0],endgoal[1],resolution)
        if c ==1 or endgoal[0] not in range(0,201) or endgoal[1] not in range(0,101):
            print("Goal point inside obstacle space/not in workspace space.Try again")
            exit()
        else:
            pass
    def resolutionCriteria(self,resolution):
        if (200%resolution)!=0  or(100%resolution)!=0:
            print("Enter an achivable resolution")
            exit()
        else:
            pass


    def child(self, i, in_weight, resolution, visited, nodes, weight_list, root):



    def left(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):

        return currentNode


    def right(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):

        return currentNode


    def up(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):



    def down(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):



    def up_left(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):



    def up_right(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):



    def down_left(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):



    def down_right(self, previousNode, in_weight, resolution, visited, nodes, weight_list, root):



    def possiblePath(self, currentNode, x, y, weight, previousNode, resolution, visited, nodes, weight_list, root):

        return currentNode, weight


    def traverseNode(self, endgoal, visited, new_root, startPointX, startPointY, resolution, new_endgoal):



    def plotPygame(self, resolution, new_endgoal, visited):



        pygame.quit()


    def algo(self, resolution, previousNode, endgoal, startPointX, startPointY):



        print("-------Exploring nodes-----")
        while endgoal not in visited:




def main():
    startPointX = input("input x coordinate for initial node")
    startPointY = input("input y coordinate for initial node")
    endPointX = input("input x coordinate for goal node")
    endPointY = input("input y coordinate for goal node")
    resolution = input("input interger value for resolution")
    resolution = int(resolution)

    previousNode = [float(startPointX) / resolution, float(startPointY) / resolution]
    endgoal = [float(endPointX) / resolution, float(endPointY) / resolution]
    shortestPath = Djik()
    shortestPath.algo()



main()

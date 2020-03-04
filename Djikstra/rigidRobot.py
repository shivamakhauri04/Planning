#!/usr/bin/env python
# coding: utf-8

import pygame
import numpy as np
from sys import exit
import math

radius=input("Please input radius")
c=input("Please input clearance")

class Djik():
    def __init__(self,resolution,previousNode,endgoal):
        self.resolutionCriteria(resolution)  
        self.navigate(previousNode,resolution)
        self.endNavigation(endgoal,resolution)
        self.black = [0, 0, 0]
        self.white = [255, 255, 255]
        self.blue=[0,0,255]
        self.green = [0,255,0]
        self.index=2

    def obstacle(self,x,y,resolution):
        index = 0
        # circle
        if ((x - 225) ** 2) + ((y - 150) ** 2) - ((25 + distance) ** 2) <= 0:
            index = 1
        #  ellipse200
        if ((x - 150) / (40 + distance)) ** 2 + ((y - 100) / (20 + distance)) ** 2 - 1 <= 0:
            index = 1
        # quad
        # if (15*x+25*y - 7375/ <= 0) and (15*x - 25*y + 625/ >= 0) and (15*x +25*y -8125<= 0) and (15*x -25*y + 1375 >= 0):
        #    index=1
        # rect

        # poly
        return index


    def navigate(self,previousNode,resolution):
        c = self.obstacle(previousNode[0], previousNode[1])
        if c == 1 or previousNode[0] not in range(0, 301) or (previousNode[1] not in range(0, 301)):
            print("Start point inside obstacle space or not in workspace space or not a good entry ")
            exit()
        else:
            pass

    def endNavigation(self,endgoal,resolution):
        c = self.obstacle(endgoal[0], endgoal[1])
        if c == 1 or endgoal[0] not in range(0, 301) or endgoal[1] not in range(0, 301):
            print("Goal point inside obstacle space or not in workspace space or not a good entry ")
            exit()
        else:
            pass





    def child(self,i,in_weight,resolution,visited,nodes,weight_list,root):
        self.left(i, in_weight, visited, nodes, weight_list, root)
        self.right(i, in_weight, visited, nodes, weight_list, root)
        self.up(i, in_weight, visited, nodes, weight_list, root)
        self.down(i, in_weight, visited, nodes, weight_list, root)
        self.up_left(i, in_weight, visited, nodes, weight_list, root)
        self.up_right(i, in_weight, visited, nodes, weight_list, root)
        self.down_left(i, in_weight, visited, nodes, weight_list, root)
        self.down_right(i, in_weight, visited, nodes, weight_list, root)

    def left(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0] - 1
        y = currentNode[1]
        weight = 1 + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)
        return currentNode

    def right(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0] + 1
        y = currentNode[1]
        weight = 1 + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)
        return currentNode

    def up(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0]
        y = currentNode[1] + 1
        weight = 1 + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)

    def down(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0]
        y = currentNode[1] - 1
        weight = 1 + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)

    def up_left(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0] - 1
        y = currentNode[1] + 1
        weight = math.sqrt(2) + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)

    def up_right(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0] + 1
        y = currentNode[1] + 1
        weight = math.sqrt(2) + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)

    def down_left(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0] - 1
        y = currentNode[1] - 1
        weight = math.sqrt(2) + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)

    def down_right(self, previousNode, in_weight, visited, nodes, weight_list, root):
        currentNode = previousNode[:]
        x = currentNode[0] + 1
        y = currentNode[1] - 1
        weight = math.sqrt(2) + in_weight
        currentNode, weight = self.possiblePath(currentNode, x, y, weight, previousNode, visited, nodes, weight_list,
                                                root)
        
    def possiblePath(self,currentNode,x,y,weight,previousNode,resolution,visited,nodes,weight_list,root):
        
        return currentNode,weight

    def traverseNode(self,endgoal,visited,new_root,startPointX,startPointY,resolution,new_endgoal):
        while True:
                    
        print("-----------Shortest path by Djikstra-------") 
    

    def plotPygame(self,resolution,new_endgoal,visited):
        

    def algo(self,resolution,previousNode,endgoal,startPointX,startPointY):
        
        

def main():

    startPointX=input("input x coordinate for initial node")
    startPointY=input("input y coordinate for initial node")
    endPointX=input("input x coordinate for goal node")
    endPointY=input("input y coordinate for goal node")
    resolution=input("input interger value for resolution")
    resolution=int(resolution)

    previousNode = [float(startPointX)/resolution,float(startPointY)/resolution]
    endgoal=[float(endPointX)/resolution,float(endPointY)/resolution]
    
    shortestPath = Djik(resolution,previousNode,endgoal)
    shortestPath.algo(resolution,previousNode,endgoal,startPointX,startPointY)
    

main()
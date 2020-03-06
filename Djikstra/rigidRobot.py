#!/usr/bin/env python
# coding: utf-8
import pygame
import numpy as np
from sys import exit
import math

radius  = float(input("Please input radius"))
clearance  =  float(input("Please input clearance"))
distance  = radius+clearance
class Djik():
    def __init__(self,previousNode,endgoal):
        # begin the movement 
        self.navigate(previousNode)
        # last movement taken to reach the goal
        self.endNavigation(endgoal)
        # colour for background
        self.black = [0, 0, 0]
        # colour to show obstacles
        self.white = [255, 255, 255]
        # colour to show shortest path
        self.blue=[0,0,255]
        # colour to show traverse areas in the map
        self.green = [0,255,0]
        # Scaling factor for the pygame env
        self.index=2

    # function to draw the obstacles in the map
    def obstacle(self,x,y):
        index = 0
        # circle
        if ((x-225)**2)+((y-150)**2)-(25**2)<=0:
            index=1
        #  ellipse
        if ((x-150)/40)**2 + ((y - 100)/20)**2 - 1 <=0:
            index=1
        # quad
        if (5*y-3*x+475 <=0) and (5*y-3*x+625>=0) and  (5*y+3*x-725>=0)and  (5*y+3*x-875<=0):
            index=1
        # rect
        if (y-13*x+140 <=0) and (y-185 <=0) and (y-x-100 >=0) and (5*y-7*x-400 >=0) :
            index=1
        if (5*y+7*x-1450<=0) and (5*y-6*x-150>=0) and (5*y+6*x-1050>=0) and (5*y-7*x-400 <=0):
            index = 1
        # polygon
        if(y - 1.732*x - 15.456864 <=0) and (y + 0.577*x - 96.382696 <= 0) and (y- 1.732*x + 134.54 >= 0) and (y + 0.577*x - 84.815 >= 0):
            index = 1
        return index
        
    
    def navigate(self,previousNode):
        c=self.obstacle(previousNode[0],previousNode[1])
        if c ==1 or previousNode[0]  not in range(0,301) or (previousNode[1] not in range(0,301)):
            print("Start point inside obstacle space or not in workspace space or not a good entry ")
            exit()
        else:
            pass

    def endNavigation(self,endgoal):
        c=self.obstacle(endgoal[0],endgoal[1])
        if c ==1 or endgoal[0] not in range(0,301) or endgoal[1] not in range(0,301):
            print("Goal point inside obstacle space or not in workspace space or not a good entry ")
            exit()
        else:
            pass

    # function to move the robot from current position to next position
    def child(self,i,in_weight,visited,nodes,weight_list,root):
        # move left
        self.left(i,in_weight,visited,nodes,weight_list,root)
        # move right
        self.right(i,in_weight,visited,nodes,weight_list,root)
        # move up
        self.up(i,in_weight,visited,nodes,weight_list,root)
        # move down
        self.down(i,in_weight,visited,nodes,weight_list,root)
        # move diagonally left up
        self.up_left(i,in_weight,visited,nodes,weight_list,root)
        # move diagonnaly right up
        self.up_right(i,in_weight,visited,nodes,weight_list,root)
        # move diagonally left down
        self.down_left(i,in_weight,visited,nodes,weight_list,root)
        # move diagonally right down
        self.down_right(i,in_weight,visited,nodes,weight_list,root)

    def left(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]-1
        y=currentNode[1]
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
        return currentNode
    def right(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]+1
        y=currentNode[1]
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
        return currentNode
    def up(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]
        y=currentNode[1]+1
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def down(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]
        y=currentNode[1]-1
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def up_left(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]-1
        y=currentNode[1]+1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def up_right(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]+1
        y=currentNode[1]+1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def down_left(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]-1
        y=currentNode[1]-1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def down_right(self,previousNode,in_weight,visited,nodes,weight_list,root):
        # manipulate x and y according to the movement
        currentNode=previousNode[:]
        x=currentNode[0]+1
        y=currentNode[1]-1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
        
    def possiblePath(self,currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root):
        # if cost of going to the current node is less than the last one, update
        c=self.obstacle(x,y)
        if x in range(0,int(300)+1) and y in range(0,int(200)+1)and c==0:
            currentNode[0]=x
            currentNode[1]=y
            weight=weight
            # update only if the node is unvisited
            if currentNode not in visited:
            # visit if the current node is in the list of nodes to be traversed
                if currentNode in nodes:
                    check=nodes.index(currentNode)
                    weightcheck=weight_list[check]
                    # criteria for the update
                    if weightcheck<weight:
                        pass
                    else:
                        # update the node list and the weight list
                        nodes.pop(check)
                        weight_list.pop(check)
                        root.pop(check)
                        nodes.append(currentNode)
                        weight_list.append(weight)
                        root.append(previousNode)
                else:
                    # update the node list and the weight list
                    nodes.append(currentNode)
                    weight_list.append(weight)
                    root.append(previousNode)
            else:
                pass
        return currentNode,weight

    def traverseNode(self,endgoal,visited,new_root,startPointX,startPointY,new_endgoal):
        while True:
            if endgoal in visited:
                # if endgoal is in the visited stack , means the goal is achieved
                endgoal_index=visited.index(endgoal)
                endgoal=new_root[endgoal_index]
                
                new_endgoal.append(endgoal)
                if endgoal == [float(startPointX),float(startPointY)]:
                    break
                    
        print("-----------Shortest path by Djikstra-------") 
    
    # function toplot on pygame
    def plotPygame(self,new_endgoal,visited):
        # read the obstacles and fill it in the pygame
        observation=[]            
        for i in range(0,301):
            for j in range(0,201):
                c=self.obstacle(i,j)
                if c==1:
                    observation.append([i,j])
                    
        state=np.array(observation)
        observation=state*self.index
        visited_buffer = np.array(visited)
        visited=visited_buffer*self.index
        visited_buffer1 = np.array(new_endgoal)
        new_endgoal=visited_buffer1*self.index
        pygame.init()
        # size of the pygame display
        size = [300*self.index, 200*self.index]
        display = pygame.display.set_mode(size)
        pygame.display.set_caption("Dijkstra Point Robot") 
        clock = pygame.time.Clock()
        done = False

        while not done:
            print ("reached  here####################")
            # fill the background
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:  
                    done = True 
            display.fill(self.black)
            # fill the obstacles
            for i in observation:
                pygame.draw.rect(display, self.white, [i[0],200*self.index-i[1],self.index,self.index])
            pygame.display.flip()
            clock.tick(20)
            # fill the traversed nodes will green
            for i in visited:
                pygame.time.wait(1)
                pygame.draw.rect(display, self.green, [i[0],200*self.index-i[1],self.index,self.index])
                pygame.display.flip()
            # draw the shortest path in blue
            for j in new_endgoal[::-1]:
                pygame.time.wait(1)
                pygame.draw.rect(display, self.blue, [j[0], 200*self.index-j[1], self.index,self.index])
                pygame.display.flip()
                    
            pygame.display.flip()
            pygame.time.wait(15000)
            done = True
            
        pygame.quit()

    def algo(self,previousNode,endgoal,startPointX,startPointY):
        nodes=[]
        nodes.append(previousNode)
        root=[]
        root.append(previousNode)
        weight_list=[]
        # initilize all the weights initially as infinity
        weight=float('Inf')
        weight_list.append(weight)
        new_root=[]
        visited=[]
        new_endgoal=[]
        new_endgoal.append(endgoal)
        counter=0
        new_index=0
        in_weight=0

        print("-------Exploring nodes-----")
        # explore all the nodes
        while endgoal not in visited:
                # begin movement by moving the robot in all directions
                self.child(nodes[new_index],in_weight,visited,nodes,weight_list,root)
                visited.append(nodes[new_index])
                
                new_root.append(root[new_index])
                nodes.pop(new_index)
                weight_list.pop(new_index)
                root.pop(new_index)
                counter=counter+1
                if weight_list != []:
                    # find the minVertex
                    in_weight=min(weight_list)
                    # find the index of the minimum vertex
                    index=weight_list.index(in_weight)
                    new_index=index
        print (len(visited))
        # explre the nodes from the min vertex
        self.traverseNode(endgoal,visited,new_root,startPointX,startPointY,new_endgoal)
        # plot the map
        self.plotPygame(new_endgoal,visited)
        

def main():

    startPointX=input("input x coordinate for initial node")
    startPointY=input("input y coordinate for initial node")
    endPointX=input("input x coordinate for goal node")
    endPointY=input("input y coordinate for goal node")
    previousNode = [float(startPointX),float(startPointY)]
    endgoal=[float(endPointX),float(endPointY)]
    
    shortestPath = Djik(previousNode,endgoal)
    shortestPath.algo(previousNode,endgoal,startPointX,startPointY)
    

main()


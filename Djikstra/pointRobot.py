#!/usr/bin/env python
# coding: utf-8
import pygame
import numpy as np
from sys import exit
import math

class Djik():
    def __init__(self,previousNode,endgoal):
        #self.resolutionCriteria(resolution)  
        self.navigate(previousNode)
        self.endNavigation(endgoal)
        self.black = [0, 0, 0]
        self.white = [255, 255, 255]
        self.blue=[0,0,255]
        self.green = [0,255,0]
        self.index=2

    def obstacle(self,x,y):
        index = 0
        # circle
        if ((x-225)**2)+((y-150)**2)-(25**2)<=0:
            index=1
        #  ellipse200
        if ((x-150)/40)**2 + ((y - 100)/20)**2 - 1 <=0:
            index=1
        # quad
        #if (15*x+25*y - 7375/ <= 0) and (15*x - 25*y + 625/ >= 0) and (15*x +25*y -8125<= 0) and (15*x -25*y + 1375 >= 0):
        #    index=1
        # rect
        
        # poly
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


    def child(self,i,in_weight,visited,nodes,weight_list,root):
        self.left(i,in_weight,visited,nodes,weight_list,root)
        self.right(i,in_weight,visited,nodes,weight_list,root)
        self.up(i,in_weight,visited,nodes,weight_list,root)
        self.down(i,in_weight,visited,nodes,weight_list,root)
        self.up_left(i,in_weight,visited,nodes,weight_list,root)
        self.up_right(i,in_weight,visited,nodes,weight_list,root)
        self.down_left(i,in_weight,visited,nodes,weight_list,root)
        self.down_right(i,in_weight,visited,nodes,weight_list,root)

    def left(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]-1
        y=currentNode[1]
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
        return currentNode
    def right(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]+1
        y=currentNode[1]
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
        return currentNode
    def up(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]
        y=currentNode[1]+1
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def down(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]
        y=currentNode[1]-1
        weight=1+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def up_left(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]-1
        y=currentNode[1]+1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def up_right(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]+1
        y=currentNode[1]+1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def down_left(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]-1
        y=currentNode[1]-1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def down_right(self,previousNode,in_weight,visited,nodes,weight_list,root):
        currentNode=previousNode[:]
        x=currentNode[0]+1
        y=currentNode[1]-1
        weight=math.sqrt(2)+in_weight
        currentNode,weight=self.possiblePath(currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root)
    def possiblePath(self,currentNode,x,y,weight,previousNode,visited,nodes,weight_list,root):
        c=self.obstacle(x,y)
        if x in range(0,int(300)+1) and y in range(0,int(200)+1)and c==0:
            currentNode[0]=x
            currentNode[1]=y
            weight=weight
            if currentNode not in visited:
                if currentNode in nodes:
                    check=nodes.index(currentNode)
                    weightcheck=weight_list[check]
                    if weightcheck<weight:
                        pass
                    else:
                        nodes.pop(check)
                        weight_list.pop(check)
                        root.pop(check)
                        nodes.append(currentNode)
                        weight_list.append(weight)
                        root.append(previousNode)
                else:
                    nodes.append(currentNode)
                    weight_list.append(weight)
                    root.append(previousNode)
            else:
                pass
        return currentNode,weight

    def traverseNode(self,endgoal,visited,new_root,startPointX,startPointY,new_endgoal):
        while True:
            if endgoal in visited:
                #print (endgoal)
                endgoal_index=visited.index(endgoal)
                endgoal=new_root[endgoal_index]
                
                new_endgoal.append(endgoal)
                if endgoal == [float(startPointX),float(startPointY)]:
                    break
                    
        print("-----------Shortest path by Djikstra-------") 
    

    def plotPygame(self,new_endgoal,visited):
        observation=[]            
        for i in range(0,301):
            for j in range(0,201):
                c=self.obstacle(i,j)
                if c==1:
                    observation.append([i,j])
                    
        state=np.array(observation)
        observation=state*self.index
        visited_buffer = np.array(visited)
        #print (visited_buffer)
        visited=visited_buffer*self.index
        visited_buffer1 = np.array(new_endgoal)
        new_endgoal=visited_buffer1*self.index
        pygame.init()
        
        size = [300*self.index, 200*self.index]
        display = pygame.display.set_mode(size)
        pygame.display.set_caption("Dijkstra Point Robot") 
        clock = pygame.time.Clock()
        done = False

        while not done:
            print ("reached  here####################")
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:  
                    done = True 
            display.fill(self.black)
            for i in observation:
                pygame.draw.rect(display, self.white, [i[0],200*self.index-i[1],self.index,self.index])
            pygame.display.flip()
            clock.tick(20)
            for i in visited:
                pygame.time.wait(1)
                pygame.draw.rect(display, self.green, [i[0],200*self.index-i[1],self.index,self.index])
                pygame.display.flip()
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
        while endgoal not in visited:
                self.child(nodes[new_index],in_weight,visited,nodes,weight_list,root)
                visited.append(nodes[new_index])
                
                new_root.append(root[new_index])
                nodes.pop(new_index)
                weight_list.pop(new_index)
                root.pop(new_index)
                counter=counter+1
                if weight_list != []:
                    in_weight=min(weight_list)
                    index=weight_list.index(in_weight)
                    new_index=index
        print (len(visited))
        self.traverseNode(endgoal,visited,new_root,startPointX,startPointY,new_endgoal)
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


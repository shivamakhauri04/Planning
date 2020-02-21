import numpy as np
import re
import os

# class to store graph data
class GraphNode:
    # constructor
    def __init__(self,data,level,visited):
        # store the data of the node
        self.data = data
        # store the level of the graph
        self.level = level
        # track if the node is visited
        self.visited = visited 
    
    def find_zero(self,matrix,x):
        # find and return the index of zeros in the 2d array
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if matrix[i][j]==x:
                    return i,j
    
    def shift_graphElements(self,matrix,x1,y1,x2,y2):
        # generate new puzzle childrens by shifting the position of zero
        if x2 >=0 and x2 < len(self.data) and y2 >= 0 and y2 <len(self.data):
            temp_matrix = []
            # copy the original matrix in buffer to keep track
            temp_matrix = self.matrix_copy(matrix)
            # swap the elements to create new graph
            temp =  temp_matrix[x2][y2]
            temp_matrix[x2][y2] = temp_matrix[x1][y1]
            temp_matrix[x1][y1] = temp
            return temp_matrix
        else:
            None

    
    def expand_matrix(self,parent_tag,child_tag):
        
        # call the function to find position of zero
        x,y = self.find_zero(self.data,0)
        
        # shuffle the puzzle to create new children
        shuffle_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        child_matrix = []
       
        
        for i in shuffle_list:
            # for each children add the values in the text file
            child = self.shift_graphElements(self.data,x,y,i[0],i[1])
            
            
            if child is not None:
                # for each children store its data 
                child_node = GraphNode(child,self.level+1,0)
                child_matrix.append(child_node)
                child_tag = child_tag+1  
                
                    
        return child_matrix

    def matrix_copy(self,data):
        # create a copy of the matrix of the graph to keep its track before shuffling
        temp = []
        for i in data:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
    
    

class dfs:
    def __init__(self,size):
        # find the size of the row of the adjency matrix of the graph
        self.n = size
        # to keep a track of the unvisited nodes
        self.open = []
        # to keep a trcak of the visited nodes
        self.closed = []

    def inputMatrix(self):
        # input the elements of the puzzle from the user
        matrix = []
        for i in range(3):
            data = []
            for j in range(3):
                data.append(int(input()))
            matrix.append(data)
        return matrix
        

    def invCount(self,initialMatrix):
        # function to count the number of inversions 
        invCount = 0
        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if initialMatrix[j]>initialMatrix[i]:
                    invCount = invCount + 1
        return invCount

    def checkSolvability(self,initialMatrix):
        # function to check if the number of inversions is odd
        temp = initialMatrix
        invCount = self.invCount(temp)
        return (invCount%2)


    def check_visited(self,start,goal):
        # function to keep a track of the visted nodes
        return self.visited_status(start.data,goal)+start.level
    
    def visited_status(self,start,goal):
        temp = 0
        # function to check the status of the graph node is visited
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    temp +=1
        return temp

def remove_bracks():
    file = open('temp.txt','r')
    file1 = open('Nodes.txt','w')
    lines = file.read()
    s = re.sub(r'[^\w\s]','',lines)
    file1.write(s)
    file.close()
    os.remove('temp.txt')

def main():
    # constructor call
    DFS = dfs(3)
    print("input the start matrix(3*3)- Enter the data element by element")
    # add the input elements of the graph
    initialMatrix = DFS.inputMatrix()
    # check for solvability of the puzzle
    if (DFS.checkSolvability(initialMatrix)):
        print ("Not solvable")
    else:
        print("input the goal matrix(3*3)- Enter the data element by element")
        # if solvable, enter the goal matrix
        goalMatrix = DFS.inputMatrix()
        # traverse through the nodes of the matrix
        initialMatrix = GraphNode(initialMatrix,0,0)
        # track the nodes which have already been traversed
        initialMatrix.visited = DFS.check_visited(initialMatrix,goalMatrix)
        # store the possible paths
        DFS.open.append(initialMatrix)
        print ('\n \n')
        # Creating recursion
        f1 = open("nodePath.txt","w")
        f = open('temp.txt','w')
        f2 = open("NodesInfo.txt",'w')
        parent_tag = 0
        child_tag = 1
        f2.write(str(child_tag))
        f2.write(' ')
        f2.write(str(parent_tag)) 
        while True:
            current_matrix = DFS.open[0]
            print("")
            print("######################")
            print("\n")
            for i in current_matrix.data:
                for j in i:
                    print(j,end = " ")
                print("")
            # store the graph cnfiguration for the best path
            temp = np.asarray(current_matrix.data)
            # slice nodes to store them columnwise 
            temp1 = [i for i in temp[:,0]]
            str1 = ''
            for i in temp1:
                str1 = str1 + str(i) + ' '

            temp2 = [i for i in temp[:,1]]
            str2 = ''
            for i in temp2:
                str2 = str2 + str(i) + ' '

            temp3 = [i for i in temp[:,2]]
            str3 = ''
            for i in temp3:
                str3 = str3 + str(i) + ' '
            # write nodes in file
            f1.write(str(str1))
            f1.write(' ')
            f1.write(str(str2))
            f1.write(' ')
            f1.write(str(str3))
            f1.write('\n')  
            parent_tag = parent_tag+1
            # limiting condition for recursion so that doesn't run infinitely
            if(DFS.visited_status(current_matrix.data,goalMatrix)==0):
                break
            for i in current_matrix.expand_matrix(parent_tag,child_tag):
                # traverse the neighbours of the visited noeds to check if visited
                i.visited = DFS.check_visited(i,goalMatrix)
                
                child_tag = child_tag + 1
                #print (i.data)
                f.write(str(i.data))
                f.write('\n')
                f2.write('\n')
                f2.write(str(child_tag))
                f2.write(' ')
                f2.write(str(parent_tag))

                
                DFS.open.append(i)
            
            # if node travered, store it in closed list
            DFS.closed.append(current_matrix)
            del DFS.open[0]
            DFS.open.sort(key = lambda x:x.visited,reverse=False)
        f1.close()
        f.close()

if __name__ == "__main__":
    main()
    remove_bracks()

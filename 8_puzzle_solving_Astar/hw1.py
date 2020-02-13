#Pseudocode
# Input the initial matrix
# Input the goal matrix
# Create a graph node with the initial input matrix
# Calculate the f score of the start node
# Expand the current node and append the expanded matrces each as a node to the graph in the Open list
# Push the current node into closed list
# Calculate the fsore again for each node
# State with the least fscore is expanded again
# Continue the above process till the current_state=goal_matrix


class GraphNode:
    def __init__(self,data,level,fvalue):
        self.data = data
        self.level = level
        self.fvalue = fvalue 
    
    def find_underScore(self,matrix,x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if matrix[i][j]==x:
                    return i,j
    
    def shift_graphElements(self,matrix,x1,y1,x2,y2):
        if x2 >=0 and x2 < len(self.data) and y2 >= 0 and y2 <len(self.data):
            temp_matrix = []
            temp_matrix = self.matrix_copy(matrix)
            temp =  temp_matrix[x2][y2]
            temp_matrix[x2][y2] = temp_matrix[x1][y1]
            temp_matrix[x1][y1] = temp
            return temp_matrix
        else:
            None

    
    def expand_matrix(self):
        x,y = self.find_underScore(self.data,'_')
        shuffle_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        child_matrix = []
        for i in shuffle_list:
            child = self.shift_graphElements(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = GraphNode(child,self.level+1,0)
                child_matrix.append(child_node)
        return child_matrix

    def matrix_copy(self,data):
        temp = []
        for i in data:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
    
    

class Astar:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []

    def inputMatrix(self):
        data = []
        for i in range(0,self.n):
            row = input().split(" ")
            data.append(row)
        return data

    def f_score(self,start,goal):
        return self.h_score(start.data,goal)+start.level
    
    def h_score(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != "_":
                    temp +=1
        return temp

    def main(self):
        print("input the start matrix(3*3)- Enter the data rowwise with spaces in between elements")
        initialMatrix = self.inputMatrix()
        print("input the goal matrix(3*3)- Enter the data rowwise with spaces in between elements")
        goalMatrix = self.inputMatrix()
        initialMatrix = GraphNode(initialMatrix,0,0)
        initialMatrix.fvalue = self.f_score(initialMatrix,goalMatrix)
        self.open.append(initialMatrix)
        print ('\n \n')
        # Creating recursion
        while True:
            current_matrix = self.open[0]
            print("")
            print("######################")
            print("\n")
            for i in current_matrix.data:
                for j in i:
                    print(j,end = " ")
                print("")
        # limiting condition for recursion so that doesn't run infinitely
            if(self.h_score(current_matrix.data,goalMatrix)==0):
                break
            for i in current_matrix.expand_matrix():
                i.fvalue = self.f_score(i,goalMatrix)
                self.open.append(i)
            self.closed.append(current_matrix)
            del self.open[0]

            self.open.sort(key = lambda x:x.fvalue,reverse=False)
        





puzzle = Astar(3)
puzzle.main()


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
        x,y = self.find_underScore(self.data,0)
        shuffle_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        child_matrix = []
        f = open('Nodes.txt','w')
        for i in shuffle_list:
            child = self.shift_graphElements(self.data,x,y,i[0],i[1])
            if child is not None:
                buffer = []
                child_node = GraphNode(child,self.level+1,0)
                child_matrix.append(child_node)
                for m in child_node.data:
                    for n in m:
                        f.write(str(n))
                        f.write(' ')
                f.write('\n')
                        
                print (buffer)        #############put in text
                
                
                
        f.close()
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
        matrix = []
        for i in range(3):
            data = []
            for j in range(3):
                data.append(int(input()))
            matrix.append(data)
        return matrix
        

    def invCount(self,initialMatrix):
        invCount = 0

        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if initialMatrix[j]>initialMatrix[i]:
                    invCount = invCount + 1
        return invCount

    def checkSolvability(self,initialMatrix):
        temp = initialMatrix
        invCount = self.invCount(temp)
        return (invCount%2)


    def f_score(self,start,goal):
        return self.h_score(start.data,goal)+start.level
    
    def h_score(self,start,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    temp +=1
        return temp




def main():
    astar = Astar(3)
    print("input the start matrix(3*3)- Enter the data element by element")
    initialMatrix = astar.inputMatrix()
    print (initialMatrix)
    if (astar.checkSolvability(initialMatrix)):
        print ("Not solvable")
    else:
        
        print("input the goal matrix(3*3)- Enter the data element by element")
        goalMatrix = astar.inputMatrix()
        initialMatrix = GraphNode(initialMatrix,0,0)
        initialMatrix.fvalue = astar.f_score(initialMatrix,goalMatrix)
        astar.open.append(initialMatrix)
        print ('\n \n')
        # Creating recursion
        f1 = open("nodePath.txt","w")

        while True:
            current_matrix = astar.open[0]
            print("")
            print("######################")
            print("\n")
            for i in current_matrix.data:
                for j in i:
                    print(j,end = " ")
                    f1.write(str(j))
                    f1.write(' ')

                f1.write('\n')     
                print("")
            # limiting condition for recursion so that doesn't run infinitely
            if(astar.h_score(current_matrix.data,goalMatrix)==0):
                break
            for i in current_matrix.expand_matrix():
                i.fvalue = astar.f_score(i,goalMatrix)
                astar.open.append(i)
            astar.closed.append(current_matrix)
            del astar.open[0]

            astar.open.sort(key = lambda x:x.fvalue,reverse=False)
        f1.close()





#puzzle = Astar(3)
main()

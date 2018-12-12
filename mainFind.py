class DFA: 
   
    def __init__(self,num_states): 
        self.collection = [-1 for x in range(num_states)] #No. of vertices 
        #self.graph = defaultdict(list) # default dictionary to store graph 
   
  
    # function to add an edge to graph 
    '''
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    '''
    # A utility function to find the subset of an element i 
    def find_parent(self, i): 
        if self.collection[i] == -1: 
            return i 
        if self.collection[i] != -1: 
             return self.find_parent(self.collection[i]) 
  
    # A utility function to do union of two subsets 
    def union(self,x,y): 
        x_set = self.find_parent(x) 
        y_set = self.find_parent(y) 
        self.collection[x_set] = y_set 
        #self.collection[x] = y


    # start states: s_1 s_2, delta table: delta_1 delta_2, accepting states: f_1 f_2
    def unionFind(self, s_1, s_2, delta_1, l):
        List = []
        #collection = []

        # Add start states for both DFAs
        List.append([s_1, s_2])

        #print("Here")
        #print(List)
        # Add states to collection
        #col = len(delta_1) + len(delta_2)
        '''
        for i in range(col):
            collection.append(-1)
        '''    

        while (len(List) != 0):
            print(List)
            temp = List.pop(0)
            # FIND(A_1) FIND(A_2)
            A_1 = self.find_parent(temp[0])
            A_2 = self.find_parent(temp[1])

            #if A_1 != f_1 and A_2 != f_2:
            if A_1 != A_2:
                #UNION(A_1, A_2, A_1)
                self.union(A_1, A_2)
                for i in range(l):
                    List.append([delta_1[temp[0]][i], delta_1[temp[1]][i]])
                    
    def check_equ(self, f_1, f_2):
        for i in range(len(self.collection)):
            #print("i and index: ", i, self.collection[i])
            print("final states: ", f_1, f_2)
            if(self.collection[i] != -1):
                if(i == f_1 or i == f_2):
                    if(self.collection[i] != f_1 and self.collection[i] != f_2):
                        print("False")
                        print("i and index: ", i, self.collection[i])
                        return False
                else:
                    continue
            else:
                break
        return True
            
def main():
    '''
    #Equivalent DFAs
    DFA_1 = [[1, 2], [3, 1], [1, 2], [1, 0], [5, 4], [6, 5], [5, 4]]
    
    s_1 = 0
    f_1 = 3
    
    s_2 = 4
    f_2 = 6
    l = len(DFA_1[0])
    num_states = 7
    
    DFA_1 = [[1, 0], [0, 2], [2, 1], [4, 3], [6, 5], [5, 6], [3, 4]]
    
    s_1 = 0
    s_2 = 3
    f_1 = 0
    f_2 = 3
    l = len(DFA_1[0])
    num_states = 7
    '''
    
    DFA_1 = [[1], [2], [3], [4], [5], [0], [7], [8], [6]]
    
    s_1 = 0
    s_2 = 6
    #f_1 =
    l = 1
    num_states = 9
    
    E = DFA(num_states)
    
    E.unionFind(s_1, s_2, DFA_1, l)
    
    print(E.collection)
    '''
    check = E.check_equ(f_1, f_2)
    #check2 = 
    if(check):
        print("Valid DFAs")
    else:
        print("Invalid DFAs")
    '''
    #print(check)
    #print(E.check_equ(f_1, f_2))
    
    #unionFind()
main()
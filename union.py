import sys

class state:
    def __init__(self, _accepting, _zero_tr, _one_tr):
	self.accepting = _accepting
        self.zero_tr = _zero_tr
	self.one_tr = _one_tr

class DFA:
    def __init__(self, dfa_file):
        file = open(dfa_file,"r")
        lines = file.read().splitlines()
        for i in range(len(lines)):
            lines[i] = list(map(int, lines[i].split()))
            
        states = lines[1:]
        self.numStates = lines[0][0]
        self.numTrans = lines[0][1]
        acceptStates = lines[0][2:]
        self.delta = []
        
        for i in range(self.numStates):
            current = state((i in acceptStates), states[i][0], states[i][1])
            self.insert_state(current)

	    
    def insert_state(self, state):
	self.delta.append(state)

class UNION_FIND:
    def __init__ (self, dfa_file_1, dfa_file_2):
        self.dfa_main = DFA(dfa_file_1)
        self.dfa_other = DFA(dfa_file_2)
        for i in range(len(self.dfa_other.delta)):
            self.dfa_other.delta[i].one_tr += self.dfa_main.numStates
            self.dfa_other.delta[i].zero_tr += self.dfa_main.numStates
        
        self.other_start = self.dfa_main.numStates # will be index representing start of tacked on dfa
        for i in range(self.dfa_other.numStates):
            self.dfa_main.insert_state(self.dfa_other.delta[i])
        self.dfa_main.numStates = self.dfa_main.numStates + self.dfa_other.numStates
        self.collection = [-1 for x in range(self.dfa_main.numStates)]
        self.List = []
        self.List.append([0, self.other_start])
                 
        
    # A utility function to find the subset of an element i
    def find_parent(self, i):
        if self.collection[i] == -1:
            return i
        return self.find_parent(self.collection[i])

    def union(self,x,y):
        self.collection[x] = y

    def equivalence(self):
        print "Our DFA:"
        for i in range(len(self.dfa_main.delta)):
            print "accept: ", self.dfa_main.delta[i].accepting, " zero: ", self.dfa_main.delta[i].zero_tr, " one: ", self.dfa_main.delta[i].one_tr
        
        while (len(self.List) != 0):
            current = self.List.pop(0)
            print "LEEST:", self.List
            A_1 = self.find_parent(current[0])
            A_2 = self.find_parent(current[1])
            if A_1 != A_2:
                self.union(A_1, A_2)
                self.List.append([self.dfa_main.delta[current[0]].zero_tr, self.dfa_main.delta[current[1]].zero_tr])
                self.List.append([self.dfa_main.delta[current[0]].one_tr, self.dfa_main.delta[current[1]].one_tr])
        print self.collection


class LAZY:
    def __init__(self, dfa_file_1, dfa_file_2):
        self.dfa_1 = DFA(dfa_file_1)
        self.dfa_2 = DFA(dfa_file_2)

    def exclusive(self):
         equal = 1
         processing_states = []

         seen_states = [[0,0]]
         current_1 = seen_states[0][0]
         current_2 = seen_states[0][1]
         processing_states.append(seen_states[0])
         while(len(processing_states) > 0 ):

             temp = processing_states.pop(0)
             current_1 = temp[0]
             current_2 = temp[1]
             
             if( self.dfa_1.delta[current_1].accepting != self.dfa_2.delta[current_2].accepting):
                 equal = 0
                 
             state_on_zero = [self.dfa_1.delta[current_1].zero_tr, self.dfa_2.delta[current_2].zero_tr]
             if (state_on_zero not in seen_states):
                 seen_states.append(state_on_zero)
                 processing_states.append(state_on_zero)

             state_on_one = [self.dfa_1.delta[current_1].one_tr, self.dfa_2.delta[current_2].one_tr]
             if (state_on_one not in seen_states):
                 seen_states.append(state_on_one)
                 processing_states.append(state_on_one)

         if (equal):
             print "EEEQUIQUI"
         else:
             print "NARC"
             
def main():
    #DFA_1_FILE = input("DFA 1: ")
    #DFA_2_FILE = input("DFA 2: ")

    decision = input("Enter 1 for lazy, 2 for union_find: ")
    if (decision == 1):
        LAZY_obj = LAZY(sys.argv[1], sys.argv[2])
        LAZY_obj.exclusive()
    if (decision == 2):
        UNION_FIND_obj = UNION_FIND(sys.argv[1], sys.argv[2])
        UNION_FIND_obj.equivalence()

main()

import sys
import time

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
        self.dfa_other1 = (dfa_file_1)
        self.dfa_other = DFA(dfa_file_2)
        self.dfa_copy = DFA(dfa_file_2)
        for i in range(len(self.dfa_copy.delta)):
            self.dfa_copy.delta[i].one_tr += self.dfa_main.numStates
            self.dfa_copy.delta[i].zero_tr += self.dfa_main.numStates

        self.other_start = self.dfa_main.numStates # will be index representing start of tacked on dfa
        for i in range(self.dfa_copy.numStates):
            self.dfa_main.insert_state(self.dfa_copy.delta[i])
        self.dfa_main.numStates = self.dfa_main.numStates + self.dfa_copy.numStates
        self.collection = [-1 for x in range(self.dfa_main.numStates)]
        self.List = []
        #self.List2 = []
        self.List.append([0, self.other_start, "e"])
        self.witness = ""
        #self.wit1 = ""
        #self.wit2 = ""
        self.wit_len = 0
        self.e = 1


    # A utility function to find the subset of an element i
    def find_parent(self, i):
        if self.collection[i] == -1:
            return i
        return self.find_parent(self.collection[i])

    def union(self,x,y,l):
        #print "x: ", x, " y: ", y
        self.collection[x] = y
        self.witness += l


    def equivalence(self):
        #print "Our DFA:"

        #for i in range(len(self.dfa_main.delta)):
            #print "accept: ", self.dfa_main.delta[i].accepting, " zero: ", self.dfa_main.delta[i].zero_tr, " one: ", self.dfa_main.delta[i].one_tr

        while (len(self.List) != 0):
            #print "LEEST:", self.List
            current = self.List.pop(0)
            #print "LEEST:", self.List
            #print("Collection: ", self.collection)
            A_1 = self.find_parent(current[0])
            A_2 = self.find_parent(current[1])
            if A_1 != A_2:
                self.union(A_1, A_2, current[2])
                self.List.append([self.dfa_main.delta[current[0]].zero_tr, self.dfa_main.delta[current[1]].zero_tr, "0"])
                self.List.append([self.dfa_main.delta[current[0]].one_tr, self.dfa_main.delta[current[1]].one_tr, "1"])
        #print self.collection
        '''
        if(self.check_equ()):
            print("Yes, the two DFA's are equivalent")
        else:
            print("No, the two DFA's are not equivalent. Here is the shortest witness accepted by one of them: ")
            #self.wit()
            #print(self.witness[1:self.wit_len+1])
        '''

    def wit(self):
        next_tran = []
        next_tran.append([0, self.other_start])
        for i in range(1 ,len(self.witness)):
            temp = next_tran.pop(0)
            if (self.dfa_main.delta[temp[0]].accepting and not(self.dfa_main.delta[temp[1]].accepting)):
                break
            if (self.dfa_main.delta[temp[1]].accepting and not(self.dfa_main.delta[temp[0]].accepting)):
                break
            else:
                if self.witness[i] == "0":
                    next_tran.append([self.dfa_main.delta[temp[0]].zero_tr, self.dfa_main.delta[temp[1]].zero_tr])
                    self.wit_len += 1
                else:
                    next_tran.append([self.dfa_main.delta[temp[0]].one_tr, self.dfa_main.delta[temp[1]].one_tr])
                    self.wit_len += 1

    def check_equ(self):
        for i in range(len(self.collection)):
            #print(i, " ", self.collection[i])
            #print(self.dfa_main.delta[i].accepting, " ", self.dfa_main.delta[self.collection[i]].accepting)
            if(self.collection[i] == -1):
                continue
            if (self.dfa_main.delta[i].accepting):
                if(not(self.dfa_main.delta[self.collection[i]].accepting)):
                    print("No, the two DFA's are not equivalent. This is the shortest witness: ")
                    self.e = 1
                    #self.wit()
                    #print(self.witness[1:self.wit_len+1])
                    return False
            if (self.dfa_main.delta[self.collection[i]].accepting):
                if(not(self.dfa_main.delta[i].accepting)):
                    print("No, the two DFA's are not equivalent. This is the shortest witness: ")
                    self.e = 1
                    #self.wit()
                    #print(self.witness[1:self.wit_len+1])
                    return False
        #return True
        print("Yes, the two DFA's are equivalent")
        self.e = 0
class LAZY:
    def __init__(self, dfa_file_1, dfa_file_2):
        self.dfa_1 = DFA(dfa_file_1)
        self.dfa_2 = DFA(dfa_file_2)
        self.ee = 0

	def exclusive(self):
		start = time.time()
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
            print "Yes, the two DFA's are equivalent"
        else:
            print "No, the two DFA's are not equivalent. Here is the shortest witness: "
            self.ee = 1
        end = time.time()
        #print(end - start)


def main():

    DFA_1_FILE = raw_input("Please type the name of the file containing the first DFA: ")
    DFA_2_FILE = raw_input("Please type the name of the file containing the second DFA: ")

    #LAZY_obj = LAZY(DFA_1_FILE, DFA_2_FILE)
    #UNION_FIND_obj = UNION_FIND(DFA_1_FILE, DFA_2_FILE)

    prog_decision = 1
    while(prog_decision != -1):
        alg_decision = input("Enter 1 for lazy, 2 for union_find: ")
        if (alg_decision == 1):
            LAZY_obj = LAZY(DFA_1_FILE, DFA_2_FILE)
            if (LAZY_obj.ee == 1):
                UNION_FIND_obj = UNION_FIND(DFA_1_FILE, DFA_2_FILE)
                UNION_FIND_obj.equivalence()
                #UNION_FIND_obj.check_equ()
                UNION_FIND_obj.wit()
                print(UNION_FIND_obj.witness[1:UNION_FIND_obj.wit_len+1])
            #LAZY_obj.exclusive()
        if (alg_decision == 2):
            UNION_FIND_obj = UNION_FIND(DFA_1_FILE, DFA_2_FILE)
            UNION_FIND_obj.equivalence()
            UNION_FIND_obj.check_equ()
            if (UNION_FIND_obj.e == 1):
                UNION_FIND_obj.wit()
                print(UNION_FIND_obj.witness[1:UNION_FIND_obj.wit_len+1])
        prog_decision = input("Enter -1 to quit, 1 to continue with same input, 0 to change input: ")
        if (prog_decision == 0):
            DFA_1_FILE = raw_input("Enter file 1: ")
            DFA_2_FILE = raw_input("Enter file 2: ")
            #LAZY_obj = LAZY(DFA_1_FILE, DFA_2_FILE)
            #UNION_FIND_obj = UNION_FIND(DFA_1_FILE, DFA_2_FILE)
    '''
    decision = input("Enter 1 for lazy, 2 for union_find: ")
    if (decision == 1):
        LAZY_obj = LAZY(sys.argv[1], sys.argv[2])
        LAZY_obj.exclusive()
    if (decision == 2):
        UNION_FIND_obj = UNION_FIND(sys.argv[1], sys.argv[2])
        UNION_FIND_obj.equivalence()
    '''

main()

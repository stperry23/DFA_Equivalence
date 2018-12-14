'''
CS 454 Fall 2018
Ryan Boyle, Spencer Perry, and John Salman
Final Project
--------------------------------------
Overview:
--------------------------------------
Report:

'''
import sys

def lazy_exclusive(numsStates_a, numTrans_a, acceptStates_a, dfa_a, numsStates_b, numTrans_b, acceptStates_b, dfa_b):
    equal = 0
    states = [[0,0]]
    all_states = [[0,0]]
    current = 0
    while(len(states) > 0 ):
        if(accept_check(new_states[current][0],new_states[current][1], acceptStates_a, acceptStates_b) == False):
            equal = 1
            new_states = []
        for i in range(numTrans_a):
            state = [dfa_a[new_states[current][0]][i],dfa_b[new_states[current][1]][i]]
            if(state not in states):
                new_states.append(state)
            states.append(state)
            print(new_states)
        new_states.pop(0)
        for i in range(numTrans_a-1):
            if(accept_check(new_states[current][0],new_states[current][1], acceptStates_a, acceptStates_b) == False):
                equal = 1
                new_states = []

    if(equal == 0):
        print("EQUIVALIANT")
    if(equal == 1):
        print("NOT EQUIVALIANT!!")



def accept_check(state_a, state_b, acceptStates_b, acceptStates_a):
    if(state_a in acceptStates_a and state_b in acceptStates_b):
        return True
    if(state_a not in acceptStates_a and state_b not in acceptStates_b):
        return True
    return False



def union_find(dfa_a, dfa_b):
    pass

def dfa_parser(dfa):
    file = open(dfa,"r")
    lines = file.read().splitlines()
    for i in range(len(lines)):
        lines[i] = list(map(int, lines[i].split()))

    dfa = lines[1:]
    numStates = lines[0][0]
    numTrans = lines[0][1]
    acceptStates = lines[0][2:]

    return numStates, numTrans, acceptStates, dfa



def main():

    DFA_A = "DFA_2_1.txt"#input("DFA 1: ")
    DFA_B = "DFA_2_2.txt"#input("DFA 2: ")

    numsStates_a, numTrans_a, acceptStates_a, dfa_a = dfa_parser(DFA_A)
    numsStates_b, numTrans_b, acceptStates_b, dfa_b = dfa_parser(DFA_B)

    lazy_exclusive(numsStates_a, numTrans_a, acceptStates_a, dfa_a, numsStates_b, numTrans_b, acceptStates_b, dfa_b)


main()

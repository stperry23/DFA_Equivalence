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

def lazy_exclusive(dfa_a, dfa_b, acceptStates_a, acceptStates_b):
    pass

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

    DFA_A = "DFA_1_1.txt"#input("DFA 1: ")
    DFA_B = "DFA_1_2.txt"#input("DFA 2: ")

    numsStates_a, numTrans_a, acceptStates_a, dfa_a = dfa_parser(DFA_A)
    numsStates_b, numTrans_b, acceptStates_b, dfa_b = dfa_parser(DFA_B)

    lazy_exclusive(dfa_a, dfa_b, acceptStates_a, acceptStates_b)


main()

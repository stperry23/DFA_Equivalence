# DFA_Equivalence
CS454 Final Project

Names: Spencer Perry, Ryan Boyle, John Salman 	Section: 1


Title of the project: Analysis of equivalence of DFA’s Algorithms 


Statement of problem: . Implement an efficient algorithm to test the equivalence of DFA’s. It is possible to solve this problem using the UNION/FIND data structure that we discussed in CS 415. Even if it was not covered in CS 415, it is not hard to learn the details.
 
First we will implement a ‘Lazy exclusive-or’ algorithm which we will find the cross product of the 2 DFA’s preceded by a breadth first search. The second algorithm we will take is the Union/Find approach. We will then compare and contrast the two approaches taken to solve this problem. 

Inputs and Outputs of the program: 
The program takes as input a text file containing 2 transition tables representing the two DFA’s. If the two DFA’s are not equivalent the program will output ‘Not equivalent’ and the shortest string accepted by one DFA but not the other. If the two DFA’s are equivalent the program will output ‘Equivalent’.



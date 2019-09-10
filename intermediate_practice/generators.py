# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:06:26 2019

@author: austin.schrader
"""

# generators
# another way of creating iterators
# uses a function rather than a separate class
# generates the background code for the next() and iter() methods
# uses a special statement called yield which saves the state of the generator and set a resume point for when next() is called again

# a python program to demonstrate working of generators
def Reverse(data):
    # this is like counting from 100 to 1 by taking one (-1)
    # step backward
    for index in range(len(data)-1, -1, -1):
        yield data[index]
    
def Main():
    rev = Reverse('Harssh')
    for char in rev:
        print(char)
    data = 'Harssh'
    print(list(data[i] for i in range(len(data)-1, -1, -1)))
    
if __name__=="__main__":
    Main()
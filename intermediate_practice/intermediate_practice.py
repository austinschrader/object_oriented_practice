# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:52:42 2019

@author: austin.schrader
"""

class MyClass:
    number = 0
    name = "noname"
    
def Main():
    me = MyClass()
    
    me.number = 1337
    me.name = "Harssh"
    
    print(me.name + " " + str(me.number))

if __name__ =='__main__':
    Main()
    

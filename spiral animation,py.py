# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:25:08 2020

@author: HP
"""

import turtle
import random

tur=turtle.Turtle()
turtle.bgcolor("black")

list_color=["white","red","pink","green","blue","yellow","orange","violet"]
tur.setpos(-250,250)
tur.penup()
def spiral(row,col):
    c=0
    r=0
    while(r<row and c<col):
        col1=random.randint(0,7)
        tur.color(list_color[col1])
        for i in range(r,col):
            tur.dot()
            tur.forward(25)
        tur.right(90)
        r=r+1
        
        col1=random.randint(0,7)
        tur.color(list_color[col1])
        for i in range(r,row):
            tur.dot()
            tur.forward(25)
        tur.right(90)
        col=col-1
        
        col1=random.randint(0,7)
        tur.color(list_color[col1])
        for i in range(col-1,c-1,-1):
            tur.dot()
            tur.forward(25)
        tur.right(90)
        row=row-1
        
        col1=random.randint(0,7)
        tur.color(list_color[col1])
        for i in range(row-1,r-1,-1):
            tur.dot()
            tur.forward(25)
        tur.right(90)
        c=c+1

spiral(20,21)    
turtle.done()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:52:53 2017

@author: tymarking
"""

from .operator import Operator, Opps, Times, Plus, Minus, Divide, Power
from constant import Constant




def main():
    equation = input("enter equation to solve: ")
    print("Your equation is " +str(equation))
    if not checkInput(equation):
        return
    
    equ = parseInput(equation)
    
    
    
def checkInput(equation):
    if "=" not in equation:
        print("Equation must include an equal sign")
        return False
    
def parseInput(equation):
    
    
    
    return

main()
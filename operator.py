#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:06:22 2017

@author: tymarking
"""

from enum import Enum, NoAlias

class Operator(object):
    oppType = None
    def __init__(self):
        return
    
    def evaluate(self, expression1 = None, expression2 = None):
        #returns expression after evaluating operator and given expressions
        raise NotImplementedError
    
    def getType(self):
        return self.oppType
    
    
class Opps(Enum):
    _settings_ = NoAlias
    #Value is order stepp (power before * and / before + and -)
    PLUS = 1
    MINUS = 1
    TIMES = 2
    DIVIDE = 2
    POWER = 3
    

class Times(Operator):
    def __init__(self):
        self.oppType = Opps.TIMES
        return
    def evaluate(self, expression1 = None, expression2 = None):
        #returns expression after evaluating operator and given expressions
        raise NotImplementedError
        
class Plus(Operator):
    def __init__(self):
        self.oppType = Opps.PLUS
        return
    def evaluate(self, expression1 = None, expression2 = None):
        #returns expression after evaluating operator and given expressions
        raise NotImplementedError
        
class Minus(Operator):
    def __init__(self):
        self.oppType = Opps.MINUS
        return
    def evaluate(self, expression1 = None, expression2 = None):
        #returns expression after evaluating operator and given expressions
        raise NotImplementedError
        
class Divide(Operator):
    def __init__(self):
        self.oppType = Opps.DIVIDE
        return
    def evaluate(self, expression1 = None, expression2 = None):
        #returns expression after evaluating operator and given expressions
        raise NotImplementedError

class Power(Operator):
    def __init__(self):
        self.oppType = Opps.POWER
        return
    def evaluate(self, expression1 = None, expression2 = None):
        #returns expression after evaluating operator and given expressions
        raise NotImplementedError
    
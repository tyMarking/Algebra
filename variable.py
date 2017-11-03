#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:07:16 2017

@author: tymarking
"""

#dict of var types. if key = str of var, value is what it equals to (expression) if value is none, var is unkown
variableTypes = {}

class Variable(object):
    name = None
    power = 1
    def __init__(self, name, power = None):
        self.name = name
        if power is not None:
            self.power = power
        if name not in variableTypes:
            variableTypes[name] = [self,]
        else:
            varList = variableTypes[name]
            varList.append(self)
            variableTypes[name] = varList
            
    def getListOfSameVar(self):
        return variableTypes[self.name]
    
    
    def substitute(self, expression):
        #return equation and remove from variableTypes
        varList = variableTypes[self.name]
        varList.remove(self)
        variableTypes[self.name] = varList
        raise NotImplementedError
        
            
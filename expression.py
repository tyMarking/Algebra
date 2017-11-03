#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:07:35 2017

@author: tymarking
"""
from operator import Operator

class Expression():
    unorderedItems = []
    def __init__(self, items = None):
        if items is not None:
            self.unorderedItems = items
    
    def addItem(self, item):
        self.unorderedItems.append(item)
    
    def setItems(self, items):
        self.unorderedItems = items
        
    def order(self):
        for i in range(len(self.unorderedItems)):
            if type(self.unorderedItems[i]) is Operator:
                
                
        
    
# Recursive, expressions within expressions
# stack of opperators
# value operator (value operator (value operator value))
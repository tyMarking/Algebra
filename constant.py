#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:06:53 2017

@author: tymarking
"""

class Constant(object):
    value = None
    def __init__(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
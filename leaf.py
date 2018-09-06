# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 18:29:41 2018

@author: Simone Casini
"""
class Leaf:
    """A leaf of the decision tree"""
    
    def __init__(self, result):
        self.result = result
    
    
    def __call__(self, example):
        return self.result
    
    
    def display(self, indent=0):
        print('Result =', self.result)
        
        
    def __repr__(self):
        return repr(self.result)

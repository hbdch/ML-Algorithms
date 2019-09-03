# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:11:27 2019

@author: Sahil
"""

import numpy as np
import CustomExceptions
class Node:
    id_count = 1
    def __init__(self, label, data):
        self.label = label
        self.data = data
        self.left = None
        self.right = None
        self.id = id_count
        id_count += 1
    
    def get_label(self):
        return self.label
    
    def get_data(self):
        return self.data
    
    def set_label(self, newlabel):
        self.label = newlabel
    
    def set_data(self, newdata):
        self.data = newdata
    
    def add_node_left(self, node):
        if self.left is not None:
            raise CustomExceptions.InsertionError('Left branch already contains a Node')
        
        self.left = node
    
    def add_node_right(self, node):
        if self.right is not None:
            raise CustomExceptions.InsertionError('Right branch already contains a Node')
        
        self.right = node
        

class Tree:
    
    def __init__(self):
        self.root = Node('root', None)
        
    def print_tree(self):
        pass
    
    #Get node by id
    #Get list of leaf nodes
    
    
        
        
        
        
# -*- coding: utf-8 -*-
'''
Created on Tue Jun 16 12:29:08 2015

@author: Walt
'''

class Glaze:
    
    def __init__(self, *receipe):
        if receipe != ():        
            self.name = receipe[0]['name']
            self.type = receipe[0]['type']
            self.materials = receipe[0]['materials']
            self.additives = receipe[0]['additives']
        
    def material_list(self):
        pass
    
    def to_batch(self):
        if self.type == 'batch':
            print 'only for percentage recepies'
        else:
            pass
    
    def to_percent(self):
        if self.type == 'percent':
            print 'only for batch recepies'
# -*- coding: utf-8 -*-
'''
Created on Tue Jun 16 12:29:08 2015

@author: Walt
'''
from chem_parse import atomic_weight

class Glaze:
    
    def __init__(self, *receipe):
        if receipe != ():        
            self.name = receipe[0]['name']
            self.type = receipe[0]['type']
            self.materials = receipe[0]['materials']
            self.additives = receipe[0]['additives']


    def to_batch(self, materials):
        if self.type == 'batch':
            print 'already in batch form'
            return materials
        else:
            print('type {} not yet implemented'.format(self.type))
            return 0

    def to_percent(self, materials):

        if self.type == 'percent':
            print 'already in percent form'
            return materials
        elif self.type == 'batch':
            percents ={}
            total = sum(self.materials.values())
            for k,v in materials.iteritems():
                percents[k] = float(v)/total 
            return percents
        else:
            print('type {} not yet implemented'.format(self.type))
            return 0

    def to_unity(self, materials):
        if self.type == 'unity':
            print 'already in unity form'  
        else:
            print('type {} not yet implemented'.format(self.type))
            return 0
            
    def material_list(self, total_weight=10000):
        if self.type == 'batch':
            total = sum(self.materials.values())
            
            percents = self.to_percent(self.materials)                                   
            
            weights = {}
            for k,v in percents.iteritems():
                weights[k] = v*float(total_weight)
            
        print('Batch Materials')
        for k,v in self.materials.iteritems():
            print('-- {}: {}'.format(k,v))
        print('Total = {}'.format(total))
        print('')
        print('Percent Materials')
        for k,v in percents.iteritems():
            print('-- {}: {}'.format(k,v))
        print('Total = {}'.format(sum(percents.values())))
        for k,v in self.additives.iteritems():
            print('-- {}: {}'.format(k,v))
        print('')
        print('Weights Materials')
        for k,v in weights.iteritems():
            print('-- {}: {}'.format(k,v))
        print('Total = {}'.format(sum(weights.values())))
        
        if self.additives !={}:
            print('Additives')
            for k,v in self.additives.iteritems():
                if type(v) == list:
                    weights[k] = [x*float(total_weight)/100.0 for x in v]
                else:
                    weights[k] = float(v)*float(total_weight)/100.0
                print('-- {}: {}'.format(k,weights[k]))
            #print('Total Weight = {}'.format(sum(weights.values())))
            
          
            
            
    
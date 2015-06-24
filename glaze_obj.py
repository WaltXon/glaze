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
        
    def material_list(self, total_weight):
        if self.type == 'batch':
            total = sum(self.materials.values())
            
            percents ={}
            for k,v in self.materials.iteritems():
                percents[k] = float(v)/total                                    
            
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
                weights[k] = [x*float(total_weight)/100.0 for x in v]
                print('-- {}: {}'.format(k,weights[k]))
            #print('Total Weight = {}'.format(sum(weights.values())))
            
    def to_batch(self):
        if self.type == 'batch':
            print 'only for percentage recepies'
        else:
            pass
    
    def to_percent(self):
        if self.type == 'percent':
            print 'only for batch recepies'

    def to_unity(self):
        if self.type == 'percent':
            print 'only for batch recepies'            
            
            
            
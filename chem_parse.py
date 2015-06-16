# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:08:28 2015

@author: waltn_000
"""

from pyparsing import Word, Optional, OneOrMore, Group, ParseException
import pandas as pd
import os
import string

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

df = pd.read_table(os.path.join(BASE_DIR, 'elements.csv'),sep=',',  header=0, skipinitialspace=True)


caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"

element = Word( caps, lowers )
elementRef = Group( element + Optional( Word( digits ), default="1" ) )
formula = OneOrMore( elementRef )

tests = [ "Al2O3", "SiO2" ]
for t in tests:
    try:
        results = formula.parseString( t )
        print t,"->", results,
    except ParseException, pe:
        print pe
    else:
        wt = sum([float(df[df['Symbol']=='{}'.format(elem)].Atomic_Weight.iloc[0]) * int(qty) for elem,qty in results])
        print ("{}".format(wt))


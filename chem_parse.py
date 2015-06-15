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

names = ['atomic_number' , 'symbol', 'name', 'atomic_mass',
'CPK color in RRGGBB hex format', 'electronic configuration', 'electronegativity in Pauling',
'atomic radius in pm' , 'ion radius in pm', 'van der Waals radius in pm', 'IE-1 in kJ/mol',
'EA in kJ/mol', 'oxidation states', 'standard state', 'bonding type', 'melting point in K',
'boiling point in K', 'density in g/mL', 'metal or nonmetal?', 'year discovered'] 

df = pd.read_table(os.path.join(BASE_DIR, 'pt-data2.csv'),sep=',',  header=None, names=names)
df.symbol.apply(string.strip)

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"

element = Word( caps, lowers )
elementRef = Group( element + Optional( Word( digits ), default="1" ) )
formula = OneOrMore( elementRef )

tests = [ "H2O", "C6H5OH", "NaCl" ]
for t in tests:
    try:
        results = formula.parseString( t )
        print t,"->", results,
    except ParseException, pe:
        print pe
    else:
        wt = sum( [df.query('symbol == {}'.format(elem))*int(qty) for elem,qty in results] )
        print "(%.3f)" % wt


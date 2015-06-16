# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:50:55 2015

@author: Walt
"""

data = {'higby 1-2-3 base': 
        { 
           'name': 'higby 1-2-3 base',
           'type': 'batch',
           'materials': {'silica': 1,
                         'epk': 2,
                         'gerstley borate': 3}, 
           'additives': {}
        }, 
      'higby water blue': 
          {
          'name': 'higby water blue',
        'type': 'batch',
        'materials': {'frit 3110': 70,
                      'gerstley borate': 5,
                      'silica': 5,
                      'soda ash': 10,
                      'epk': 5},
        'additives': {'copper carbonate': range(3,8)}
        },
       'higby green':
           {
           'name': 'higby green',
       'type': 'batch',
       'materials': {'frit 3110': 70,
                     'colemanite': 5,
                     'flint': 12,
                     'soda ash': 5,
                     'epk': 5},
       'additives': {'copper carbonate': [8],
                     'red iron oxide': [1]}
       }}
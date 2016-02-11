# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:25:01 2016

@author: Nikolay
"""

import json
import bz2
import pandas


with bz2.BZ2File('./matches.jsonlines.bz2') as matches_file:
    for line in matches_file:
        match = json.loads(line) ###doesn't work for Python 3!!!
        
        # Обработка матча
        break
    

features = pandas.read_csv('./features.csv', index_col='match_id')

features.head()
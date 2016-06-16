# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:39:27 2016

@author: Nikolay_Semyachkin
"""

graph = {1:{2, 3}, 2:{1}, 3:{1}, 4:set()}
start = 1
visited = []
distances = dict()

distances[start] = 0
d = 6
togo = graph[start]

thislevel = set()
for i in togo:
    thislevel.add(i)

for i in togo:
    distances[i] = d

d += 6


while True:
    togo = graph[start]
    thislevel = set()
    for i in togo:
        thislevel.add(i)
        distances[i] = d
    d += 6
    
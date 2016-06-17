# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:53:51 2016

@author: Nikolay_Semyachkin
"""

#graph = {1:{2, 3, 5}, 2:{1,6}, 3:{1}, 4:{6}, 5:{1}, 6:{2, 4}}
#start = 4
#d = 6

def bfs(graph, start):
    distance = dict()
    distance[start] = 0
    togo = set([start])
    marked = set()
    td = 0
    while togo:
        nextlevel = set()
        for i in togo:
            if i not in marked:
                distance[i] = td
                [nextlevel.add(n) for n in graph[i] if n not in marked]
                marked.add(i)
        td += 1
        togo = nextlevel
    return distance


####START INPUT:
TCs = int(input())

for tc in range(TCs):
    d = 6
    graph = dict()
    nodes_edges = [int(i) for i in input().split()]
    nodes = nodes_edges[0]
    edges_num = nodes_edges[1]
    
    for n in range(1, nodes+1):
        graph[n] = set()

    for i in range(edges_num):
        edge = [int(i) for i in input().split()]
        node1, node2 = edge[0], edge[1]
        graph[node1].add(node2)
        graph[node2].add(node1)
    
    start = int(input())
    ###INPUT FINISHED###
    
    dist = bfs(graph, start)
#    print(dist)
    for g in dist:
        dist[g] *= 6    
    
    for g in graph:
        if g not in dist:
            dist[g] = -1
    

        
    del dist[start]
    answer = ""
    for i in sorted(dist):
        answer += str(dist[i])+" "
    print(answer.strip())















#def bfs(graph, start):
#    undiscovered = []
#    distance = []
#    marked = set()
#    undiscovered.append(start)
#    distance.append(0)
#    marked.add(start)
##    td = 0
#    while undiscovered:
#        t = undiscovered.pop(0)
#        td = distance[-1]
#        
#        for vert in graph[t]:
#            if vert not in marked:
#                marked.add(vert)
#                undiscovered.append(vert)
#                distance.append(td+1)
#    return distance
#
#print(bfs(graph, start))

#def bfs(graph, start):
#    undiscovered = []
#    distance = dict()
#    marked = set()
#    undiscovered.append(start)
#    distance[start] = 0
#    marked.add(start)
#    td = 0
#    while undiscovered:
#        t = undiscovered.pop(0)
#        
#        
#        for vert in graph[t]:
#            if vert not in marked:
#                marked.add(vert)
#                undiscovered.append(vert)
#                distance[vert] = td+1
#        td += 1
#    return distance
#
#print(bfs(graph, start))
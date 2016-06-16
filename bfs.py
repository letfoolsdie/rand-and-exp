# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:44:43 2016

@author: Nikolay_Semyachkin
"""
def update_dist(distance_graph, new_vers, distance):
    for v in new_vers:
        distance_graph[v] += distance
    return distance_graph
    

def bfs(graph, start):
    visited, queue = dict(), [start]
    dist_dict = dict()
    distance = 0 #edge_len
    for g in graph:
        dist_dict[g] = 0    
    while queue:
        node = queue.pop(0)     
        
        if node not in visited:            
            visited[node] = dist_dict[node]
            new_vertices = graph[node] - set(visited)
#            print("node", node)
#            print("new verices", new_vertices)
#            print("distance", distance)
#            print("----------")
#            
            if new_vertices:
                distance += edge_len
                
            dist_dict = update_dist(dist_dict, new_vertices, distance)
            queue.extend(new_vertices)
    return dist_dict


###Prepare data:
TCs = int(input())
edge_len = 6
for tc in range(TCs):
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
    res = bfs(graph, start)
    
    for i in res:
        if res[i] == 0:
            res[i] = -1    
            
    del res[start]
    
    answer = ""
    for d in sorted(res):
        answer += str(res[d])+" "
            
    print(answer.strip())    

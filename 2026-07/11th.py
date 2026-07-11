# https://leetcode.com/problems/count-the-number-of-complete-components/?envType=daily-question&envId=2026-07-11

from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            comp.append(node)

            for nbr in adjList[node]:
                if nbr not in visited:
                    dfs(nbr)


        # create graph
        adjList=defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        res=0
        visited=set()
        
        for i in range(n):
            if i not in visited:
                comp=[]
                dfs(i)

                node_count=len(comp)
                edge_count=0
                for node in comp:
                    edge_count+=len(adjList[node])
                if edge_count==node_count*(node_count-1):
                    res+=1

        return res
        
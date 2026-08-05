# https://leetcode.com/problems/remove-methods-from-project/?envType=daily-question&envId=2026-08-05
from collections import defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # create a graph
        # find suspicious group using connected components dfs
        # see if any other code is using suspicious one if not remove them
        def dfs(node):
            sus.add(node)
            for nbr in adjList[node]:
                if nbr not in sus:
                    dfs(nbr)

        adjList=defaultdict(list)
        for u,v in invocations:
            adjList[u].append(v)
        
        sus=set()
        dfs(k)

        for i in range(n):
            if i not in sus:
                for nbr in adjList[i]:
                    if nbr in sus:
                        safe=False
                        return list(range(n))

        return [i for i in range(n) if i not in sus]


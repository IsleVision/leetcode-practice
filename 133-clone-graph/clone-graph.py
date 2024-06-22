"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root = Node(1,[])
        arr = [(node,root)]
        visited = {node:root}
        while arr:
            nd,nd_c = arr.pop()
            for nd_nei in nd.neighbors:
                if nd_nei not in visited:
                    nd_c_nei = Node(nd_nei.val,[])
                    visited[nd_nei] = nd_c_nei
                    arr += [(nd_nei,nd_c_nei)]
                else:
                    nd_c_nei = visited[nd_nei]
                nd_c.neighbors += [nd_c_nei] 
        return root



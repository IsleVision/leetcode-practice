"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        nds=[[root,0]]
        pre_nd=root
        pre_lvl=0
        while nds:
            nd,lvl=nds.pop(0)
            if not nd:
                continue
            if lvl==pre_lvl+1:
                pre_nd.next=None
                pre_lvl+=1
            else:
                pre_nd.next=nd
            pre_nd=nd
            nds+=[[nd.left,lvl+1],[nd.right,lvl+1]]
        pre_nd.next=None
        return root
        
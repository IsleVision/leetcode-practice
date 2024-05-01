"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        od_arr = [head]
        res = Node(head.val,None,None)
        new_arr = [res]
        hd = head
        while hd.next:
            hd = hd.next
            od_arr+=[hd]
            nd = Node(hd.val,None,None)
            new_arr[-1].next= nd
            new_arr+=[nd]
        for i in range(len(od_arr)):
            rd = od_arr[i].random
            if rd:
                idx = od_arr.index(rd)
                new_arr[i].random=new_arr[idx]
        return res
            

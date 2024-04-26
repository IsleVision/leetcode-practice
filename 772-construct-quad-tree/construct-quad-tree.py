"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        length = len(grid)
        if length==1:
            return Node(grid[0][0],True,None,None,None,None)
        else:
            lenh= length//2
            cnt_tl,arr_tl=0,[[0 for _ in range(lenh)] for _ in range(lenh)]
            cnt_tr,arr_tr=0,[[0 for _ in range(lenh)] for _ in range(lenh)]
            cnt_bl,arr_bl=0,[[0 for _ in range(lenh)] for _ in range(lenh)]
            cnt_br,arr_br=0,[[0 for _ in range(lenh)] for _ in range(lenh)]
            for i in range(length):
                for j in range(length):
                    val = grid[i][j]
                    if i<lenh and j<lenh:
                        if val==1:
                            cnt_tl+=1
                        else:
                            cnt_tl-=1
                        arr_tl[i][j]=val 
                    elif i<lenh and j>=lenh:
                        if val==1:
                            cnt_tr+=1
                        else:
                            cnt_tr-=1
                        arr_tr[i][j-lenh]=val 
                    elif i>=lenh and j<lenh:
                        if val ==1:
                            cnt_bl+=1
                        else:
                            cnt_bl-=1
                        arr_bl[i-lenh][j]=val 
                    else:
                        if val==1:
                            cnt_br+=1
                        else:
                            cnt_br-=1
                        arr_br[i-lenh][j-lenh]=val 
            lenh_sq=lenh**2
            if cnt_tl==cnt_tr==cnt_bl==cnt_br and (cnt_tl==lenh_sq or cnt_tl==-lenh_sq) :
                return Node(grid[0][0],True,None,None,None,None)
            else:
                return Node(False,False,self.construct(arr_tl),self.construct(arr_tr),self.construct(arr_bl),self.construct(arr_br))
            


        
        
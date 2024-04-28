# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        nds = [[root,0]]
        level=-1
        while nds:
            nd,lv=nds.pop(0)
            if lv==level:
                res[-1]+=[nd.val]
            else:
                res+=[[nd.val]]
                level=lv
            if nd.left:
                nds+=[[nd.left,lv+1]]
            if nd.right:
                nds+=[[nd.right,lv+1]]
        return res
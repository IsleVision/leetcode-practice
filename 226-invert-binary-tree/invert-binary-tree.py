# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return
        nds = [root]
        while len(nds):
            nd = nds.pop(0)
            if nd.left:
                nds +=[nd.left]
            if nd.right:
                nds+=[nd.right]
            if nd.left or nd.right:
                tmp=nd.left
                nd.left=nd.right
                nd.right=tmp
        return root
        
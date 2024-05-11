# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        nd = TreeNode(postorder[-1],None,None)
        length=len(postorder)
        if length==1:
            return nd
        idx=inorder.index(postorder[-1])
        if idx==length-1:
            nd.left = self.buildTree(inorder[:-1],postorder[:-1])
        elif idx==0:
            nd.right = self.buildTree(inorder[1:],postorder[:-1])
        else:
            nd.left = self.buildTree(inorder[:idx],postorder[:idx])
            nd.right = self.buildTree(inorder[idx+1:],postorder[idx:-1])
        return nd
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res =True
        arr=[]

        def search(root:TreeNode, arr:List[TreeNode]):
            nonlocal res
            if not root:
                return
            search(root.left,arr)
            if arr and root.val<=arr[-1]:
                res= False
            arr += [root.val]
            search(root.right,arr)
        
        search(root,arr)
        return res
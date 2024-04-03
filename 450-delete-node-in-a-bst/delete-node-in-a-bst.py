# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # def bst(root:TreeNode,root_par:TreeNode, key:int) -> Optional[TreeNode], Optional[TreeNode]:
        #     if not root:
        #         return None,root_par
        #     if root.val >key:
        #         return bst(root.left,root,key)
        #     elif root.val < key:
        #         return bst(root.right,root,key)
        #     else:
        #         return root,root_par

        # nd,nd_par = bst(root,None,key)
        # if not nd:
        #     return root
        # if not nd.left and not nd.right:
        #     if nd_par.val>nd.val:
        #         nd_par.left=None
        #     else:
        #         nd_par.right=None
        # if nd.left and not nd.right:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left 
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root




        
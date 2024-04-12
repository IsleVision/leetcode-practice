# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val>key:
            root.left= self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                nd=root.right
                nd_pre=None
                while nd.left:
                    nd_pre=nd
                    nd=nd.left
                nd.left=root.left
                if nd_pre:
                    if nd.right:
                        nd_pre.left=nd.right
                    else:
                        nd_pre.left=None
                    nd.right=root.right
                return nd
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #solution 1
        # if not preorder:
        #     return None
        # nd = TreeNode(preorder[0],None,None)
        # if not preorder[1:]:
        #     return nd
        # idx = inorder.index(preorder[0])
        # idx_n = inorder.index(preorder[1])
        # if idx==idx_n-1:
        #     nd.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        # else:
        #     nd.left =self.buildTree(preorder[1:idx+1],inorder[0:idx])
        #     nd.right=self.buildTree(preorder[idx+1:],inorder[idx+1:])
        # return nd

        #solution 2
        if not preorder:
            return None
        nd = TreeNode(preorder[0],None,None)
        length=len(preorder)
        if length==1:
            return nd
        idx = inorder.index(preorder[0])
        if idx==0:
            nd.right=self.buildTree(preorder[1:],inorder[1:])
        elif idx==length-1:
            nd.left=self.buildTree(preorder[1:],inorder[:-1])
        else:
            nd.left= self.buildTree(preorder[1:idx+1],inorder[:idx])
            nd.right=self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return nd
        


        

        
        
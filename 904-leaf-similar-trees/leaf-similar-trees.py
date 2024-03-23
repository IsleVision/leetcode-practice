# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def resolveLeaf(self, root):
        nd_arr = [[root,1]]
        leaves = []
        while nd_arr:
            nd_tmp,dep = nd_arr.pop()
            if nd_tmp.right:
                nd_arr +=[[nd_tmp.right,dep+1]]
            if nd_tmp.left:
                nd_arr +=[[nd_tmp.left,dep+1]]
            if not nd_tmp.left and not nd_tmp.right:
                leaves += [nd_tmp.val]
        return leaves


    def leafSimilar(self, root1, root2):
        return self.resolveLeaf(root1)==self.resolveLeaf(root2)
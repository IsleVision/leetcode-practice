# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nd_arr = [[root,root.val-1]]
        good = 0
        while nd_arr:
            nd,max_v = nd_arr.pop()
            if nd.val>=max_v:
                good +=1
                max_v=nd.val

            if nd.right:
                nd_arr += [[nd.right,max_v]]
            if nd.left:
                nd_arr +=[[nd.left,max_v]]
        
        return good


        
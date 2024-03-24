# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSum(self,root:Optional[TreeNode],targetSum:int)->int:
        res = 0
        nd_arr = [[root,0]]
        while nd_arr:
            [nd, sum_v]= nd_arr.pop()
            if not nd:
                continue
            sum_v += nd.val
            if sum_v==targetSum:
                res += 1
            nd_arr += [[nd.right,sum_v]]
            nd_arr += [[nd.left,sum_v]]
        return res

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res= 0
        if not root:
            return 0
        else:
            res= self.findSum(root,targetSum)
        res += self.pathSum(root.left,targetSum)
        res += self.pathSum(root.right,targetSum)
        return res

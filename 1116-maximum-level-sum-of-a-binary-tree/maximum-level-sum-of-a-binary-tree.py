# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        nd_arr = [[root,0]]
        res = []
        while nd_arr:
            [nd,dep]=nd_arr.pop(0)
            if not nd:
                continue
            if len(res)-1<dep:
                res +=[nd.val]
            else:
                res[dep] +=nd.val
            nd_arr+=[[nd.left,dep+1]]
            nd_arr+=[[nd.right,dep+1]]
        max_v=res[0]
        l = 1
        for i in range(len(res)):
            if res[i]>max_v:
                max_v=res[i]
                l=i+1
        return l





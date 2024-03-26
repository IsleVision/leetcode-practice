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
        max_v = root.val
        l=1
        while nd_arr:
            [nd,dep]=nd_arr.pop(0)
            if not nd:
                continue
            if len(res)-1<dep:
                if res and res[-1]>max_v:
                    max_v = res[-1]
                    l=dep
                res +=[nd.val]
            else:
                res[dep] +=nd.val
            nd_arr+=[[nd.left,dep+1]]
            nd_arr+=[[nd.right,dep+1]]
        if res[-1]>max_v:
            return len(res)
        else:
            return l





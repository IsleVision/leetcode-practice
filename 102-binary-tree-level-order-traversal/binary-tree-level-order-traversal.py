# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nds = [[0, root]]
        res = [[]]
        cur_level = 0
        while len(nds):
            level, nd = nds.pop(0)
            if nd.left:
                nds += [[level+1,nd.left]]
            if nd.right:
                nds += [[level+1, nd.right]]

            if level == cur_level:
                res[-1] += [nd.val]
            else:
                cur_level += 1
                res += [[nd.val]]
        return res


            




        
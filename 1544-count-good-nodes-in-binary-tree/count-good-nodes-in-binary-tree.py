# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nd_arr = [[root,1]]

        path = {}
        good = 1
        while nd_arr:
            nd,dep = nd_arr.pop()
            path[dep]=nd.val
            for i in range(1,dep,1):
                if path[i]>nd.val:
                    break
                if i==dep-1:
                    good+=1

            if nd.right:
                nd_arr += [[nd.right,dep+1]]
            if nd.left:
                nd_arr +=[[nd.left,dep+1]]
        
        return good


        
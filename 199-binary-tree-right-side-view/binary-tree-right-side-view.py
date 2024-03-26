# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nd_arr = [[root,0]]
        res = []
        dep_g=-1
        while nd_arr:
            [nd,dep]=nd_arr.pop(0)
            if not nd:
                continue
            if dep_g!=dep:
                res += [nd.val]
                dep_g=dep
            nd_arr +=[[nd.right,dep+1]]
            nd_arr +=[[nd.left,dep+1]]
        return res







        # not able to find left nodes in different branch    
        # self.res = []
        # self.dep_g=-1
        # self.stop=False
        # def dfs(root:TreeNode,dep):
        #     if not root:
        #         return
        #     if self.dep_g>=dep:
        #         self.stop=True
        #     self.dep_g =dep
        #     if not self.stop:
        #         self.res += [root.val]
        #     dfs(root.right,dep+1)
        #     dfs(root.left,dep+1)
        # dfs(root,0)    
        # return self.res




        
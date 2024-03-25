# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root == p or root==q:
            return root
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        if l and r:
            return root
        else:
            return l or r

















        # Not very efficient solution
        # def dfs_search(root:TreeNode)->int:
        #     hit = 0
        #     if not root:
        #         return 0
        #     if root == p or root == q:
        #         hit +=1
        #     if hit ==2:
        #         return 2
        #     hit += dfs_search(root.left)
        #     hit += dfs_search(root.right)
        #     return hit

        # def dfs_search(root:TreeNode)->int:
        #     hit = 0
        #     nd_arr = [root]
        #     while nd_arr:
        #         nd = nd_arr.pop()
        #         if not nd:
        #             continue
        #         if nd == p or nd == q:
        #             hit +=1
        #         if hit ==2:
        #             return True
        #         nd_arr += [nd.right]
        #         nd_arr += [nd.left]
        #     return False
    
        # dep=0
        # nd_arr = [[root,0]]
        # res = None
        # while nd_arr:
        #     [nd,dep_tmp]=nd_arr.pop(0)
        #     if nd==None:
        #         continue
        #     if not res or dep_tmp>dep and dfs_search(nd):
        #             res = nd
        #             dep = dep_tmp
        #     nd_arr += [[nd.left,dep_tmp+1]]
        #     nd_arr += [[nd.right,dep_tmp+1]]
        # return res
        
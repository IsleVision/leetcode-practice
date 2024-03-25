# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def resolveLengthDi(self,root:Optional[TreeNode], di:Optional[bool]=True)->int:
    #     nd = root
    #     leng = -1
    #     while nd:
    #         if di:
    #             nd = nd.left
    #         else:
    #             nd = nd.right
    #         di = not di
    #         leng+=1
    #     return leng

    # def resolveLength(self,root:Optional[TreeNode])->int:
    #     return max(self.resolveLengthDi(root,True),self.resolveLengthDi(root,False))

    # def longestZigZag(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     max_l = self.resolveLength(root)
    #     max_l = max(max_l, self.longestZigZag(root.left), self.longestZigZag(root.right))
    #     return max_l


    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def resolveLengthDi(root:Optional[TreeNode], di:Optional[bool]=True)->int:
            if not root:
                return 0
            nd = root
            leng = -1
            while nd:
                if di:
                    nd = nd.left
                else:
                    nd = nd.right
                di = not di
                leng+=1
            return leng
        
        max_l = 0
        nd_arr = [[root,resolveLengthDi(root,True),resolveLengthDi(root,False)]]
        while nd_arr:
            [nd,leng_l,leng_r] = nd_arr.pop()
            max_l = max(max_l,leng_l,leng_r)
            if nd!=None:
                nd_arr += [[nd.right,leng_l-1,resolveLengthDi(nd.right,False)]]
                nd_arr += [[nd.left,resolveLengthDi(nd.left,True),leng_r-1]]

        return max_l

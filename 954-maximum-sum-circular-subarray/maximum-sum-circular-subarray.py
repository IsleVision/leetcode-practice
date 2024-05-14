class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_v,max_res=0,0
        min_v,min_res=0,0
        max_n = nums[0]
        total=0
        for e in nums:
            if e>max_n:
                max_n=e
            total+=e
            max_v=max(max_v+e,e)
            max_res=max(max_v,max_res)
            min_v=min(min_v+e,e) 
            min_res=min(min_v,min_res)
        if total==min_res and max_res==0:
            return max_n
        return max(total-min_res,max_res)

            


        
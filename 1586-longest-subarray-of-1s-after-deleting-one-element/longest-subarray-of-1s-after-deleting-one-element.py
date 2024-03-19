class Solution(object):
    def longestSubarray(self, nums):
        l,r=0,0
        cnt_0=0
        max_cnt=0
        for r in range(len(nums)):
            if nums[r]==0:
                cnt_0+=1
            while cnt_0>1:
                l+=1
                if nums[l-1]==0:
                    cnt_0 -=1
            max_cnt = max(r-l,max_cnt)
        return max_cnt

        
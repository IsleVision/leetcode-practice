class Solution(object):
    def pivotIndex(self, nums):
        #solution1
        # for i in range(len(nums)):
        #     if sum(nums[:i])==sum(nums[i+1:]):
        #         return i
        # return -1

        #solution2
        sum_r = sum(nums)
        sum_l = 0
        for i in range(len(nums)):
            sum_r -= nums[i]
            sum_l += nums[i-1] if i>0 else 0
            if sum_r==sum_l:
                return i
        return -1


class Solution(object):
    def moveZeroes(self, nums):
        i,j = 0,0
        length = len(nums)
        for i in range(length):
            if nums[i] ==0:
                for j in range(i+1,length,1):
                    if nums[j]!=0:
                        nums[i]=nums[j]
                        nums[j]=0
                        break
        return nums   
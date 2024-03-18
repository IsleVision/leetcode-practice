class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        i,j=0,len(nums)-1
        cnt =0
        while i<j:
            if nums[i]+nums[j]==k:
                cnt +=1
                i+=1
                j-=1
            elif nums[i]+nums[j]>k:
                j-=1
            else:
                i+=1
        return cnt



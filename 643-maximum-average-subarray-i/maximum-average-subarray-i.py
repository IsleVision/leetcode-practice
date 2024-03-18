class Solution(object):
    def findMaxAverage(self, nums, k):
        i=1
        max_sum=sum(nums[0:k])
        cur_sum=sum(nums[0:k])
        for i in range(1,len(nums)-k+1,1):
            cur_sum= cur_sum+nums[i+k-1]-nums[i-1]
            max_sum= max(max_sum,cur_sum)
        return max_sum*1.0/k



        
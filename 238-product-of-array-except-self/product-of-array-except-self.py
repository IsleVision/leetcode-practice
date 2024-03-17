class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        res1 = [1]*length
        res2 = [1]*length
        res = [1]*length
        tmp = 1
        for i in range(1,length,1):
            res1[i] = tmp*nums[i-1]
            tmp = res1[i]
        tmp = 1    
        for i in range(length-2,-1,-1):
            res2[i] = tmp*nums[i+1]
            tmp = res2[i] 
            res[i]=res1[i]*res2[i]
        res[length-1]=res1[length-1]    
        return res



        
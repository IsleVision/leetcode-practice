class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        res1 = [1]*length
        res2 = [1]*length
        res = [1]*length
        tmp = 1
        for i in range(1,length,1):
            res1[i] = res1[i-1]*nums[i-1]
        tmp = 1    
        for i in range(length-2,-1,-1):
            res2[i] = res2[i+1]*nums[i+1]
            res[i]=res1[i]*res2[i]
        res[length-1]=res1[length-1]    
        return res



        
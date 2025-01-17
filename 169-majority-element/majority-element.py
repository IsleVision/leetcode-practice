class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1
        for k in dic:
            if dic[k] > len(nums)/2:
                return k

        
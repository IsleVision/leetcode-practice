class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length ==1:
            return nums[0]
        DP = [0 for _ in range(length)]
        DP[0]=nums[0]
        DP[1]=nums[0] if nums[0]>nums[1] else nums[1]
        for i in range(2,length):
            if DP[i-2]==DP[i-1]:
                DP[i]=DP[i-2]+nums[i]
            else:
                DP[i]=max(DP[i-2]+nums[i],DP[i-1])
        return DP[length-1]


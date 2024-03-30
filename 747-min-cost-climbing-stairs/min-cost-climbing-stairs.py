class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp=[0 for _ in range(length+2)]
        for i in range(length-1,-1,-1):
            dp[i] = cost[i]+ min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])
            

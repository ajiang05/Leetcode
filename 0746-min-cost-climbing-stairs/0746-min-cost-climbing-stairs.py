class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        We can either start at index 1 or 0 
        I am thinking that we need to use two dp because we can either start at 0 or 1
        dp[i] = min cost to get to index i

        dp_0 = len(cost)+1
        dp[0] = dp[0]
        dp[0] = dp[1]

        dp[i] = min(dp[i-1],dp[i-2])
        """
        if len(cost)==2:
            return min(cost)

        dp = [0]*(len(cost)+1)

        for i in range(2,len(cost)+1):
            dp[i] = min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        
        
        return dp[len(cost)]

            

        
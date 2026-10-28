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

        dp_0 = [0]*(len(cost)+1)
        dp_1 = [0]*(len(cost)+1)

        dp_0[0],dp_0[1] = cost[0],cost[1]+cost[0]

        dp_1[0], dp_1[1] = float('inf'),cost[1]

        for i in range(2,len(cost)+1):
            if i==len(cost):
                dp_0[i] = min(dp_0[i-1],dp_0[i-2])
                dp_1[i] = min(dp_1[i-1],dp_1[i-2]) 
                break
            dp_0[i] = cost[i]+min(dp_0[i-1],dp_0[i-2])
            dp_1[i] = cost[i]+min(dp_1[i-1],dp_1[i-2])

        
        
        return min(dp_0[-1],dp_1[-1])

            

        
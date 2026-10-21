class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        We have a choice of including a number and not including it
        We can do a recursive loop where we add a number of dont add it

        We can do nums*target

        dp[i][j] = is i numbers to get to j
        """
        dp = {}
        def dfs(curr_sum):
            combination = 0
            if curr_sum in dp:
                return dp[curr_sum]
            if curr_sum==target:
                return 1
            if curr_sum>target:
                return 0

            for n in nums:
                include = dfs(curr_sum+n)
                combination+=include
            
            dp[curr_sum] = combination
            
            return combination
        
        return dfs(0)
            

            
                


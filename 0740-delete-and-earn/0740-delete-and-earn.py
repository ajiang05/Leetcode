class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        We can create a dictonary and map number to frequency
        You can either delete a number or not delete it
        We can sort the nums
        """

        points = [0]*(max(nums)+1)
        dp = [0]*len(points)
        
        for n in nums:
            points[n]+=n
        
        dp[0] = 0
        for i in range(1,len(points)):
            if i>=2:
                dp[i] = max(dp[i-1],points[i]+dp[i-2])
            else:
                dp[i] = max(dp[i-1],points[i])
            
        return dp[-1]
        
        
        
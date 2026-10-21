class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Houses next to each other cant be robbed
        First one is neighbor with the last one

        We have a choice of robbing a house or skipping it 
        if we choose first then we cant choose last
        if we choose last we cant choose first

        dp[i] = max(amount of money we can get)
        dp = len(nums)*[0]

        dp[i] = max(dp[i-1],nums[i]+dp[i-2],num[i]+dp[i-3])

        Lets do it with no circle then modify
        """
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        dp = [0]*(len(nums)-1)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        dp2 = [0]*len(nums)
        dp2[0] = 0
        dp2[1] = nums[1]

        #exclude last house
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        
        #exclude first house
        for i in range(2,len(nums)):
            dp2[i] = max(dp2[i-1],nums[i]+dp2[i-2])
        
        return max(dp[-1],dp2[-1])


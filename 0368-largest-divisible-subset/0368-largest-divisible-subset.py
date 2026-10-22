class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        """
        """
        dp = [[] for _ in range(len(nums))]
        sort = sorted(nums)

        dp[-1] = [sort[-1]]

        for i in range(len(sort)-2,-1,-1):
            longest = [sort[i]]
            for j in range(len(sort)-1,i,-1):
                if dp[j][-1]%sort[i]==0:
                    curr_long = dp[j]+[sort[i]]
                    if len(curr_long)>len(longest):
                        longest = curr_long
            dp[i] = longest
        
        result = []
        for i in range(len(dp)):
            if len(dp[i])>len(result):
                result = dp[i]
        
        return result



                    


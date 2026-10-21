class Solution:
    def numSquares(self, n: int) -> int:
        """
        This is similar to coin exchange where we have to use perfect squares
        """
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        perf = []

        
        for i in range(1,n+1):
            sqrt = math.isqrt(i)
            if sqrt*sqrt==i:
                perf.append(i)
        
        print(perf)
        
        for i in range(2,len(dp)):
            for p in perf:
                #We want to see the number of coins to make diff
                diff = i-p
                if diff>=0:
                    dp[i] = min(dp[diff]+1,dp[i])
                else:
                    break
        
        return dp[-1]
            

            

        

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        """
        I am thinking of doing dp here
        dp[i] = min at that path
        
        old = [2,1,3]
        new = [7,6,]

        [2,1,3],
        [6,5,4],
        [7,8,9]
        ]
        """
        
        n = len(matrix)
        dp = [0]*n

        if n==1:
            return matrix[0][0]

        for r in range(n):
            new_dp = [0]*n
            for c in range(n):
                val = matrix[r][c]
                if c==0:
                    new_dp[c] = min(dp[c],dp[c+1])+val
                elif c==n-1:
                    new_dp[c] = min(dp[c],dp[c-1])+val
                else:
                    new_dp[c] = min(dp[c],dp[c-1],dp[c+1])+val
            
            dp = new_dp
        
        return min(dp)


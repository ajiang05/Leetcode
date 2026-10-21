class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        aaaaa *...

        The hard part is the * we need to somehow know how many letters to choose
        The length s has to be greater than or equal to p

        We have the choice of including characters or not including it
        Im thinking of a stack+dp 

        is the string equal at index s and index p

        dp[s][p] = if we can form the string at index s and at index p
        dp[s-1][p] = True and p matches letter 

        """
        ROW = len(s)
        COL = len(p)

        dp = [[False]*(COL+1) for _ in range(ROW+1)]
        dp[0][0] = True
        
        for i in range(2,COL+1):
            if p[i-1]=='*':
                dp[0][i] = dp[0][i-2]

        for r in range(1,ROW+1):
            for c in range(1,COL+1):
                curr_p = p[c-1]
                curr_s = s[r-1]
                
                if curr_p=="." or curr_p==curr_s:
                    dp[r][c] = dp[r-1][c-1]
                    continue

                elif curr_p=="*":
                    prev = p[c-2]

                    #empty string
                    dp[r][c] = dp[r][c-2]

                    #Case with .* or a*
                    if prev==curr_s or prev==".":
                        dp[r][c] = dp[r-1][c] or dp[r][c]
                        
        
        return dp[-1][-1]
            

                

      

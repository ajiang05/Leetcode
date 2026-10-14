class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        dp = len(s)
        dp[i] = number of words
        We can iterate through string s and once we get to a word we can mark that there is a word at that index

        For dp we have choices of including a word and not including a word

        dp[i] represents if we can create word at dp[i]
        We can do recursion too

        We can have a function where we take in left and right pointer
        if we can create with left and right we pass recursive l
        if we hit r = len(s)-1 and we can create word we return true
        else we return false
        """
        #dp represents if we can segment from 0 to i 
        words = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        
        return dp[-1]


            
        
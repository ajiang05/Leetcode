class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        We can have each index start as center
        then we can expand out
        """
        def expand(l,r):
            count = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count

        result = 0
        for i in range(len(s)):
            result+=expand(i,i)
            result+=expand(i,i+1)
        
        return result
            
    

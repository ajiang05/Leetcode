class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We have a set and we add and remove from it
        
        If we hit something in the set we remove until we hit that same letter from the left
        """
        letters = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in letters:
                longest = max(longest,r-l+1)
                letters.add(s[r])
            else:
                while s[l]!=s[r]:
                    letters.remove(s[l])
                    l+=1
                l+=1
        
        return longest
                    
       
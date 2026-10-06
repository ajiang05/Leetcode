class Solution:
    def countCommas(self, n: int) -> int:
        """
        1-999 is zero commas - length 1-3 is zero
        1,000-999,999 is 1 comma - length 4-6 is 1
        1,000,000 - 999,999,999 -length 7-9 is two

        if len(n)//2 == 0 or 1 then zero
        if len(n)//2 = 2 or len(n)//2 remainder 1 or len(n)//2==3 then 1
        if len(n)//2 = 3 remainder 1 or len(n)//2 = 4 or len(n)//2 = 4 remainder 1 then 2
        if len(n)//2 = 5 or len(n)//2 remainder
        """
        result=0
        curr = 1000
        
        while curr<=n:
            result+=n-curr+1
            curr*=1000
        
        return result
            
        
        return result
            
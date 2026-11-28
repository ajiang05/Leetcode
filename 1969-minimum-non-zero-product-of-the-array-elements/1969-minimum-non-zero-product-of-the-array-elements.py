class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        """
        1 -> 0001
        2 -> 0010
        3 -> 0011
        4 -> 0100
        5 -> 0101
        6 -> 0110
        7 -> 0110
        We have left pointer and right pointer We always want to find pair for smallest
        """
        r = (2**p)-1
        mod = 10**9+7

        pairs = r//2

        return (pow(r-1,pairs,10**9+7)*r)%mod

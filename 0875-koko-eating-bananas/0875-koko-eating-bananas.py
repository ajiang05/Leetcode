class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        We want to find the minimum k bananas that koko eats.

        len(piles)<=h

        WE can do 1 to max(piles)

        We need to find minimum banaas once we find one that equals h=value we set it equal
        if the number of hours is greater than h we top hald and if it is less than or equal to we check bottom half 
        """
        l = 1
        r = max(piles)

        """
        [1,2,3,4,5,6,7,8,9,10,11]
        """

        while l<r:
            mid = (l+r)//2
            eating_time  = sum([math.ceil(pile/mid) for pile in piles])

            if eating_time>h:
                l = mid+1
            elif eating_time<=h:
                r = mid
        
        return l
        





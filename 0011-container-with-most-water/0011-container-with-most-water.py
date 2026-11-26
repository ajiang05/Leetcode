class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        We have a left and right pointer 
        We move the smaller one inside
        """
        l = 0 
        r = len(height)-1
        max_water = 0

        while l<r:
            max_water = max(max_water,(r-l)*min(height[l],height[r]))

            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        
        return max_water
        
            

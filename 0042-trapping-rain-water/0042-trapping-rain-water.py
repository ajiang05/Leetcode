class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Sliding window
        We need to check left and right 
        if left is greater and right is less we can start a while loop 

        while r<len(height):
            We check that it is less than left and once it is greater we add the total water

        This doesnt work for the case where the elevation is decreasing

        water[i] = min(left,right)-height[i]

        You have to use sort of a prefix here where we have left
        """
        l = 0
        r = len(height)-1
        rightMax, leftMax = 0,0
        water = 0

        while l<r:
            rightMax = max(height[r],rightMax)
            leftMax = max(height[l],leftMax)

            if leftMax<=rightMax:
                water+=(leftMax-height[l])  
                l+=1 
            else:
                water+=(rightMax-height[r])
                r-=1
                
        
        return water
        

        
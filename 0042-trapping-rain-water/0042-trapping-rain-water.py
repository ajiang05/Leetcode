class Solution:
    def trap(self, height: list[int]) -> int:
        """
        We want the max for forward and backwards
        """
        n = len(height)
        forward = [0]*n
        backward = [0]*n

        max_f = 0
        max_b = 0
        for i in range(0,n):
            max_f = max(max_f,height[i])
            forward[i] = max_f

            max_b = max(max_b,height[n-i-1])
            backward[n-i-1] = max_b
        
        print(forward)
        print(backward)
        water = 0
        for i in range(1,n-1):
            min_h = min(forward[i],backward[i])
            if height[i]<min_h:
                water+=(min_h-height[i])
        
        return water

        """
        [2,4,1,2
        [4,4,4,4,4,5]
        [5,5,5,5,5,5]
        """


        
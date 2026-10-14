class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        We can create a prefix array foward and one backward
        [-1,-2,-1]
        """
        seen = {0:1}
        prefix = 0
        result = 0

        for i in range(len(nums)):
            prefix+=nums[i]

            if prefix-k in seen:
                result+=seen[prefix-k]
            
            seen[prefix] = 1+seen.get(prefix,0)
        
        return result

        
       



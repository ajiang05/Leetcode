class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        We have a dict and keep track of freq of the num and we have number:indice
        """
        indices = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in indices:
                return [i,indices[diff]]
            else:
                indices[nums[i]] = i
        
        return []
      
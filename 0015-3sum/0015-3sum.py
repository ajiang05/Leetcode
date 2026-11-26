class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        We know that nums[i]+nums[j] = -nums[k]
        We can do a double for loop try every single combination and check

        We do a nested for loop
        The outer loop is target:
            The inner loop is the loop for two sum
                We check by ordering it and putting in tuple
                If not in seen:
                    We add it to result
        """
        
        seen = set()
        result = []

        nums.sort()

        for i in range(len(nums)):
            target = nums[i]*-1
            diff = {}

            if i>0 and nums[i]==nums[i-1]:
                continue
                
            for j in range(i+1,len(nums)):
                if target-nums[j] in diff:
                    trips = [target*-1,nums[j],target-nums[j]]
                    tuple_trips = tuple(sorted(trips))
                    if tuple_trips in seen:
                        continue
                    else:
                        seen.add(tuple_trips)
                        result.append(trips)
                else:
                    diff[nums[j]] = j
        
        return result



        
        
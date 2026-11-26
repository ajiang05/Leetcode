class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        [2,3,4,5,6,1]
        Binary search
        We check if left is less than mid if it is we know it is sorted
        If target is less than mid 
            We know that first half is sorted 
        else:
            We know that second half is sorted
        """
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if target==nums[mid]:
                return mid

            #left is sorted
            if nums[l]<=nums[mid]:
                if target>=nums[l] and target<nums[mid]:
                    r = mid-1
                else:
                    l =mid+1
            else:
                if target>nums[mid] and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
                



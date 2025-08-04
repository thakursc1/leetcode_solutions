# Last updated: 03/08/2025, 21:33:27
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        left = 0 
        right = len(nums)

        left_idx = -1
        while left<right:
            mid = left+ (right -left)//2 

            if nums[mid] >= target:
                right = mid 
                if nums[mid] == target:
                    left_idx = mid 
            else:
                left = mid + 1

        right_idx = -1
        left = 0
        right = len(nums)
        while left<right:
            mid = left+ (right -left)//2 
            if nums[mid] <= target:
                left = mid+1
                if nums[mid]==target:
                    right_idx = mid
            else:
                right = mid
        
        return [left_idx, right_idx]

        
        


# Last updated: 03/08/2025, 08:59:31
class Solution:
    def search(self, nums: List[int], target: int) -> int:


        left = 0 
        right = len(nums)

        while left < right : 

            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left= mid+1
            else:
                right = mid 
        
        return -1 


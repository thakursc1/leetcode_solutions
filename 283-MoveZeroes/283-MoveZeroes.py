class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        find_non_zero = 0
        swap_ptr = 0 

        while find_non_zero <len(nums):
            while find_non_zero < len(nums) and nums[find_non_zero]==0:
                find_non_zero+=1
            if find_non_zero < len(nums):
                nums[swap_ptr], nums[find_non_zero] = nums[find_non_zero], nums[swap_ptr]
                find_non_zero+=1
                swap_ptr+=1
        



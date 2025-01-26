class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prod = 1
        ans = [1]
        for i in range(1, len(nums)):
            prod*=nums[i-1]
            ans.append(prod)
        
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod*=nums[i+1]
            ans[i]*=prod
        
        return ans

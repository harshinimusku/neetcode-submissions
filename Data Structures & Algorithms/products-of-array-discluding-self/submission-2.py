class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [0] * len(nums)
        left = 1
        right = 1
        right_product = [0] * len(nums)
        ans = [1] * len(nums)
        for i in range(len(nums)):
            
            left *= nums[i]
            left_product[i] = left
           
            right *= nums[len(nums) - i - 1]
            right_product[len(nums) - i - 1] = right
        for i in range(len(nums)):
            if i > 0:
                ans[i] *= left_product[i-1]
            if i < len(nums) - 1:
                ans[i] *= right_product[i+1]
         
   
        return ans


        
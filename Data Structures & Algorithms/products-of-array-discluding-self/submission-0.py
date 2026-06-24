class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length  # Initialize the result array with 1s
        
        # 1. Calculate prefix products (everything to the left)
        left_product = 1
        for i in range(length):
            res[i] = left_product
            left_product *= nums[i]
            
        # 2. Calculate suffix products (everything to the right) and multiply
        right_product = 1
        for i in range(length - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
            
        return res
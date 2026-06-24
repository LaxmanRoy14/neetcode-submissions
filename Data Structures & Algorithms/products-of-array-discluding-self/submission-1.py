class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length
        
        left_product = 1
        for i in range(length):
            res[i] = left_product
            left_product *= nums[i]
            
        right_product = 1
        for i in range(length - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
            
        return res
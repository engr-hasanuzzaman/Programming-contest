# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        product_left = 1
        # calculte product of left elements
        for i, n in enumerate(nums):
            products.append(product_left)
            product_left *= nums[i]
        
        product_right = 1
        # multiply left elements product with right element's product
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= product_right
            product_right *= nums[i]
        return products

# https://leetcode.com/problems/product-of-the-last-k-numbers/

# observation: since we are keeping product of last n elements, if we get value 0
# we will make array empty indicating we will get zero product otherwise
# keep calculate and keep first n numbef of producit in array
# [2,4,7,1,-3] -> [2, 8, 56, 56, -168] so for last k elements arr[-1] // arr[-(k+1)] will be result
class ProductOfNumbers:

    def __init__(self):
        self.product = []

    def add(self, num: int) -> None:
        if num == 0:
            self.product = []
            return
    
        if not self.product:
            self.product.append(num)
        else:
            self.product.append(self.product[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.product) == 0 or k > len(self.product):
            return 0
    
        if k == len(self.product):
            return self.product[-1]
        return self.product[-1] // self.product[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
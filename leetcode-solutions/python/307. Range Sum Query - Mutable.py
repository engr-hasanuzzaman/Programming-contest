# https://leetcode.com/problems/range-sum-query-mutable/
# use fenwick/binary indexed tree to solve this problem
# bit is for good for calculate sum query for one and two dimention array
# this is one based implementation
# n & -n extract last set bit to remaining part so 10: 1010 10 & -10 is 2(10)
# here adjustment is reset the lower set bit that is equvalent to
# i = i - (i & -i) i minux lower set bit that is reset lower set bit
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.size = len(nums)
        # one base int that's way size+1
        self.bit = [0 for _ in range(self.size+1)]
        for i in range(1, self.size+1):
          self._add(i, nums[i-1])

    def update(self, index: int, val: int) -> None:
      diff = val - self.nums[index]
      self.nums[index] = val
      # one base index: index+1
      self._add(index+1, diff)
        

    def sumRange(self, left: int, right: int) -> int:
      # since we want to include left that's why calling left
      return self._sum(right+1) - self._sum(left)
        
    def _sum(self, i):
      res = 0
      while i > 0:
        res += self.bit[i]
        i -= self._lowbit(i)
      return res
    
    def _lowbit(self, x):
      return x & -x
    
    def _add(self, i, val):
      while i <= self.size:
        self.bit[i] += val
        i += self._lowbit(i)


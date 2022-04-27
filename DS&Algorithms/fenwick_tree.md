#
- The intution of this DS is, every number can be represent as the sum of binary powere. Ex. 1 = 0 + 2^0, 2 = 0 + 2^1, 7 = 2^2 + 2^1+2^0. We will store sum in this interval so, to get total sum the time complexity will be O(logn)
- reset the right most set is `n -= n & (-n)` or `x & (x -1)`
- `n -= n & (-n)` means - and `n` with `2s complement of n` then substrack from `n` which will give the next parent element
- `n + n & (-n)` means `& n` with `2s complement of n` then sum with `n` which will give the next element to update
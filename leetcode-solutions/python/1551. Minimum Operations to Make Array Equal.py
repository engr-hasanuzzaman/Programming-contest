# https://leetcode.com/problems/minimum-operations-to-make-array-equal/

# first solution
# we need to convert all the number to the mean of the given array integers
# if n is odd then mean is the middle number otherwise mean of middle two numbers
class Solution:
    def minOperations(self, n: int) -> int:
        half = n // 2
        ans = 0
        i = n % 2 + 1
        for _ in range(half):
            ans += i
            i += 2
        return ans

class Solution:
    def minOperations(self, n: int) -> int:
        #  If length of an array (n) is even then, the Answer is sum of first n/2 odd numbers.
        #  eg. If n=6, then Answer is sum of first 3 (n/2) odd numbers. ie. 1,3,5.
        #  Formula for "Sum of first n odd numbers = n^2 "

        #   If the length of an array (n) is odd then, the Answer is sum of first n/2 even numbers.
        #   if n=7, then Answer is sume of first 3 (n/2) even numbers. ie. 2,4,6
        #   Formula for "Sum of first n even numbers = n(n+1) "
        half = n // 2
        if n % 2 == 0:
            return half * half
        else:
            return half * (half + 1)
        
        
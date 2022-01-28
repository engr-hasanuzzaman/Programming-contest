# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = odd_count = even_count = 0
        odd_sum_count = 0
        
        for n in arr:
            cur_sum += n
            if cur_sum % 2 == 1:
                odd_sum_count += even_count + 1
                odd_count += 1
            else:
                odd_sum_count += odd_count
                even_count += 1
        return odd_sum_count % (pow(10, 9) + 7)

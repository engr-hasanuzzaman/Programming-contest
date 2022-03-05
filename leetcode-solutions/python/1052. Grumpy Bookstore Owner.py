# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur_num = 0
        max_num = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                cur_num += customers[i]
        max_num = cur_num
        # tracking max disappointed range within minutes size
        left = 0
        right = minutes - 1
        for i in range(minutes, len(customers)):
            # adjust the counter
            if grumpy[i-minutes] == 1:
                cur_num = cur_num - customers[i-minutes]
    
            # add the new number
            if grumpy[i] == 1:
                cur_num = cur_num + customers[i]
                
            if cur_num > max_num:
                max_num = cur_num
                left = i - minutes + 1
                right = i
        number = 0
        for i in range(len(customers)):
            if grumpy[i] == 0 or (i >= left and i <= right):
                number += customers[i]
        return number

# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        ans = [0] * size
        num_of_one = 0
        if boxes[0] == '1':
            num_of_one += 1
        
        for i in range(1, size):
            ans[i] += ans[i - 1] + num_of_one
            if boxes[i] == '1':
                num_of_one += 1

        num_of_one = 0
        if boxes[-1] == '1':
            num_of_one += 1
        temp = [0] * size
        for i in range(size - 2, -1, -1):
            temp[i] += temp[i + 1] + num_of_one
            ans[i] += temp[i + 1] + num_of_one
            if boxes[i] == '1':
                num_of_one += 1
            
        return ans

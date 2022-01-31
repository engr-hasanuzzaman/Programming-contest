# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i, o in enumerate(operations):
            if o == 'X++' or o == '++X':
                x += 1
            else:
                x -= 1
        return x

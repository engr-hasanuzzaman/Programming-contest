# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
import math

# wrong solution for 
# Input
# "(()))(()))()())))"
# Output 1, Expected 4
# why, when go left to right it will need 4 insertion but if we use stack from last to first
# it will give a wrong answer
class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        for i in range(len(s)-1, -1, -1):
            p = s[i]
            if p == '(':
                # print("before ", count)
                count += self.pop_and_count(stack)
                # print("after ", count)
            else:
                stack.append(p)
        if stack != []:
            if stack[0] == '(':
                count += len(stack) * 2
            else:
                count += math.ceil(len(stack) / 2)
                if len(stack) % 2 != 0:
                    count += 1
        return count
                              
    def pop_and_count(self, stack):
        if stack == []:
            return 2
        if len(stack) == 1:
            stack.pop();
            return 1
        else:
            stack.pop()
            stack.pop()
            return 0
        
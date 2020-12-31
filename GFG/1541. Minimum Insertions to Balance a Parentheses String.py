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
        bal = 0 
        adjust = 0
        for c in s:
            if c == '(':
                bal += 2 # bal means how many ) we need to balance
                # if every thing went well ball should be even => for ex. ()(
                # bal is 1 so, insert ) and increment adjustment and decrease balance
                # to make it ())( {last extra ( will calculate finally be because we do not know yet                   #                 what will come next}
                if bal % 2 == 1:
                    adjust += 1
                    bal -= 1
            else:
                bal -= 1
                if bal < 0:
                    # encounder ) before ( so need to insert missing (
                    # since ( means two bal increment balance by 2
                    adjust += 1 
                    bal += 2
        return bal + adjust

        
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bag = []
        def inner(string, openC, closedC, n):
            nonlocal bag
            if openC == closedC == n:
                bag.append(string)
                return
            
            if closedC > openC or openC > n or closedC > n:
                return
            # put parenthesis in the correct order, so when both will be size n, will get the 
            # expected string
            inner(string + "(", openC + 1, closedC, n)
            inner(string + ")", openC, closedC + 1, n)
        
        inner("", 0, 0, n)
        
        return bag
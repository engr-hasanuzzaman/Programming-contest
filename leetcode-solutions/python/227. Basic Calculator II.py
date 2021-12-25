# https://leetcode.com/problems/basic-calculator-ii/

import re
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        d = deque()
        i = 0
        s = s.replace(' ', '')
        s = re.split(r'(\D)', s)
        size = len(s)
        while i < size:
            c = s[i]
            if c == '':
                i += 1
                continue
            if c == '*':
                res = int(d.pop()) * int(s[i+1])
                d.append(res)
                i += 1
            elif c == '/':
                res = int(d.pop()) // int(s[i+1])
                d.append(res)
                i += 1
            else:
                d.append(c)
            i += 1
        if len(d) == 1:
            return d.pop()
        
        while len(d) > 1:
            n1 = int(d.popleft())
            op = d.popleft()
            n2 = int(d.popleft())
            if op == '+':
                res = n1 + n2
            else:
                res = n1 - n2
            d.appendleft(res)
        return d.pop()
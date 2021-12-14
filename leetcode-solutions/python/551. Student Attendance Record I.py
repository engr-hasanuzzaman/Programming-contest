# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        cons_late = 0
        abs_count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                cons_late += 1
            elif s[i] == 'A':
                abs_count += 1
                cons_late = 0
            else:
                cons_late = 0
            
            if abs_count >= 2 or cons_late >= 3:
                return False
        return True

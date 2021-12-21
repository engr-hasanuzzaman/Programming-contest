# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i = 0
        size = len(seats)
        ans = 0
        while i < size:
            ans += abs(seats[i] - students[i])
            i += 1
        return ans

# https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1/#

class Solution:
    def median(self, matrix, r, c):
        min_num = float('inf')
        max_num = float('-inf')
        for row in range(r):
            min_num = min(min_num, matrix[row][0])
            max_num = max(max_num, matrix[row][c-1])

        target_number = (r * c + 1) // 2  # <= target_number
        while min_num < max_num:
            mid = min_num + (max_num - min_num) // 2
            count = 0
            for row in range(r):
                count += bisect_right(matrix[row], mid)

            # if we have enought elements it could be our potential result
            if count >= target_number:
                max_num = mid
            else:
                min_num = mid + 1

        return min_num

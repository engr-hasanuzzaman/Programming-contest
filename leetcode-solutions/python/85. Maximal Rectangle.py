# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        col_heights = [0] * len(matrix[0])

        # calculate column height for each row and call max-area history gram
        # calculate max area for each row and return max area
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    col_heights[j] += 1
                else:
                    col_heights[j] = 0
            max_area = self.max_area_histogram(col_heights, max_area)
        return max_area

    def max_area_histogram(self, nums, cur_max):
        stack = []
        size = len(nums)
        for i in range(size):
            num = nums[i]
            while stack and stack[-1][0] > num:
                n, idx = stack.pop()
                # we have lower bound
                if stack:
                    cur_max = max(cur_max, (i - stack[-1][1] - 1) * n)
                else:
                    # have no smaller size, so consider all previous element
                    cur_max = max(cur_max, i * n)
            stack.append((num, i))
        # process remaing elements which does not have min on the right size/all max in
        while stack:
            n, _ = stack.pop()
            if stack:
                cur_max = max(cur_max, (size - stack[-1][1] - 1) * n)
            else:
                # print(f"--max {i}")
                # have no smaller size, so consider all previous element
                cur_max = max(cur_max, size * n)
        # print("---final max is ", cur_max)
        return cur_max

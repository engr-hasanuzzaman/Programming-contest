# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we will calculate max areay for each col considering all the neighbors height >= that item
        # so, we need to know the index of smller hight from left and right side
        # maintain and stack with increasing order with index
        # we will calculate area that include the element's entire height
        stack = [0]
        max_area = heights[0]

        # ways: 2
        # adding min numb to ensure all the stack will be processing here
        heights.append(-1)
        for i in range(0, len(heights)):
            # remove all the larger elemtn from top as we need min elemnt's index
            while stack and heights[stack[-1]] > heights[i]:
                # the element that is on top, for which current is smaller element in the right
                # and next stack element is the smaller element in the left. So, we can canculate area
                # of the stack element
                cur_idx = stack.pop()
                if stack:
                    max_area = max(
                        max_area, (i - stack[-1] - 1) * heights[cur_idx])
                else:
                    # all the prvious number was > ith number
                    max_area = max(max_area, i * heights[cur_idx])
            # push the current
            stack.append(i)

        # ways 1: 1, 2, 3 process the remaining elements in stack
        # process the remainig number which is stored in increasint number
        # we know that, all the element in stack does not have smaller element on right
        # max_idx = len(heights)
        # while stack:
        #     cur_idx = stack.pop()
        #     if stack:
        #         max_area = max(max_area, (max_idx - stack[-1] - 1) * heights[cur_idx])
        #     else:
        #         # all the prvious number was > ith number
        #         max_area = max(max_area, max_idx * heights[cur_idx])
        return max_area

# https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1/?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions#

class Solution:

    # Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self, a, n):
        stack = []
        spans = []
        for price in a:
            cur_span = 1
            while stack and stack[-1][0] <= price:
                cur_span += stack.pop()[1]
            stack.append((price, cur_span))
            spans.append(cur_span)
        return spans

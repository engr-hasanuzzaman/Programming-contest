# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda job: -job.profit)
        slots = [False] * n
        count = 0
        total_profit = 0
        for job in Jobs:
            slot = min(n, job.deadline) - 1
            while slot > 0 and slots[slot] != False:
                slot -= 1

            if not slots[slot]:
                count += 1
                total_profit += job.profit
                slots[slot] = True
        return count, total_profit

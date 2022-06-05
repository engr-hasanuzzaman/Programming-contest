class Solution:
    def overlappedInterval(self, Intervals):
        # sort by start time
        Intervals.sort(key=lambda i: i[0])
        ans = Intervals[0:1]
        N = len(Intervals)
        for i in range(1, N):
            if Intervals[i][0] <= ans[-1][1]:
                ans[-1][0] = min(Intervals[i][0], ans[-1][0])
                ans[-1][1] = max(Intervals[i][1], ans[-1][1])
            else:
                ans.append(Intervals[i])
        return ans

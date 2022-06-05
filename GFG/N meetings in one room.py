class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        meetings = [Meeting(start[i], end[i]) for i in range(n)]
        meetings.sort()

        cur_meeting = meetings[0]
        ans = 1
        for i in range(1, n):
            meeting = meetings[i]

            if meeting.start > cur_meeting.end:
                cur_meeting = meeting
                ans += 1
        return ans


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __eq__(self, other):
        return self.end == other.end

    def __reps__(self):
        return str(self.start) + "-" + str(self.end)

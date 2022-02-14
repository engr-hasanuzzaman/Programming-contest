# https://leetcode.com/problems/meeting-rooms/

=begin
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
=end

# @param {Integer[][]} intervals
# @return {Boolean}
def can_attend_meetings(intervals)
    sorted_intervals = intervals.sort_by{|a| a.first }
    (intervals.size - 1).times do |i|
        if sorted_intervals[i+1][0] < sorted_intervals[i][1]
            return false 
        end
    end
    
    true
end
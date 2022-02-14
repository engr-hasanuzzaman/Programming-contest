# https://leetcode.com/problems/meeting-rooms-ii/
# https://leetcode.com/problems/meeting-rooms-ii/
=begin
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
=end

require 'algorithms'
include Containers
# @param {Integer[][]} intervals
# @return {Integer}
def min_meeting_rooms(intervals)
    min_heap = MinHeap.new
    sorted_intervals = intervals.sort_by{|start, _| start}
    room_counter = 0
    
    sorted_intervals.each do |start_time, end_time|
        if !min_heap.min || (min_heap.min && min_heap.min > start_time)
            min_heap << end_time
            room_counter += 1
        else
            min_heap.pop
            min_heap << end_time
        end
    end
    
    room_counter
end


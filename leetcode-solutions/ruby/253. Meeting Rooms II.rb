# https://leetcode.com/problems/meeting-rooms-ii/

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


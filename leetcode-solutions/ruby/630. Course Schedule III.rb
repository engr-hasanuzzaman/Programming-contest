# https://leetcode.com/problems/course-schedule-iii/

# LTE with ruby Algorithms
# sort the courses with last days because we have to process course which has
# shorter end date. Iterate each course, keep current spend time by adding duration
# If any point current_time + duration > end_time, check whether removing course from already process list, is there any course whice took more time then the current course, remove that and pick this course.
# Finally, all the possible course will be present on the queue
require 'algorithms'
include Containers
# @param {Integer[][]} courses
# @return {Integer}
def schedule_course(courses)
  # sort by lastday as only way to include item complete within last days
  courses.sort_by! { |c| c.last }
  last_complete_time = 0
  max_heap = MaxHeap.new
  courses.each do |dur, last|
    if last_complete_time + dur <= last
      last_complete_time += dur
      max_heap << dur
    elsif max_heap.size > 0 && max_heap.max > dur
      # remove course which took largest amount of time
      last_complete_time += dur - max_heap.pop
      max_heap << dur
    end
  end
  max_heap.size
end

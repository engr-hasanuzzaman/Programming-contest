# https://leetcode.com/problems/course-schedule-iii/
# sort the courses with last days because we have to process course which has
# shorter end date. Iterate each course, keep current spend time by adding duration
# If any point current_time + duration > end_time, check whether removing course from already process list, is there any course whice took more time then the current course, remove that and pick this course.
# Finally, all the possible course will be present on the queue
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pop = heapq.heappop
        push = heapq.heappush
        heap = []
        heapq.heapify(heap)
        courses.sort(key=lambda course: course[1])
        time = 0
        for duration, last_day in courses:
            if time + duration <= last_day:
                push(heap, -duration)
                time += duration
            elif heap and -heap[0] > duration:
                time += duration + pop(heap)
                push(heap, -duration)
        return len(heap)

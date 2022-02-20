# https://leetcode.com/problems/maximum-performance-of-a-team/

require "algorithms"
include Containers

# @param {Integer} n
# @param {Integer[]} speed
# @param {Integer[]} efficiency
# @param {Integer} k
# @return {Integer}
def max_performance(n, speed, efficiency, k)
    sum_of_speed = 0
    max_performance = 0
    min_heap = MinHeap.new
    performances = efficiency.zip(speed).sort_by{|e| -e.first }
    
    performances.each do |performance|
        if min_heap.size > k - 1
            sum_of_speed -= min_heap.pop
        end
        sum_of_speed += performance.last
        min_heap.push(performance.last)
        max_performance = [max_performance, sum_of_speed * performance.first].max
    end
    
    max_performance % (10**9+7)
end

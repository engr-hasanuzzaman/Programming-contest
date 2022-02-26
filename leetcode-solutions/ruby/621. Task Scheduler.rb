# https://leetcode.com/problems/task-scheduler/

# @param {Character[]} tasks
# @param {Integer} n
# @return {Integer}
def least_interval(tasks, n)
    task_freq = Array.new(26){0}
    tasks.each do |task|
        task_freq[task.ord - 'A'.ord] += 1
    end
    
    task_freq.sort!
    max_freq = task_freq.last
    # if we do not have any other task
    max_idle_time = (max_freq - 1) * n
    
    # now remove other task frequency from idle task count at max (max_freq - 1) as this is the
    # maximum idle time we have
    24.downto(0) do |i|
        max_idle_time -= [task_freq[i], max_freq - 1].min
    end
    
    [max_idle_time, 0].max + tasks.size
end
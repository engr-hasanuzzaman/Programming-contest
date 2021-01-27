=begin
use max queue to solve this problem. I have implement max queue by keeping tracking
of index as well as add_count, remove_count.
First initialize the array with q_size and take the first element
then (q_size to input size) dequeue element, enqueue element add max value to ans
=end
def enqueue(elm)
    while !@q.empty? && @q.first.first < elm
        @q.shift()
    end
    @q.unshift([elm, @add_count])
    @add_count += 1
end

def deenqueue()
    if @q[-1][1] == @remove_count
        @q.pop()
    end
    
    @remove_count += 1
end

def solve(arr, queries)
    ans = []
    queries.each do |q_size|
        @q = []
        c_ans = []
        @add_count = 0
        @remove_count = 0
        
        # fill the q_size
        q_size.times do |i|
            enqueue(arr[i])
        end
        c_ans.push(@q.last.first)

        # for each step dequeue, enqueue and find the max value
        q_size.upto(arr.size-1) do |i|
            deenqueue()
            enqueue(arr[i])
            c_ans.push(@q.last.first)
        end

        ans << c_ans.min
    end
    ans
end
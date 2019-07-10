# https://leetcode.com/problems/daily-temperatures/

# @param {Integer[]} t
# @return {Integer[]}
def daily_temperatures(t)
  result = []
  stack = []
  
  (t.size-1).downto(0) do |i|
      if !stack.empty? && t[i] < t[stack.last]
          result[i] = 1
          stack << i
      else
          while !stack.empty? && t[stack.last] <= t[i]
              stack.pop
          end
          # puts "--s #{stack}, #{t[i]}"
          if stack.empty?
              result[i] = 0
          else
              result[i] = stack.last - i
          end
          
          stack << i
      end
  end
  
  result
end
# https://leetcode.com/problems/queue-reconstruction-by-height/

# @param {Integer[][]} people
# @return {Integer[][]}
def reconstruct_queue(people)
  # sort by height and set position smallest to ...
  people = people.sort_by{|p| [p.first, p.last] }
  ans = Array.new(people.size)
  
  people.each do |p|
      i = 0
      h, k = p
      
       while k > 0 || (ans[i] && ans[i].first <= h)
          if ans[i] && ans[i].first < h
              i += 1 
              next
          end

          i += 1
          k -= 1
      end
      
      ans[i] = p
  end
  
  ans
end
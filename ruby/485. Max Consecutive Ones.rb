# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
    max_con = 0
    current_con = 0

    nums.each do |n|
      if n == 1
        current_con += 1
      else 
        max_con = max_con > current_con ? max_con : current_con
        current_con = 0
      end
    end
    
    max_con = max_con > current_con ? max_con : current_con
    
    return max_con
end

# https://leetcode.com/problems/paint-house-ii/

# @param {Integer[][]} costs
# @return {Integer}
def min_cost_ii(costs)
    total_costs = [costs.first]
    num_of_house = costs.size
    num_of_color = costs.first.size
    
   1.upto(num_of_house - 1) do |h_no|
       total_cur_cost = []
       num_of_color.times do |i|
           total_cur_cost << (total_costs[h_no - 1][0...i] + total_costs[h_no - 1][i+1..-1]).min + costs[h_no][i]
       end
       total_costs << total_cur_cost
   end
    
    total_costs.last.min
end

# time = O(n*k*k) , space O(n*k)
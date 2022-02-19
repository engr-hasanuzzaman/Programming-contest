# https://leetcode.com/problems/paint-house/

# @param {Integer[][]} costs
# @return {Integer}
def min_cost(costs)
    total_costs = [costs.first]
    
    1.upto(costs.size-1) do |h_number|
        optimal_cost_for_first_color = total_costs[h_number-1][1..2].min + costs[h_number][0]
        optimal_cost_for_second_color = [total_costs[h_number-1][0], total_costs[h_number-1][2]].min + costs[h_number][1]
        optimal_cost_for_third_color = total_costs[h_number-1][0..1].min + costs[h_number][2]
        
        total_costs << [optimal_cost_for_first_color, optimal_cost_for_second_color, optimal_cost_for_third_color]
    end
    
    total_costs.last.min
end

# [[1, 3, 5], [2, 4, 3], [3, 1, 2], [2,1,4]] -> 7
# total_costs = [[1, 3, 5], [5, 5, 4], [7, 5, 7], [7, 5, 7], [7, 8, 9]]
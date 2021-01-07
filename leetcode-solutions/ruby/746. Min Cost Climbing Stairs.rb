# https://leetcode.com/problems/min-cost-climbing-stairs/
def min_cost_climbing_stairs(cost)
    2.upto(cost.size-1) do |i|
      # we have two option, either come from i-1 step or i-2 step
      cost[i] = [cost[i-1], cost[i-2]].min + cost[i]
    end
   # to go top, we can either top tow floor
    cost[-2..-1].min
end
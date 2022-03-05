# https://leetcode.com/problems/watering-plants-ii/

# @param {Integer[]} plants
# @param {Integer} capacity_a
# @param {Integer} capacity_b
# @return {Integer}
def minimum_refill(plants, capacity_a, capacity_b)
    cur_cap_a = capacity_a
    cur_cap_b = capacity_b
    left = 0
    right = plants.size - 1
    num_of_fill = 0
    
    while left <= right
        if left == right
            num_of_fill += 1 if ([cur_cap_a, cur_cap_b].max < plants[left])
        else
            if plants[left] > cur_cap_a
                num_of_fill += 1
                cur_cap_a = capacity_a
            end
            
            if plants[right] > cur_cap_b
                cur_cap_b = capacity_b
                num_of_fill += 1
            end
            
            cur_cap_a -= plants[left]
            cur_cap_b -= plants[right]
        end
        left += 1
        right -= 1
    end
    
    num_of_fill
end

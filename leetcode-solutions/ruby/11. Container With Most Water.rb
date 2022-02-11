# https://leetcode.com/problems/container-with-most-water/

# @param {Integer[]} height
# @return {Integer}
def max_area(height)
    area = 0
    left = 0
    right = height.size - 1
    # there are two ways we can maximize area, with taking max distance or
    # with maximum height
    while left < right
        cur_area = [height[left], height[right]].min * (right - left)
        area = [area, cur_area].max
        if height[left] > height[right]
            new_right = right - 1
            while height[right] >= height[new_right] && new_right > left
                new_right -= 1
            end
            right = new_right
        else
            new_left = left + 1
            while height[left] >= height[new_left] && new_left < right
                new_left += 1
            end
            left = new_left
        end
    end
    
    area
end

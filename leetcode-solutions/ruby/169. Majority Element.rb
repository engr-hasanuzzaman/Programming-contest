# https://leetcode.com/problems/majority-element/

def majority_element(nums)
    # Boyer-Moore Voting Algorithm
   candidate = nil
   count = 0
   nums.each do |num|
       if count.zero?
           candidate = num
       end
       
       count += 1 if num == candidate
       count -= 1 if num != candidate
   end
   
   candidate
end

# since majority element frequency is > size / 2, if we sort the nums size / 2 th element will be
# the majority element
def majority_element(nums)
    nums.sort!
    nums[nums.size / 2]
end

# using hashmap
def majority_element(nums)
    e_counter = {}
    res = nums.first
    max_count = 0
    nums.each do |n|
        if e_counter[n]
            e_counter[n] += 1
        else
            e_counter[n] = 1
        end
        
        if e_counter[n] > nums.size / 2
            return n
        end
    end
end
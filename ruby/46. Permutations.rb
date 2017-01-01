# @param {Integer[]} nums
# @return {Integer[][]}
# this problem is like 'base case and build' type
# we will first make solution for base element here is the permutation with one element
# continuously inset additionaly element on previous result untill get final result
# premutation([1]) -> [[1]]
# premutation([1,2]) -> [[1,2],[2,1]]
# premutation([1,2,3]) -> insert 3 every position of every elements of permutaion([1,2])
def permute(nums)
    return [nums] if nums.size <= 1
    
    result = []
    num = nums[0]
    sub_permutation = permute(nums[1..-1])
    
    sub_permutation.each do |array|
        nums.size.times do |i|
          if i == 0 
            result << [num] + array
          elsif i == array.size
            result << array + [num]
          else
             result << (array[0..i-1] + [num] + array[i..-1])
          end 
       end
    end
    
   return result
end

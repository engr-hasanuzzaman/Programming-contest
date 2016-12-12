# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
# this solution is without using existing set datastructure
def intersection(nums1, nums2)
    nums1.uniq!
    nums2.uniq!
    result = []
    
    if nums1.size > nums2.size
        nums2.each do |n|
            result << n if nums1.include? n
        end
    else
        nums1.each do |n|
            result << n if nums2.include? n
        end
    end
    
   return result
end
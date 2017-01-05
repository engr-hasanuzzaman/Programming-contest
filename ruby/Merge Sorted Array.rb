# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
    n.times do |index|
        nums1[m] = nums2[index]
        
        m.downto(1).each do |i|
            break if nums1[i] > nums1[i - 1]
            
            nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]
        end
        
        m += 1
    end
    puts nums1.inspect
end

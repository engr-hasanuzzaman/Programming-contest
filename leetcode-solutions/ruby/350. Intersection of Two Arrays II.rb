# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
  map = {}
  ans = []
  nums1.each do |n|
      if map[n]
          map[n] += 1
      else
          map[n] = 1
      end
  end
  
  nums2.each do |n|
      if map[n] && map[n] > 0
         ans << n
          map[n] -= 1
      end
  end
  
  ans
end
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

# TLE solution with minHeap
require 'algorithms'
include Containers
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[][]}
def k_smallest_pairs(nums1, nums2, k)
    min_heap = MinHeap.new
    [k, nums1.size].min.times do |i|
        min_heap.push([nums1[i] + nums2[0], nums1[i], nums2[0], 0])
    end
    ans = []
    k.times do
        break if min_heap.empty?
        _, n1, n2, idx = min_heap.pop
        ans.push([n1, n2])
        if idx + 1 < nums2.size
            min_heap.push([n1+nums2[idx+1], n1, nums2[idx+1], idx+1])
        end
    end
    
    ans
end
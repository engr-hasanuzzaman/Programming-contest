// https://leetcode.com/problems/array-partition-i/

import (
	"fmt"
	"sort"
)

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	var ans int
	size := len(nums)
	fmt.Println(nums)
	for i := 0; i < size; i += 2 {
		ans += min(nums[i], nums[i+1])
	}

	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
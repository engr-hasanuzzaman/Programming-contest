package main

import "fmt"

// https://leetcode.com/problems/find-pivot-index/

func pivotIndex(nums []int) int {
	var sum int
	for _, n := range nums {
		sum += n
	}
	fmt.Println("sum ", sum)

	var curSum int
	for i, n := range nums {
		if curSum == (sum - n - curSum) {
			return i
		}

		curSum += n
	}

	return -1
}

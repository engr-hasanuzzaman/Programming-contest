// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

func dominantIndex(nums []int) int {
	var largestNum int
	var ans int

	for i, n := range nums {
		if largestNum < n {
			largestNum = n
			ans = i
		}
	}

	for _, n := range nums {
		if n != largestNum && 2*n > largestNum {
			return -1
		}
	}

	return ans
}
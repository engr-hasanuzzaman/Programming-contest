// https://leetcode.com/problems/plus-one/

func plusOne(digits []int) []int {
	size := len(digits)
	rem := 1 // add 1 to number
	for i := size - 1; i >= 0; i-- {
		if digits[i]+rem >= 10 {
			digits[i] = 0
			rem = 1
		} else {
			digits[i] = digits[i] + rem
			rem = 0
		}
	}

	if rem == 1 {
		ans := make([]int, size+1)
		ans[0] = 1
		for i := 1; i <= size; i++ {
			ans[i] = digits[i-1]
		}
		digits = ans
	}

	return digits
}


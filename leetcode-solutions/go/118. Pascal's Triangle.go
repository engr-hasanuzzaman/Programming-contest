// https://leetcode.com/problems/pascals-triangle/

func generate(numRows int) [][]int {
	// rows := make([]int, numRows)
	result := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
			result[i] = make([]int, i+1)
	}
	for i := 0; i < numRows; i++ {
			for j := 0; j <= i; j++ {
					if j == 0 || j == i {
							result[i][j] = 1
					}else {
							result[i][j] = result[i-1][j-1] + result[i-1][j]
					}
			} 
	}   
	
	return result
}
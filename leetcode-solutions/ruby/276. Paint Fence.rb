=begin
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1

    f(0) = 0; // zero posts, so zero ways
    f(1) = k; // one post, so you can paint all k colors
	
If you want to paint the second fence the SAME color as the previous fence, you will only have one option. 
If you want to paint the second fence a DIFFERENT color than the previous fence, you will have (k-1) options. 
You have to subtract 1 to account for the color of the previous fence.

	same: 1 (one option only)
    diff: (k-1)  (k colors minus 1 to account for color of previous fence)
	
so for two fence posts, you will add up same + diff to get all the ways you can paint the two fence posts.
	same = k * 1 
	diff = k * (k-1) 
    f(2) = same + diff = k * 1 + k * (k -1) 
    
	recurrance relation
    diff = (diff + same) * (k-1);
    same = (diff) * 1
	
	runtime 0(n), space complexity (1)
=end

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def num_ways(n, k)
    return 0 if n == 0
    return k if n == 1
    return k+k*(k-1) if n == 2
    
    dp = []
    dp[0] = k
    dp[1] = k + k*(k-1)
    
    for i in 2...n
        dp[i] = (k-1)*(dp[i-2] + dp[i-1])
    end
    
    dp.last
end
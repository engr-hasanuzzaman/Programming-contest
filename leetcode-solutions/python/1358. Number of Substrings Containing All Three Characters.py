# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

# wrong answere
# use prefix sum to keep the counter of previous index's counter of a,b,c on a particular index
# check generate all the sub-string and check how many a,b,c in that range in a constant time
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # (a_counter, b_counter, c_counter)
        counter_arr = [[0,0,0] for _ in range(len(s) + 1)]
        cur_counter = [0, 0, 0]
        for i, c in enumerate(s):
            counter_arr[i] = cur_counter[:]
            cur_counter[ord(c) - ord('a')] += 1
        counter_arr[-1] = cur_counter[:]

        ans = 0
        # loop throught all the sub-string and check
        min_size = 3
        # this part is taking too much of the time
        # if we can calculate how many sub-string will contain the current sub-string
        # it would not re-calculate again
        for size in range(min_size, len(s)+1):
            for start in range(len(s) - size + 1):
                num_of_a = counter_arr[start+size][0] - counter_arr[start][0]
                num_of_b = counter_arr[start+size][1] - counter_arr[start][1] 
                num_of_c = counter_arr[start+size][2] - counter_arr[start][2] 
                if num_of_a > 0 and num_of_b > 0 and num_of_c > 0:
                    ans += 1
        return ans

# solution using dynamic programming and sliding window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #a, b, c
        cur_counter = [0, 0, 0]
        left = 0
        result = 0
        for right, char in enumerate(s):
            cur_counter[ord(char) - ord('a')] += 1
            while cur_counter[0] > 0 and cur_counter[1] > 0 and cur_counter[2] > 0:
                result += len(s) - right
                cur_counter[ord(s[left]) - ord('a')] -= 1
                left += 1
        return result

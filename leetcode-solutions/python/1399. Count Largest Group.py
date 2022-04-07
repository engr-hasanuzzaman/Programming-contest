# https://leetcode.com/problems/count-largest-group/
class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = {}
        max_group_size = 0
        for i in range(1, n+1):
            sum = digit_sum(i)
            if sum in group:
                group[sum].append(i)
            else:
                group[sum] = [i]
            max_group_size = max(max_group_size, len(group[sum]))
        count = 0
        for g in group.values():
                if len(g) == max_group_size:
                    count += 1
        return count

def digit_sum(num):
    sum = 0
    while num > 0:
        sum += (num % 10)
        num //= 10
    return sum

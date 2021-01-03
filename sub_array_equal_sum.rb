class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        total= sum(arr)
        memo = {}
        memo['optimal_sub_sum'] = total
        Solution.calculate_min_diff(memo, arr, 0, 0, total)
        print(memo['optimal_sub_sum'])
        # print(memo)
        return abs(total - 2*memo['optimal_sub_sum']) == 0
    def calculate_min_diff(memo, arr, i, current_total, total):
        memo_key = str(i) + "_" + str(current_total)
        if memo_key in memo:
            return memo[memo_key]
        if i >= len(arr) or current_total * 2 > total:
            memo[memo_key] = total - current_total
            if abs(total - 2*memo['optimal_sub_sum']) > abs(total - 2*memo[memo_key]):
                memo['optimal_sub_sum'] = memo[memo_key]
            return memo[memo_key]
        # we have two choice, either we can consider the current item
        # or skip the current item
        with_current_item = Solution.calculate_min_diff(memo, arr, i+1, current_total+arr[i], total)
        # with_current_item = Solution.calculate_min_diff(memo,arr, i+1, current_total+arr[i], total )
        without_current_item = Solution.calculate_min_diff(memo, arr, i+1, current_total, total)
        if abs(total - with_current_item * 2) > abs(total - without_current_item * 2):
            memo[memo_key] = without_current_item
        else:
            memo[memo_key] = with_current_item

        if abs(total - 2*memo['optimal_sub_sum']) > abs(total - 2*memo[memo_key]):
            memo['optimal_sub_sum'] = memo[memo_key]

        return memo[memo_key]
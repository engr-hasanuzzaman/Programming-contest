# https://leetcode.com/problems/3sum-with-multiplicity/

# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def three_sum_multi(arr, target)
  mod = 10**9 + 7
  ans = 0
  arr.sort!

  arr.each_with_index do |n, i|
    rem = target - n

    # two pointer technique
    left = i + 1
    right = arr.size - 1
    while left < right
      if arr[left] + arr[right] > rem
        right -= 1
      elsif arr[left] + arr[right] < rem
        left += 1
      # found our first pair, now lookinf for how many such pair exist
      elsif arr[left] != arr[right]
        l_count = 1
        r_count = 1
        while left < right && arr[left] == arr[left + 1]
          l_count += 1
          left += 1
        end

        while right > left && arr[right] == arr[right - 1]
          r_count += 1
          right -= 1
        end

        ans += r_count * l_count
        left += 1
        right -= 1
      # if left & right are same
      else
        ans += ((right - left + 1) * (right - left)) / 2
        # entire array considered
        break
      end
    end
  end

  ans % mod
end

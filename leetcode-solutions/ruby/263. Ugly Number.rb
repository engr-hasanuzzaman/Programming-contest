# https://leetcode.com/problems/ugly-number/

# @param {Integer} n
# @return {Boolean}
def is_ugly(n)
  return false if n <= 0
  return true if n <= 6

  [2, 3, 5].each do |factor|
    n /= factor while (n % factor).zero?
  end

  n == 1
end

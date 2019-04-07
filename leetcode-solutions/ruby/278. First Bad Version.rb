# https://leetcode.com/problems/first-bad-version/

# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
  low = 1
  high = n
  
  while low < high
      mid = (low + high) / 2
      r = is_bad_version(mid)
      if r 
          high = mid
      else
          low = mid + 1
      end
  end
 
  low
end
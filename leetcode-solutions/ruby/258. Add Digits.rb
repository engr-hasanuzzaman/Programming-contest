# 

# constant time
# @param {Integer} num
# @return {Integer}
def add_digits(num)
  if num.zero?
      return num
  elsif num % 9 == 0
      return 9
  else
      num % 9
  end
end
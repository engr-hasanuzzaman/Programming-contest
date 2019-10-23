# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
  counter = 0
  1.upto(n) do |num|
      counter +=1 if good_number?(num)
  end

  counter
end

def good_number?(n)
  good_numbers = ['2', '5', '6', '9']
  s_n = n.to_s
  puts "-s_n #{s_n}"
  good_numbers.each do |n|
      s_n.delete!(n)
  end
  puts "---#{s_n}"
  s_n.size.zero?
end

puts rotated_digits(10)
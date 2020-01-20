# https://leetcode.com/problems/maximum-69-number/

# @param {Integer} num
# @return {Integer}
def maximum69_number (num)
  s_num = num.to_s.split('')
  
  s_num.each_index do |i|
      if s_num[i] == '6'
          s_num[i] = '9'
          break
      end
  end
   
  s_num.join.to_i
end
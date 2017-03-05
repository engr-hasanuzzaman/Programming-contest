#!/bin/ruby

time = gets.strip
h = time.split(':')[0].to_i
m = time.split(':')[1].to_i
s = time.split(':')[2][0..1].to_i
period = time[-2...time.size]

# puts "h = #{h}, m = #{m}, s = #{s}, period = #{period}"
if period.downcase == 'am'
    if h == 12
      h = 0 
    end
else
  h = (h % 12) + 12
end

puts "#{"%02d" % h}:#{"%02d" % m}:#{"%02d" % s}"

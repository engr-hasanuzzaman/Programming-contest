def flip(n)
  num_of_bits = (Math.log(n, 2)).to_i
  # find the max num with all bit set with num_of_bits
  m = 1 << num_of_bits
  m = m | (m - 1)
  puts "n = #{n}, b(n) = #{n.to_s(2)}, after flipping #{(m^n).to_s(2)} #{(m^n).to_s}"
end

(1..20).each do |n|
  flip(n)
end

def rp(s)
  return if s.size.zero?
  rp(s[1..-1])
  print s[0]
end

rp("sumon")
puts ''
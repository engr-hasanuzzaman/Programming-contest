def polynomial_mul(a, b)
  result = Array.new(a.size + b.size - 1){ 0 }
  
  a.size.times do |i|
    b.size.times do |j|
      result[i + j] = result[i + j] + a[i] * b[j]
    end
  end 
  
  return result
end

def print_polynomial(a)
  a.each_with_index do |c, i|
    if i.zero?
      print "#{c}"
    else
      print " + #{c}X^#{i}"
    end 
  end
  
  puts ''
end

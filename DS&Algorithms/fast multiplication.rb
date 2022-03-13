def pow(a, n)
    return 1 if n.zero?

    res = pow(a, n/2)
    if n.even?
        res * res
    else
        res * res * a
    end
end

puts "----(2,4) #{pow(2, 4)}"
puts "----(2,5) #{pow(2, 5)}"
puts "----(3,6) #{pow(3, 6)}"
puts "----(6,3) #{pow(6, 3)}"
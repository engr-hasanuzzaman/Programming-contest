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

def fast_pow_iterative(a, n)
    res = 1
    while n > 0
        if n & 1 == 1 # when get set bit, perform operation
            res = res * a
        end
        a = a * a
        n >>= 1 # right shift
    end
    res
end
puts "-------------------"
puts "----(2,4) #{fast_pow_iterative(2, 4)}"
puts "----(2,5) #{fast_pow_iterative(2, 5)}"
puts "----(3,6) #{fast_pow_iterative(3, 6)}"
puts "----(6,3) #{fast_pow_iterative(6, 3)}"
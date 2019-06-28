#Given two numbers a and b, write a fast method to multiply both of them.
#Algorithm: Russian Peasant
=begin
1. Initialize ans=0
2. if b is odd ,add a to ans
3. double a,half b
4. repeat steps 2 and 3 until b>0
=end


def multiply(a, b)
  p "a: #{a}, b: #{b}"
  a, b = b, a if b > a # makesure b is smaller then a
  ans = 0
  while b > 0
    ans += a if b % 2 != 0
    b /= 2
    a *= 2
  end

  ans
end
p ARGV
n1 = (ARGV[0] && ARGV[0].to_i) || 20
n2 = (ARGV[1] && ARGV[1].to_i) || 5
p n1, n2
p multiply(n1, n2)
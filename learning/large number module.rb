# ( a + b ) mod m = ( a mod m + b mod m ) mod m
# ( a − b ) mod m = ( a mod m − b mod m ) mod m
# ( a · b ) mod m = ( a mod m · b mod m ) mod m

a = 123456789
b = 987654321
m = 5578

puts "Actual sum module #{(a+b) % m}"
puts "calculative module #{(a % m + b % m) % m}"

puts "Actual substract module #{(a-b) % m}"
puts "calculative module #{(a % m - b % m) % m}"

puts "Actual product module #{(a*b) % m}"
puts "calculative module #{(a % m * b % m) % m}"

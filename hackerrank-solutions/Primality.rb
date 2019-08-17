def primality(n)
  return "Not prime" if n <= 1

  n_sqrt = Math.sqrt(n)
  (2..n_sqrt).each do |d|
    # puts "d #{d}, #{n}"
    return "Not prime" if n % d == 0
  end

  "Prime"
end

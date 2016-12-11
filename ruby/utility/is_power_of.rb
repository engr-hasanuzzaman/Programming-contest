# if a number n is power of p, then if we keeping divition like 
# following code then we will det final divition rusult 1
# n = n / pow 
def is_power_of(num, pow)
	while(num > 1) do
		return false unless num % pow == 0

		num /= pow
	end

	return num == 1
end


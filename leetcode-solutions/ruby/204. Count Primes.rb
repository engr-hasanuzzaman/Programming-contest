# @param {Integer} n
# @return {Integer}
# Using  Sieve of Eratosthenes Algorithm
def count_primes(n)
    # to track which numbe is prime or not
    # initially cosider all number are prime
    isPrime = Array.new(n){ true }
    count = 0
    num = 2
    
    while(num * num < n)
        # if num is non-prime then already it's multiple also mark as non-prime
        unless isPrime[num]
          num += 1
          next
        end
        
        # start with p*p, because before that number will be 
        # mark by other number
        p = num * num
        
        while(p < n)
            isPrime[p] = false
            p += num
        end
        
        num += 1
    end
    
    # skip positon 0 & 1
    2.upto(n - 1).each do |i|
        count += 1 if isPrime[i]
    end
     
    return count
end

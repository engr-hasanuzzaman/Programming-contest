# @param {Integer} n
# @return {Integer}
def count_primes(n)
    count = 0
    
    # count number less then n 
    n -= 1
    n.downto(2).each do |num|
        count += 1 if num.prime?
    end
    
    return count
end

class Integer
    def prime?
        return false if self <= 1
        
        Math.sqrt(self).to_i.downto(2).each{ |n| return false if self % n == 0 }
        
        return true
    end
end

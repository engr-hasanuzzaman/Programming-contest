# @param {String} s
# @return {Integer}
def title_to_number(s)
   mapping = {}    
   ('A'..'Z').each_with_index{|n, i| mapping[n] = i.next }
   
    s.reverse!

    # A..Z work like base 26 number 
    base = 26
    sum = 0
    
    s.split('').each_with_index do |n, i|
    	# construct number 
        sum += base**i * mapping[n]
    end
    
    return sum
end
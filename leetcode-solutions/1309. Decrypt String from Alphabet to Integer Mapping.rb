# @param {String} s
# @return {String}
def freq_alphabets(s)
    
end

def to_c(str)
    s = str.size
    if s <= 2
        return (64 + str.to_i).chr
    end

    i = 0
    ans = ''
    i.upto(s - 3) do |o|
      ans += (64 + o.to_i).chr
    end 

    ans += (64 + str[-2:-1].to_i).chr
    ans
end
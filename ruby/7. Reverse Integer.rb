# @param {Integer} x
# @return {Integer}
 FIXNUM_MAX = 2147483647
 FIXNUM_MIN = -2147483648
def reverse(x)
    if x < 0
        number =  -x.to_s.reverse.to_i
        if number < FIXNUM_MIN
            return 0
        else
            return number
        end
    else
        number = x.to_s.reverse.to_i
        
        if number > FIXNUM_MAX
            return 0
        else
            return number
        end
    end
end

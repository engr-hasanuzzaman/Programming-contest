# @param {Integer} a
# @param {Integer} b
# @return {Integer}
=begin
- Assuming you understood the bit manipulation method in other languages.
- The solution in Python is different than other languages because in Python it considers the unlimited length of integers whereas in other languages integers has fixed length of 32-bit.
- If we perform the normal bit manipulation solution in python then the loop runs for infinite times as integers are not fixed to 32-bit. To avoid this in python we use a MASK 0xffffffff to keep the integer in 32-bits.
- At last we have conditions to return the value because especially for negative integers we have to first calculate the two's complement of the returning number. But only ~a will flip infinite bits of a and hence we have limit it in 32-bit using MASK. Thus we xor a with mask and finally return ~(a^MASK).
=end
def get_sum(a, b)
    return a if b.zero?
    
    mask = 0xffffffff # limit with in 32 bit
    
    while b != 0
        c = a & b # carry
        a = (a ^ b) & mask # sum
        b = (c << 1) & mask # carry will be applied on left shifted item
    end
    
    return ~(a ^ mask) if ((a >> 31) & 1) == 1
    a
end

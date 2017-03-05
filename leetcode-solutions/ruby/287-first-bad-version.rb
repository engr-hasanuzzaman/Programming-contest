# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    return n if n == 1
    
    array = (1..n).to_a
    first_bad = n
    
    loop do 
        if array.size == 1 
            return array[0]
        end
        
        middle = array.size / 2
        
        if is_bad_version(middle)
            array = (1..middle).to_a
        else
            array = ((middle+1)..n).to_a
        end
    end
end

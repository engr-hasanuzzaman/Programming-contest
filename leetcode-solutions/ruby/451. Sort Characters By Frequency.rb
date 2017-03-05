# @param {String} s
# @return {String}
def frequency_sort(s)
    h = s.chars.each_with_object(Hash.new(0)){|i, h| h[i] += 1 }
    h = h.sort_by{|k, v| -v}
    result = ''
    h.each do |a|
        result += a[0] * a[1]
    end
    
    result
end

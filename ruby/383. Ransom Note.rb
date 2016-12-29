# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
    hash = ransom_note.chars.each_with_object(Hash.new(0)){|c, h| h[c] += 1}
    
    magazine.chars.each do |c|
        hash[c] -= 1
    end
    
    hash.values().select{|n| n > 0}.size == 0
end

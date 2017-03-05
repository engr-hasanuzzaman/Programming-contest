# @param {String} version1
# @param {String} version2
# @return {Integer}
def compare_version(version1, version2)
    version1 = version1.split('.').map(&:to_i)
    version2 = version2.split('.').map(&:to_i)
    
    #  take max length of array
    max_length =  version2.size > version1.size ? version2.size : version1.size 
       
    max_length.size.times do |index|
        if version1.fetch(index, 0) > version2.fetch(index, 0)
            return 1
        end
        
        if version2.fetch(index, 0) > version1.fetch(index, 0)
            return -1
        end
    end
    
    return 0
end

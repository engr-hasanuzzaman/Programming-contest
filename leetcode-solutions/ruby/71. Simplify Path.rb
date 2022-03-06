# https://leetcode.com/problems/simplify-path/

# @param {String} path
# @return {String}
def simplify_path(path)
    paths = path.split("/")
    canonical_path = []
    
    paths.each do |dir|
        if dir == "" or dir == "."
            next
        end
        
        if dir == '..'
            canonical_path.pop
        else
            canonical_path << dir
        end
    end
    
    "/#{canonical_path.join("/")}"
end

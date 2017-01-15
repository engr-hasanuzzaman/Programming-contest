# @return {Boolean}
def repeated_substring_pattern(str)
    s_len = str.size
    # return true if s_len == 1
    
    sub_str_size = s_len / 2 
    
    while(sub_str_size >= 1)
      if s_len % sub_str_size != 0
          sub_str_size -= 1
          next
      end
      
    #   take str with size sub_str_size
    return true if str[0...sub_str_size] * (s_len / sub_str_size) == str
    sub_str_size -= 1
    end 
     
    return false 
end

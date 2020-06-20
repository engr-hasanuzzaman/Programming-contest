
def rot13(secret_messages)
  # your code here
    c_arr = ('a'..'z').to_a
    capital_c_arr = ('A'..'Z').to_a
    secret_messages.map do |str|
        str.split("").map do |c|
            if c.ord >= 'a'.ord && c.ord <= 'z'.ord
                c_arr[(c.ord + 13 - 'a'.ord)%26]
            elsif c.ord >= 'A'.ord && c.ord <= 'Z'.ord
                c_arr[(c.ord + 13 - 'A'.ord)%26]
            else
                c
            end
        end.join("")
    end
end

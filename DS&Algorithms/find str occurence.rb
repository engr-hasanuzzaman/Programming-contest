=begin
input: CodeNCode is the best resouce for competitive coding, co
output: 2 as competitive & coding contains co
=end
def str_find(text, str)
    str_freq = Hash.new(0)
    str.each_char do |chr|
        str_freq[chr] += 1
    end

    window_size = str.size
    left =  right = 0
    chr_count = 0
    ans = []
    cur_str_freq = str_freq.dup
    while right < text.size
        chr = text[right]
        unless str_freq.key?(chr)
            right += 1
            left = right
            chr_count = 0
            cur_str_freq = str_freq.dup
            next
        end

        cur_str_freq[chr] -= 1
        chr_count += 1

        #shrink the window size
        while chr_count > window_size || cur_str_freq[chr] < 0
            chr_count -= 1
            cur_str_freq[text[left]] += 1
            left += 1
        end

        if chr_count == window_size
            # puts " c #{chr_count}, #{cur_str_freq} #{left}, #{right}"
            ans << left
        end
        right += 1
    end

    ans
end

text = 'CodeNCode is the best resouce for competitive coding CaCCC'
str = 'Co'
puts "---------#{str_find(text, str)} === [0, 5]"
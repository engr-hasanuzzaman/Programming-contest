# Enter your code here. Read input from STDIN. Print output to STDOUT
str = gets.strip.chars
result = []
i = 0
while i < str.size
    if str[i] == str[i.next]
        i += 2
    elsif result[-1] == str[i] # check for input like 'abba' or 'abbabbabba'
        result.pop
        i += 1
    else
        result << str[i]
        i += 1
    end
end

if result.size.zero?
    print 'Empty String'
else
    print result.join('')
end

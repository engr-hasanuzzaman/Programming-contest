# method that handle the operation on the provided register
def exec_operation(operation, register, i, j)
    case operation
    when 'CLEAR'
        register[i] = 0
    when 'SET'
        register[i] = 1
    when 'OR'
        register[i] = or_operation(register, i, j)
    when 'AND'
        register[i] = and_operation(register, i, j)
    end 
end

# helper methods that handle the bitwise AND operation
def and_operation(s, i, j)
    if s[i] == '?' && s[j] == '?'
        '?'
    elsif s[i] == '?' || s[j] == '?'
        if s[i] == '?'
            if s[j] == 1
                return '?'
            else
                return 0
            end
        else
            if s[i] == 1
                return '?'
            else
                return 0
            end
        end
    else
        s[i] & s[j]
    end
end

# handle bitwise OR operation
def or_operation(s, i, j)
    if s[i] == 1 || s[j] == 1
        1
    elsif s[i] == 0 && s[j] == 0
        0
    else
        '?'
    end
end

# read the input and perform the operation
ans = []
number_of_operations = 0
register = []

ARGF.each_line do |line|
    # save the current resutl and exit
    if line === '0' || line === 0
        ans << register.join
        break
    end

    # handle different set of test input and store the current register to ans array
    if number_of_operations.zero?
        number_of_operations = line.to_i
        ans << register.join
        register = ['?'] * 32
    else
        number_of_operations -= 1
        operation, i, j = line.split(" ")
        exec_operation(operation, register, 31 - i.to_i, 31 - j.to_i)
    end
end

ans[1..-1].each {|o| puts o}

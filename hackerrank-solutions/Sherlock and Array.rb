# Enter your code here. Read input from STDIN. Print output to STDOUT
N = gets.strip.to_i
N.times do 
    input_size = gets.strip.to_i
    input = gets.strip.split(' ').map(&:to_i)
    total = input.reduce(:+)
    left_side_total = 0
    result = nil
    
    input.size.times do |i|
        if left_side_total * 2 == (total - input[i])
            result = 'YES'
            break
        end
        
        left_side_total += input[i]
    end
    result ||= 'NO'
    puts result
end

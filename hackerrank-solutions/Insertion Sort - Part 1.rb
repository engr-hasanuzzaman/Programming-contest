def  insertionSort( ar) 
    e = ar.last
    size = ar.size
    (size - 1).downto(0) do |i|
        if i.zero?
            ar[i] = e
            break
        elsif e > ar[i -1]
            ar[i] = e
            break
        else
            ar[i] = ar[i - 1]
        end
        
        print_ar(ar)
    end
    
    print_ar(ar)
end

def print_ar(ar)
    ar.each{|n| print "#{n} "}
    puts ''
end

count = gets.to_i
ar = gets.strip.split.map {|i| i.to_i}

insertionSort( ar )

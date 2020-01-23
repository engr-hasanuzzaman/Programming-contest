def m_window(arr, w)
  dq, s = [], 0
  out = []
  
  arr.each_index do |i|
    puts "---#{dq}, s = #{s}, #{out}, #{i}"
    while dq[s] && arr[dq.last] < arr[i]
      puts "pop"
      dq.pop
    end
    
    dq << i
    s += 1 if dq[s] == i - w
    out << arr[dq[s]] if i >= w - 1
  end
  
  out.join(" ")
end

a = m_window([2, 1, 2, -1, 3], 2)
puts "ans #{a}"

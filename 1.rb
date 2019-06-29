# input_size = input_array[0].to_i
# arr = input_array[1].split(' ').map(&:to_i)

input_array = []
STDIN.read.split("\n").each do |a|
  input_array << a
end

# process input data
input_size = input_array[0].to_i
arr = input_array[1].split(' ').map(&:to_i)

def highest_product(arr_length, arr)
  return -1 if arr_length < 3
  
  get_larget_three(arr).reduce(&:*)
end  

def get_larget_three(arr)
# bubble sort for only 3 items
arr_size = arr.size
  3.times do |i|
    (arr_size - i -1).times do |j|
  #   p "--j #{j}, #{arr[j]}, #{arr[j+1]}"
      if arr[j] > arr[j+1]
        arr[j], arr[j+1] = arr[j+1], arr[j]
      end 
    end
  end
 
  arr[-3..-1]
end

p highest_product(input_size, arr)
